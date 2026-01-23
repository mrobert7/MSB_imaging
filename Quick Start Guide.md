### Prerequisites

**Hardware Requirements:**
- Raspberry Pi (Model 4 recommended, 4GB+ RAM)
- Raspberry Pi Camera Module (HQ Camera or Camera Module v2)
- Stepper motors and drivers for automated positioning
- LEDs for fluorescence excitation (470nm for GFP, 525nm for mCherry)
- 3D printer access for custom components
- Basic electronic components (see detailed parts list)

**Software Requirements:**
- Raspberry Pi OS (Bullseye or newer)
- Python 3.7+
- ImageJ/Fiji for image analysis
- Git for repository access

### Quick Start Guide

1. **Clone this repository:**
   ```bash
   git clone https://github.com/mrobert7/MSB_imaging.git
   cd MSB_imaging
   ```

2. **3D print the components:**
   - Navigate to `3D_printed_parts_stl_file/`
   - Print all STL files using parameters in `3D_printer_parameter/`
   - Recommended: PLA filament

3. **Set up the Raspberry Pi:**
   - Follow instructions in `Setting up LOTUS/`
   - Install required Python packages
   - Configure camera and GPIO pins
   - Test motor controls

4. **Run your first experiment:**
   - Use scripts in `Experimental_script_imaging_operation/`
   - Start with basic brightfield imaging
   - Progress to fluorescence time-lapse experiments

5. **Analyze your data:**
   - Import images into ImageJ
   - Use macros from `Analysis_imageJ/`
   - Process time-series data
