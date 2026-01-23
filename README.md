# LOTUS: A low-cost time-lapse automated imaging system for spatio-temporal analysis of microbial colony or biofilm development

[![DOI](https://img.shields.io/badge/DOI-10.1371/journal.pone.0339652-blue)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0339652)

## Overview

LOTUS is an open-source automated biofilm imaging platform built using Raspberry Pi, 3D-printed components, and motorized sample positioning. This repository contains all necessary files, scripts, and documentation to build and operate your own LOTUS system for macro-scale bacterial biofilm research.

Published in: *PLOS ONE* - Sakai et al. (2026)

LOTUS provides a cost-effective alternative to expensive commercial imaging systems while maintaining sufficient capability for spatio-temporal analysis of bacterial biofilm development and gene expression dynamics. The system is designed for:

- **Biofilm heterogeneity studies** - Track spatial and temporal patterns in biofilm development
- **Fluorescence reporter imaging** - Monitor gene expression using GFP, mCherry, and other fluorescent proteins
- **Multimode imaging** - Brightfield, transparency (biomass proxy), and fluorescence dual-reporter experiments
- **Time-lapse studies** - Automated long-term imaging with minimal user intervention
- **Educational applications** - Accessible platform for teaching microbiology and bioengineering

## Key Features

- **Low-cost construction:** Build for a fraction of commercial system costs
- **Automated sample positioning:** Motorized stage for multi-sample experiments
- **Fluorescence imaging:** Optimized for common fluorescent reporters (GFP, mCherry)
- **Open-source design:** All hardware designs, software, and analysis tools freely available
- **Validated performance:** Peer-reviewed characterization of sensitivity SNR, channel cross-talk, and phototoxicity
- **Flexible and modular:** Customize for your specific research needs

## Repository Contents

### 📁 [3D_printed_parts_stl_file](./3D_printed_parts_stl_file)
STL files for all custom 3D-printed components including:
- Sample stage
- Camera mounts
- LED housing
- Motorized positioning components

### 📁 [3D_printer_parameter](./3D_printer_parameter)
Recommended printing parameters and settings for optimal part quality and functionality.

### 📁 [Setting up LOTUS](./Setting%20up%20LOTUS)
Complete setup documentation including:
- Hardware assembly instructions
- Raspberry Pi configuration
- Software installation
- System calibration procedures

### 📁 [Experimental_script_imaging_operation](./Experimental_script_imaging_operation)
Python scripts for:
- Automated image acquisition
- Time-lapse control
- Multi-sample positioning
- Fluorescence excitation control

### 📁 [Image_Analysis](./Analysis_imageJ)
ImageJ macros and workflows for:
- Image preprocessing
- Biofilm biomass quantification
- Fluorescence intensity analysis
- Time-series data processing

### 📁 [Supervisor](./Supervisor)
System monitoring and management tools:
- Process supervision
- Automated restart functionality
- Error logging and recovery

### 📁 [Supplementary material_video](./Supplementary%20material_video)
Demonstration videos showing:
- System operation
- Biofilm time-lapse examples
- Setup procedures


## System Capabilities

### Validated Performance Metrics

- **Detection sensitivity:** Quantitative detection of fluorescent reporter expression
- **Temporal resolution:** Configurable image acquisition intervals (minutes to hours)
- **Spatial coverage:** Multiple biofilm colonies per experiment
- **Photobleaching characterization:** Minimal signal degradation over extended imaging
- **Signal-to-noise ratio:** Sufficient for semi-quantitative gene expression analysis
- **Channel cross-talk:** Validated for dual-reporter experiments (GFP/mCherry)
- **Phototoxicity assessment:** Safe for bacterial biofilm viability


## Citation

If you use LOTUS in your research, please cite:

> Sakai, M., et al. (2026). LOTUS: A low-cost open-source automated biofilm imaging system for spatio-temporal analysis of bacterial gene expression. *PLOS ONE*. DOI: [10.1371/journal.pone.0339652](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0339652)

## Comparison to Commercial Systems

| Feature | LOTUS | Commercial Systems |
|---------|-------|-------------------|
| Cost | < $550 | $10,000 - $100,000+ |
| Application | Macro-scale screening | Single-cell to macro |
| Resolution | Semi-quantitative | High-resolution quantitative |
| Throughput | Multi-sample (configurable) | Varies |
| Customization | Fully open-source | Limited |
| Best for | Budget-conscious labs, experimenting, education, screening | Detailed mechanistic studies |

LOTUS is designed to **complement** rather than replace commercial systems, providing an accessible entry point for biofilm research.

## Contributing

We welcome contributions from the community! Please consider:

- Reporting bugs or issues
- Suggesting enhancements
- Sharing your modifications or improvements
- Contributing analysis tools or scripts
- Documenting your experiences

Please open an issue or submit a pull request on GitHub.

## Support and Contact

- **Issues:** Use GitHub Issues for bug reports and technical questions
- **Discussions:** Share your experiences and ask questions in GitHub Discussions
- **Email:** [robert.martin.4m@kyoto-u.ac.jp]

## License

You are free to:
- Use LOTUS for academic or commercial purposes
- Modify and distribute the design
- Build upon this work

We only ask that you:
- Provide attribution (cite our paper)
- Share improvements with the community

## Acknowledgments

We thank the open-source hardware community for inspiration and the microbiology research community for valuable feedback during development.

Special thanks to:
- PLOS ONE reviewers for thorough feedback that improved the system
- Colleagues and MSB lab beta testers at Kyoto University who provided validation data
- The Raspberry Pi Foundation for accessible computing platforms

## Additional Resources

- **PLOS ONE publication:** [Link to paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0339652)
- **Supplementary Information:** Detailed validation protocols and additional data
- **Video demonstrations:** See `Supplementary material_video/`
- **Community forum:** [TBA]

---

**LOTUS** - Making biofilm research accessible to all laboratories, regardless of budget.

For questions, collaborations, or to share your LOTUS builds, please reach out!



