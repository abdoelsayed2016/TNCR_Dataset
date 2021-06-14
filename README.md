# TNDR: Table Net Detection and Recognition Dataset
## Abstract 
 
## Getting Started
### Install MMDetection v2.10.0+
TNDC has been implemented and tested with Python 3.7 and PyTorch 1.8.1. 
```
%cd $project_dir$
!pip install -q mmcv terminaltables
!git clone 'https://github.com/open-mmlab/mmdetection.git'
!pip install -r "$project_dir$/mmdetection/requirements/optional.txt"
%cd mmdetection/
!python setup.py install
!python setup.py develop
!pip install -r {"$project_dir$/mmdetection/requirements.txt"}
!pip install pillow
!pip install mmcv
!pip install mmcv-full
%cd ..
!pip uninstall pycocotools
!pip uninstall mmpycocotools
!pip install mmpycocotools
```











## requirements
```
Python: 3.7 
PyTorch: 1.8.1
OpenCV: 4.5.2
MMCV: 1.3.5
MMDetection: v2.10.0
```
## License
The code of CascadeTabNet is Open Source under the [MIT License](LICENSE). There is no limitation for both acadmic and commercial usage.

## Cite as
If you find this work useful for your research, please cite our paper:
```
```




