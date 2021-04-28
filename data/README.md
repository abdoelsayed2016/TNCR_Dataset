

# Data Prepration 
You should convert your Pascal VOC XML annotation files to a single COCO Json file so we can train our models.
The Raw folder for the data should be like below, then used generateVOC2JSON.py

    .
    │   ├── data
    │   │   ├── TNDC Dataset
    │   │   │  ├── Annotations
    │   │   │  │    ├── 000ad0bb60e1ec4176713693a41f2115.xml
    │   │   │  │    ├── ...
    │   │   │  │    ├── ffda050fe78074f78b874540ad218fb9.xml
    │   │   │  ├── ImageSets
    │   │   │  │    ├── Main 
    │   │   │  │    │     ├── test.txt
    │   │   │  │    │     ├── train.txt
    │   │   │  │    │     ├── val.txt
    │   │   │  ├── Images
    │   │   │  │    ├── 000ad0bb60e1ec4176713693a41f2115.jpg
    │   │   │  │    ├── ...
    │   │   │  │    ├── ffda050fe78074f78b874540ad218fb9.jpg
    │   │   │  ├── Output Json
    │   │   ├── generateVOC2JSON.py   




