# The codes and trained model for paper *"Color Image Restoration Exploiting Inter-channel Correlation with a 3-stage CNN"*

### K. Cui, A. Boev, E. Alshina and E. Steinbach, *Color Image Restoration Exploiting Inter-channel Correlation with a 3-stage CNN*, IEEE-JSTSP, 2020. DOI: [10.1109/JSTSP.2020.3043148](https://doi.org/10.1109/JSTSP.2020.3043148)

---
## Dependencies: 

- Python 3
- TensorFlow 1.XX (1.10 or newer)
- NumPy
- Pillow
- NVIDIA GPU + CUDA (if running in GPU mode)

## Dataset:

- You need to download the testing datasets to run the demo test for different tasks. We summarize the datasets [here](https://tumde-my.sharepoint.com/:f:/g/personal/kai_cui_tum_de/Elln4Vp3-AdBqCHtvuHe4VMB0tQdIV238QuTHMJjum0vYg?e=B2y4nR). Unzip the datasets and put them into the data folder. If you have your own dataset, please follow the [readme](./data/readme.md) in the data folder to organize the dataset.

## Usage:

1. There are three subtasks in our paper, color demosaicking (CDM), compression artifacts reduction (CAR), and real-world color image denoising (RIDN). The code and the trained models are in the corresponding folder.

2. For CDM, run `python main_py3_tfrecord.py` to test the Kodak dataset.  
When testing other datasets, simply add ` --test_set NAME`, e.g., `python main_py3_tfrecord.py --test_set McM`  
It also supports the ensemble testing mode, run `python main_py3_tfrecord.py --phase ensemble`

3. For CAR, run `python main_py3_tfrecord.py` to test the LIVE1 dataset with qp = 10.  
Use `--qp XX` to test different QPs, e.g., `python main_py3_tfrecord.py --qp 100` 

4. For RIDN, run `python main_py3_tfrecord.py` to test the SIDD_validation dataset.

5. The codes support both CPU and GPU mode. Default is *GPU 0*, use `--gpu -1` to run on CPU or choose other GPUs.

6. Please read our paper for more details!

7. Have fun!

---
## Citation:
Please cite our paper if you find the paper or the code is helpful for your research.

```
@ARTICLE{CNNCIR-JSTSP-2020,  
  author={K. {Cui} and A. {Boev} and E. {Alshina} and E. {Steinbach}},  
  journal={IEEE Journal of Selected Topics in Signal Processing},  
  title={Color Image Restoration Exploiting Inter-channel Correlation with a 3-stage {CNN}},   
  year={2020},  
  volume={},  
  number={},  
  pages={1-1},  
  doi={10.1109/JSTSP.2020.3043148}}
```

## Related Work

1. K. Cui, Z. Jin and E. Steinbach, *Color image demosaicking using a 3-stage convolutional neural network structure*, ICIP 2018. [[Paper]](https://doi.org/10.1109/ICIP.2018.8451020) [[Code]](https://github.com/amnesiack/ICIP2018CDM)
2. K. Cui and E. Steinbach, *Decoder Side Image Quality Enhancement exploiting Inter-channel Correlation in a 3-stage CNN: Submission to CLIC 2018*, CVPR Workshops 2018. [[Paper]](https://openaccess.thecvf.com/content_cvpr_2018_workshops/w50/html/Cui_Decoder_Side_Image_CVPR_2018_paper.html)
3. K. Cui and E. Steinbach, *Decoder Side Color Image Quality Enhancement using a Wavelet Transform based 3-stage Convolutional Neural Network*, CVPR Workshops 2019. [[Paper]](https://openaccess.thecvf.com/content_CVPRW_2019/html/CLIC_2019/Cui_Decoder_Side_Color_Image_Quality_Enhancement_using_a_Wavelet_Transform_CVPRW_2019_paper.html)

---
## Maintainer:

[@Kai Cui](https://github.com/amnesiack) (<kai.cui@tum.de>)  
Lehrstuhl fuer Medientechnik ([LMT](https://www.ei.tum.de/en/lmt/home/))  
Technische Universitaet Muenchen ([TUM](https://www.tum.de))  
Last modified 06.02.2021

---

## License
[![License](https://img.shields.io/badge/License-Apache%202.0-yellowgreen.svg)](https://opensource.org/licenses/Apache-2.0)  
This project is released under the Apache 2.0 license.
