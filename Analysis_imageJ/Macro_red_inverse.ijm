// ▼関数：Redチャネルを自動で取得して選択（split + red抽出）
function selectRedChannel(imagePath) {
    open(imagePath);
    run("Split Channels");
    titles = getList("image.titles");
    for (k = 0; k < titles.length; k++) {
        if (indexOf(titles[k], "(red)") != -1) {
            selectWindow(titles[k]);
            return titles[k];
        }
    }
    exit("Error: Red channel not found.");
}

// ▼フォルダ選択
dir1 = getDirectory("Choose Source Directory (with all images including reference)");
saveDir = getDirectory("Choose Destination Directory to save normalized images");
roiApplyDir = getDirectory("Choose folder of images to apply ROI");

// ▼ファイル名設定
normalizedResultPath = saveDir + "normalized_measurements.csv";
roiAppliedResultPath = saveDir + "roi_applied_measurements.csv";
roiZipPath = saveDir + "roi_all.zip";

// ▼初期化
list1 = getFileList(dir1);
list2 = getFileList(roiApplyDir);
setBatchMode(true);
roiManager("reset");
run("Clear Results");

// ▼基準画像（list1[0]）のRedチャネルを取得・処理
refPath = dir1 + list1[0];
refRedTitle = selectRedChannel(refPath);
rename("Reference");
run("8-bit");
run("Invert");

// ▼対象画像群の処理（Splitあり）
for (i = 1; i < list1.length; i++) {
    showProgress(i, list1.length - 1);

    targetPath = dir1 + list1[i];
    tgtRedTitle = selectRedChannel(targetPath);
    rename("Target_" + i);
    run("8-bit");
    run("Invert");

    imageCalculator("Subtract create", "Target_" + i, "Reference");

    selectWindow("Result of Target_" + i);

    // ROI生成範囲（例：well1）
    makeRectangle(758, 278, 498, 472);
    run("Crop");

    setAutoThreshold("Otsu dark no-reset");
    run("Create Selection");
    run("Make Inverse");
    run("Measure");
    roiManager("Add");

    saveAs("Results", normalizedResultPath);
    //saveAs("Tiff", saveDir + "normalized_" + list1[i]);

    close(); // cropped image
    close("Target_" + i);
}
close("Reference");
run("Clear Results");

// ▼ROIをまとめて保存
roiManager("Deselect");
roiManager("Save", roiZipPath);

// ▼ROI適用と再測定（Splitしない）
roiCount = roiManager("count");
imageCount = list2.length;

for (j = 0; j < imageCount; j++) {
    open(roiApplyDir + list2[j]);  // ← split しない
    rename("ApplyTarget_" + j);
    run("8-bit");

    makeRectangle(758, 278, 498, 472);
    run("Crop");

    if (j < roiCount) {
        roiManager("Select", j);
        run("Measure");
    } else {
        print("警告：画像 " + j + " に対応する ROI が存在しません");
    }

    close(); // cropped image
}

// ▼測定結果を保存
saveAs("Results", roiAppliedResultPath);
run("Clear Results");
setBatchMode(false);
