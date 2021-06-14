# TNDR: Table Net Detection and Recognition Dataset
[![PWC](https://img.shields.io/badge/PyTorch-v1.8-blue)](https://pytorch.org/)
[![PWC](https://img.shields.io/badge/%20mmdetection%20-v2.10-blue)](https://github.com/open-mmlab/mmdetection)


> **TNDR: Table Net Detection and Recognition Dataset**<br>
> [Abdelrahman Abdallah](https://github.com/abdoelsayed2016),
> [Alexander Berendeev](),
> [Islam Nuradin](),
> [Daniyar Nurseitov](),
> <br>


## Abstract 
We present TNDR, a new real table image collected from free open source websites. TNDR dataset competition is structured into three tasks, first Task A is a task for table detection from documents, second Task B is a task for detecting table structure in cell recognition, and last Task C for classification table in 5 different classes. TNDR contains 9428 high-quality labeled tables. <br><br> In this paper, we have implemented state-of-the-art deep learning-based methods for table detection to create several strong baselines. HRNets Cascade Mask R-CNN with HRNetV2p-W18 Backbone Network achieves the highest performance compare with other methods with a precision of 81.0\%, recall of 90.3\%, and f1 score of 90.3\% on the TNDR dataset. We've made TNDR open source in the hopes of encouraging more deep learning approaches to table detection, structure recognition, and classification.
## Getting Started
### Install MMDetection v2.10.0+
TNDR has been implemented and tested with Python 3.7 and PyTorch 1.8.1. 
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

##  Benchmarking

##  Models Zoo

#### 1. Cascade Mask R-CNN

<table>
  <tr>
   <th>Backbones</th><th>Config Files</th><th>Checkpoint File</th>
  </tr>
  <tr>
   <td>  Resnet-50_1x </td> <td> <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
  <tr>
    <td> Resnet-50_20e </td>  <td>  <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
   <tr>
    <td> Resnet-101_1x </td>  <td>  <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
   <tr>
    <td> Resnet-101_20e </td>  <td>  <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
   <tr>
   <td> ResNeXt-101-32x4d_1x </td>   <td>  <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
   <tr>
    <td> ResNeXt-101-64x4d_1x </td>  <td>  <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
</table>

#### 2. Cascade R-CNN

<table>
  <tr>
   <th>Backbones</th><th>Config Files</th><th>Checkpoint File</th>
  </tr>
  <tr>
   <td>  Resnet-50_1x </td> <td> <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
  <tr>
    <td> Resnet-50_20e </td>  <td>  <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
   <tr>
    <td> Resnet-101_1x </td>  <td>  <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
   <tr>
    <td> Resnet-101_20e </td>  <td>  <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
   <tr>
   <td> ResNeXt-101-32x4d_1x </td>   <td>  <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
   <tr>
    <td> ResNeXt-101-64x4d_1x </td>  <td>  <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
</table>

#### 3. Faster R-CNN
<table>
  <tr>
   <th>Backbones</th><th>Config Files</th><th>Checkpoint File</th>
  </tr>
  <tr>
   <td>  Resnet-50_L1Loss </td> <td> <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
  <tr>
    <td> Resnet-50_1x </td>  <td>  <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
   <tr>
    <td> Resnet-101_1x </td>  <td>  <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
   <tr>
   <td> ResNeXt-101-32x4d_1x </td>   <td>  <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
   <tr>
    <td> ResNeXt-101-64x4d_1x </td>  <td>  <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
</table>

#### 4. Mask R-CNN
<table>
  <tr>
   <th>Backbones</th><th>Config Files</th><th>Checkpoint File</th>
  </tr>
  <tr>
   <td>  Resnet-50_1x </td> <td> <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
   <tr>
    <td> Resnet-101_1x </td>  <td>  <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
   <tr>
   <td> ResNeXt-101-32x4d_1x </td>   <td>  <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
   <tr>
    <td> ResNeXt-101-64x4d_1x </td>  <td>  <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
</table>


#### 5. Cascade RPN
<table>
  <tr>
    <th>Method</th> <th>Backbones</th><th>Config Files</th><th>Checkpoint File</th>
  </tr>
  <tr>
   <th>Fast R-CNN </th> <td>  Resnet-50_1x </td> <td> <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
   <tr>
    <th>CRPN </th> <td> Resnet-50_1x </td>  <td>  <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
  
</table>


#### 6. Hybrid Task Cascade
<table>
  <tr>
   <th>Backbones</th><th>Config Files</th><th>Checkpoint File</th>
  </tr>
  <tr>
   <td>  Resnet-50_1x </td> <td> <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
   <tr>
    <td> Resnet-50_20e </td>  <td>  <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
   <tr>
   <td> Resnet-101_1x </td>   <td>  <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
   
</table>


#### 7. HRNets
##### 7.1 Cascade R-CNN
<table>
  <tr>
   <th>Backbones</th><th>Config Files</th><th>Checkpoint File</th>
  </tr>
  <tr>
   <td>  HRNetV2p-W18_20e </td> <td> <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
   <tr>
    <td> HRNetV2p-W32_20e </td>  <td>  <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
   <tr>
   <td> HRNetV2p-W40_20e </td>   <td>  <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
   
</table>

##### 7.2 Faster R-CNN
<table>
  <tr>
   <th>Backbones</th><th>Config Files</th><th>Checkpoint File</th>
  </tr>
  <tr>
   <td>  HRNetV2p-W18_1x </td> <td> <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
  <tr>
   <td>  HRNetV2p-W18_2x </td> <td> <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
   <tr>
    <td> HRNetV2p-W32_1x </td>  <td>  <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
     <tr>
    <td> HRNetV2p-W32_2x </td>  <td>  <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
   <tr>
   <td> HRNetV2p-W40_1x </td>   <td>  <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
    <tr>
   <td> HRNetV2p-W40_2x </td>   <td>  <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
</table>

##### 7.3 HTC 
<table>
  <tr>
   <th>Backbones</th><th>Config Files</th><th>Checkpoint File</th>
  </tr>
  <tr>
   <td>  HRNetV2p-W18_20e </td> <td> <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>

   <tr>
    <td> HRNetV2p-W32_20e </td>  <td>  <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>

</table>

##### 7.4 Mask R-CNN
<table>
  <tr>
   <th>Backbones</th><th>Config Files</th><th>Checkpoint File</th>
  </tr>
  <tr>
   <td>  HRNetV2p-W18_1x </td> <td> <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>

   <tr>
    <td> HRNetV2p-W32_1x </td>  <td>  <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>

</table>

 
 ##### 7.5 Cascade Mask R-CNN
<table>
  <tr>
   <th>Backbones</th><th>Config Files</th><th>Checkpoint File</th>
  </tr>
  <tr>
   <td>  HRNetV2p-W18_20e </td> <td> <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>

</table>

 ##### 7.6 FCOS
<table>
  <tr>
   <th>Backbones</th><th>Config Files</th><th>Checkpoint File</th>
  </tr>
  <tr>
   <td> HRNetV2p-W18_1x </td> <td> <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
  <tr>
   <td>  HRNetV2p-W18_2x </td> <td> <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
  
  <tr>
   <td> HRNetV2p-W32_1x </td> <td> <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
</table>


#### 8. ResNeSt
##### 8.1 Cascade R-CNN
<table>
  <tr>
   <th>Backbones</th><th>Config Files</th><th>Checkpoint File</th>
  </tr>
  <tr>
   <td> S-50 </td> <td> <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
  <tr>
   <td>   S-101 </td> <td> <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
  
</table>

##### 8.2 Faster R-CNN
<table>
  <tr>
   <th>Backbones</th><th>Config Files</th><th>Checkpoint File</th>
  </tr>
  <tr>
   <td> S-50 </td> <td> <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
  <tr>
   <td>   S-101 </td> <td> <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
  
</table>

#### 9. YOLO

<table>
  <tr>
   <th>Backbones</th><th>Config Files</th><th>Checkpoint File</th>
  </tr>
  <tr>
   <td> DarkNet-53_320 </td> <td> <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
  <tr>
   <td>   DarkNet-53_416  </td> <td> <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
   <tr>
   <td>   DarkNet-53_608  </td> <td> <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
</table>


#### 10. Dynamic RCNN

<table>
  <tr>
   <th>Backbones</th><th>Config Files</th><th>Checkpoint File</th>
  </tr>
  <tr>
   <td> Resnet-50_1X </td> <td> <a href="">Config Files</a> </td> <td> <a href="">Checkpoint</a> </td>
  </tr>
</table>


## License
The code of CascadeTabNet is Open Source under the [MIT License](LICENSE). There is no limitation for both acadmic and commercial usage.

## Cite as
If you find this work useful for your research, please cite our paper:
```
```




