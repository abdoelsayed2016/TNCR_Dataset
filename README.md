# TNDC: Table Net Detection and Classification
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

## Data Prepration 
data
   └── TNDC Dataset
       ├── Annotations
       │   ├── 0.xml
       │   ├── ...
       │   └── 9.xml
       ├── ImageSets
       │   └── Main
       │       ├── test.txt
       │       └── trainval.txt
       └── Images
           ├── 0.jpg
           ├── ...
           └── 9.jpg
## requirements

## Cite as
If you find this work useful for your research, please cite our paper:
```
```
