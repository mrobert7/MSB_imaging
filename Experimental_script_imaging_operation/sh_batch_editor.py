#!/usr/bin/env python3
"""Small GUI to batch-edit libcamera options in .sh files.

Requirements:
- Standard library only (tkinter, pathlib, re)
- Works across common Python 3 versions

Quick setup on a new PC:
1) Install Python 3 (3.8+ recommended)
2) Run this script:
    python sh_batch_editor.py

If tkinter is missing:
- Ubuntu/Debian: sudo apt-get update; sudo apt-get install -y python3-tk
- Fedora: sudo dnf install -y python3-tkinter
- Arch: sudo pacman -S tk
- Windows/macOS: reinstall official Python from python.org and keep Tcl/Tk enabled
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

try:
    import tkinter as tk
    from tkinter import ttk, messagebox, filedialog
except Exception as exc:  # pragma: no cover - startup-only environment check
    msg = (
        "Tkinter is not available in this Python installation.\n\n"
        "Install/fix Tk and run again:\n"
        "- Ubuntu/Debian: sudo apt-get update; sudo apt-get install -y python3-tk\n"
        "- Fedora: sudo dnf install -y python3-tkinter\n"
        "- Arch: sudo pacman -S tk\n"
        "- Windows/macOS: reinstall Python from python.org with Tcl/Tk enabled\n"
    )
    raise SystemExit(msg) from exc


SCRIPT_PATTERN = "test*.sh"
PIP_PACKAGES: tuple[str, ...] = ()
FIRST_RUN_FLAG = Path(__file__).with_name(".sh_batch_editor_first_run_done")
FIRST_RUN_FLAG.exists() or ((subprocess.check_call([sys.executable, "-m", "pip", "install", *PIP_PACKAGES]) if PIP_PACKAGES else True) and FIRST_RUN_FLAG.write_text("done\n", encoding="utf-8"))


def replace_or_add_option(command: str, option: str, value: str) -> str:
    """Replace --option value if present, otherwise append it."""
    pattern = rf"({re.escape(option)}\s+)(\S+)"
    if re.search(pattern, command):
        return re.sub(pattern, rf"\g<1>{value}", command, count=1)
    return f"{command} {option} {value}".strip()


def set_flag(command: str, flag: str, enabled: bool) -> str:
    """Ensure a flag exists (enabled) or is removed (disabled)."""
    flag_pattern = rf"(?<!\S){re.escape(flag)}(?!\S)"
    has_flag = re.search(flag_pattern, command) is not None
    if enabled and not has_flag:
        return f"{command} {flag}".strip()
    if not enabled and has_flag:
        command = re.sub(flag_pattern, "", command)
        command = re.sub(r"\s+", " ", command).strip()
    return command


def update_command_line(command: str, changes: dict[str, object]) -> str:
    """Apply requested parameter changes to a libcamera-still command line."""
    updated = command

    if changes.get("width") is not None:
        updated = replace_or_add_option(updated, "--width", str(changes["width"]))
    if changes.get("height") is not None:
        updated = replace_or_add_option(updated, "--height", str(changes["height"]))
    if changes.get("contrast") is not None:
        updated = replace_or_add_option(updated, "--contrast", str(changes["contrast"]))
    if changes.get("brightness") is not None:
        updated = replace_or_add_option(updated, "--brightness", str(changes["brightness"]))
    if changes.get("shutter") is not None:
        updated = replace_or_add_option(updated, "--shutter", str(changes["shutter"]))
    if changes.get("denoise") is not None:
        updated = replace_or_add_option(updated, "--denoise", str(changes["denoise"]))
    if changes.get("awbgains") is not None:
        updated = replace_or_add_option(updated, "--awbgains", str(changes["awbgains"]))
    if changes.get("output") is not None:
        updated = replace_or_add_option(updated, "-o", str(changes["output"]))

    if changes.get("datetime") is not None:
        updated = set_flag(updated, "--datetime", bool(changes["datetime"]))
    if changes.get("no_preview") is not None:
        updated = set_flag(updated, "-n", bool(changes["no_preview"]))

    return re.sub(r"\s+", " ", updated).strip()


class ParameterRow:
    def __init__(
        self,
        parent: tk.Widget,
        row: int,
        name: str,
        default: str = "",
        on_toggle=None,
        on_commit=None,
    ) -> None:
        self.enabled_var = tk.BooleanVar(value=False)
        self.value_var = tk.StringVar(value=default)

        ttk.Checkbutton(parent, text=name, variable=self.enabled_var, command=on_toggle).grid(
            row=row, column=0, sticky="w", padx=(0, 8), pady=2
        )
        self.entry = ttk.Entry(parent, textvariable=self.value_var, width=22)
        self.entry.grid(row=row, column=1, sticky="ew", pady=2)
        self.entry.bind("<FocusOut>", lambda _e: on_commit() if on_commit else None)
        self.entry.bind("<Return>", lambda _e: on_commit() if on_commit else None)


class ChoiceRow:
    def __init__(
        self,
        parent: tk.Widget,
        row: int,
        name: str,
        choices: list[str],
        default: str,
        on_toggle=None,
        on_commit=None,
    ) -> None:
        self.enabled_var = tk.BooleanVar(value=False)
        self.value_var = tk.StringVar(value=default)

        ttk.Checkbutton(parent, text=name, variable=self.enabled_var, command=on_toggle).grid(
            row=row, column=0, sticky="w", padx=(0, 8), pady=2
        )
        self.combo = ttk.Combobox(
            parent,
            textvariable=self.value_var,
            values=choices,
            state="readonly",
            width=20,
        )
        self.combo.grid(row=row, column=1, sticky="ew", pady=2)
        self.combo.bind("<<ComboboxSelected>>", lambda _e: on_commit() if on_commit else None)


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("SH Batch Editor")
        self.geometry("860x560")
        self.minsize(760, 500)

        self.script_dir = Path(__file__).resolve().parent
        self.base_dir = self.script_dir
        self.files = sorted(self.base_dir.glob(SCRIPT_PATTERN))

        self._build_ui()
        self._load_files()

    def _build_ui(self) -> None:
        main = ttk.Frame(self, padding=10)
        main.pack(fill="both", expand=True)
        main.columnconfigure(0, weight=1)
        main.columnconfigure(1, weight=1)

        left = ttk.LabelFrame(main, text="Shell Scripts", padding=8)
        left.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
        left.rowconfigure(1, weight=1)
        left.columnconfigure(0, weight=1)

        dir_row = ttk.Frame(left)
        dir_row.grid(row=0, column=0, sticky="ew", pady=(0, 6))
        dir_row.columnconfigure(0, weight=1)

        self.target_dir_var = tk.StringVar(value=str(self.base_dir))
        ttk.Entry(dir_row, textvariable=self.target_dir_var).grid(row=0, column=0, sticky="ew")
        ttk.Button(dir_row, text="Set", command=self._set_folder_from_entry).grid(row=0, column=1, padx=(6, 0))
        ttk.Button(dir_row, text="Browse", command=self._browse_folder).grid(row=0, column=2, padx=(6, 0))
        ttk.Button(dir_row, text="Script Folder", command=self._use_script_folder).grid(row=0, column=3, padx=(6, 0))

        self.file_list = tk.Listbox(left, selectmode=tk.EXTENDED, exportselection=False)
        self.file_list.grid(row=1, column=0, sticky="nsew")

        btn_row = ttk.Frame(left)
        btn_row.grid(row=2, column=0, sticky="ew", pady=(8, 0))
        ttk.Button(btn_row, text="Select All", command=self._select_all).pack(side="left")
        ttk.Button(btn_row, text="Clear", command=self._clear_selection).pack(side="left", padx=(8, 0))
        ttk.Button(btn_row, text="Refresh", command=self._refresh_files).pack(side="left", padx=(8, 0))
        ttk.Button(btn_row, text="Apply All Files", command=self.apply_changes_all_files).pack(side="left", padx=(8, 0))

        right = ttk.LabelFrame(main, text="Parameters To Edit", padding=8)
        right.grid(row=0, column=1, sticky="nsew")
        right.columnconfigure(1, weight=1)

        self.rows: dict[str, object] = {}
        line = 0
        self.rows["width"] = ParameterRow(right, line, "--width", "2312", on_toggle=self._on_param_toggled, on_commit=self._auto_apply_if_enabled)
        line += 1
        self.rows["height"] = ParameterRow(right, line, "--height", "1736", on_toggle=self._on_param_toggled, on_commit=self._auto_apply_if_enabled)
        line += 1
        self.rows["contrast"] = ParameterRow(right, line, "--contrast", "1.0", on_toggle=self._on_param_toggled, on_commit=self._auto_apply_if_enabled)
        line += 1
        self.rows["brightness"] = ParameterRow(right, line, "--brightness", "0.1", on_toggle=self._on_param_toggled, on_commit=self._auto_apply_if_enabled)
        line += 1
        self.rows["shutter"] = ParameterRow(right, line, "--shutter", "500", on_toggle=self._on_param_toggled, on_commit=self._auto_apply_if_enabled)
        line += 1
        self.rows["denoise"] = ChoiceRow(
            right,
            line,
            "--denoise",
            ["off", "auto", "cdn_off", "cdn_fast", "cdn_hq"],
            "off",
            on_toggle=self._on_param_toggled,
            on_commit=self._auto_apply_if_enabled,
        )
        line += 1
        self.rows["awbgains"] = ParameterRow(right, line, "--awbgains", "1.5,2.0", on_toggle=self._on_param_toggled, on_commit=self._auto_apply_if_enabled)
        line += 1
        self.rows["output"] = ParameterRow(
            right,
            line,
            "-o output path",
            "/media/raspberry4/Raspi_USB/slotimaging/well1/Data1",
            on_toggle=self._on_param_toggled,
            on_commit=self._auto_apply_if_enabled,
        )
        line += 1
        self.rows["datetime"] = ChoiceRow(
            right,
            line,
            "--datetime",
            ["on", "off"],
            "on",
            on_toggle=self._on_param_toggled,
            on_commit=self._auto_apply_if_enabled,
        )
        line += 1
        self.rows["no_preview"] = ChoiceRow(
            right,
            line,
            "-n no preview",
            ["on", "off"],
            "on",
            on_toggle=self._on_param_toggled,
            on_commit=self._auto_apply_if_enabled,
        )

        param_btns = ttk.Frame(right)
        param_btns.grid(row=line + 1, column=0, columnspan=2, sticky="ew", pady=(8, 0))
        ttk.Button(param_btns, text="Enable All Params", command=self._enable_all_params).pack(side="left")
        ttk.Button(param_btns, text="Disable All Params", command=self._disable_all_params).pack(side="left", padx=(8, 0))

        action = ttk.Frame(main)
        action.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(10, 0))
        action.columnconfigure(0, weight=1)

        self.auto_write_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(action, text="Auto write on edit", variable=self.auto_write_var).pack(side="left")
        ttk.Button(action, text="Apply To Selected Files", command=self.apply_changes).pack(side="right")

        self.status_var = tk.StringVar(value="Ready")
        ttk.Label(self, textvariable=self.status_var, anchor="w", padding=(10, 0, 10, 10)).pack(fill="x")

    def _load_files(self) -> None:
        self.file_list.delete(0, tk.END)
        for path in self.files:
            self.file_list.insert(tk.END, path.name)
        self.status_var.set(f"Found {len(self.files)} .sh files")

    def _refresh_files(self) -> None:
        self.files = sorted(self.base_dir.glob(SCRIPT_PATTERN))
        self._load_files()

    def _set_folder_from_entry(self) -> None:
        target = Path(self.target_dir_var.get().strip()).expanduser()
        if not target.is_dir():
            messagebox.showerror("Invalid folder", f"Folder not found:\n{target}")
            return
        self.base_dir = target
        self._refresh_files()

    def _browse_folder(self) -> None:
        chosen = filedialog.askdirectory(initialdir=str(self.base_dir))
        if not chosen:
            return
        self.target_dir_var.set(chosen)
        self._set_folder_from_entry()

    def _use_script_folder(self) -> None:
        self.base_dir = self.script_dir
        self.target_dir_var.set(str(self.script_dir))
        self._refresh_files()

    def _select_all(self) -> None:
        self.file_list.selection_set(0, tk.END)

    def _clear_selection(self) -> None:
        self.file_list.selection_clear(0, tk.END)

    def _enable_all_params(self) -> None:
        for row in self.rows.values():
            row.enabled_var.set(True)
        self._auto_apply_if_enabled()

    def _disable_all_params(self) -> None:
        for row in self.rows.values():
            row.enabled_var.set(False)

    def _on_param_toggled(self) -> None:
        self._auto_apply_if_enabled()

    def _auto_apply_if_enabled(self) -> None:
        if self.auto_write_var.get():
            self.apply_changes(show_dialog=False)

    def _collect_changes(self) -> dict[str, object]:
        changes: dict[str, object] = {}
        for key, row in self.rows.items():
            enabled = row.enabled_var.get()
            if not enabled:
                continue

            value = row.value_var.get().strip()
            if key in {"datetime", "no_preview"}:
                changes[key] = value.lower() == "on"
            else:
                if value == "":
                    raise ValueError(f"Value for {key} is empty")
                changes[key] = value
        return changes

    def _selected_paths(self) -> list[Path]:
        indexes = self.file_list.curselection()
        return [self.files[i] for i in indexes]

    def apply_changes(self, show_dialog: bool = True, use_all_files: bool = False) -> None:
        selected = self.files if use_all_files else self._selected_paths()
        if not selected:
            if show_dialog:
                messagebox.showwarning("No selection", "Select at least one .sh file.")
            else:
                self.status_var.set("No file selection for auto write")
            return

        try:
            changes = self._collect_changes()
        except ValueError as exc:
            if show_dialog:
                messagebox.showerror("Invalid input", str(exc))
            else:
                self.status_var.set(f"Invalid input: {exc}")
            return

        if not changes:
            if show_dialog:
                messagebox.showwarning("No parameters", "Enable at least one parameter to edit.")
            else:
                self.status_var.set("No enabled parameters")
            return

        updated_count = 0
        unchanged_count = 0
        missing_line_count = 0

        for path in selected:
            content = path.read_text(encoding="utf-8")
            lines = content.splitlines()

            command_index = None
            for i, line in enumerate(lines):
                if line.strip().startswith("libcamera-still"):
                    command_index = i
                    break

            if command_index is None:
                missing_line_count += 1
                continue

            old_line = lines[command_index].strip()
            new_line = update_command_line(old_line, changes)

            if old_line == new_line:
                unchanged_count += 1
                continue

            lines[command_index] = new_line
            path.write_text("\n".join(lines) + "\n", encoding="utf-8")
            updated_count += 1

        self.status_var.set(
            f"Updated: {updated_count}, unchanged: {unchanged_count}, no libcamera line: {missing_line_count}"
        )
        if show_dialog:
            messagebox.showinfo(
                "Done",
                (
                    f"Updated: {updated_count}\n"
                    f"Unchanged: {unchanged_count}\n"
                    f"No libcamera-still line: {missing_line_count}"
                ),
            )

    def apply_changes_all_files(self) -> None:
        self.apply_changes(show_dialog=True, use_all_files=True)


def main() -> None:
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
