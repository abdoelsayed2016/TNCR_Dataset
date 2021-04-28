## Script for Converting Pascal VOC annotations to Coco Json format
## This script shows and example conversion of our table dataset pascal voc
## annotations conversion to coco annotations  

import os
import xml.etree.ElementTree as ET
import xmltodict
import json
from xml.dom import minidom
from collections import OrderedDict
import cv2

def generateVOC2Json(rootDir,xmlFiles):
  attrDict = dict()
  # Add categories according to you Pascal VOC annotations
  attrDict["categories"]=[{"supercategory":"none","id":1,"name":"full_lined"},
                          {"supercategory":"none","id":2,"name":"merged_cells"},
                          {"supercategory":"none","id":3,"name":"nolines"},
                          {"supercategory":"none","id":4,"name":"partial_lined"},
                          {"supercategory":"none","id":5,"name":"partial_lined_merged_cells"}
        
            ]
  images = list()
  annotations = list()
  id1 = 1

  # Some random variables
  full_lined = 0
  merged_cells = 0
  nolines = 0
  partial_lined=0
  partial_lined_merged_cells=0  
  # Main execution loop
  for root, dirs, files in os.walk(rootDir):
    image_id = 0
    for file in xmlFiles:
      image_id = image_id + 1
      if file in files:
        annotation_path = os.path.abspath(os.path.join(root, file))
        image = dict()
        doc = xmltodict.parse(open(annotation_path,encoding='utf-8').read())
        image['file_name'] = str(doc['annotation']['filename'])
        print(image['file_name'])
       
        img = cv2.imread("./data/TNDC Dataset/JPEGImages/"+image['file_name'])
       
        
        height, width, channels = img.shape
        
        image['height'] = int(height)#int(doc['annotation']['size']['height'])
        image['width'] = int(width)#int(doc['annotation']['size']['width'])
        image['id'] = image_id
        print("File Name: {} and image_id {}".format(file, image_id))
        images.append(image)
        if 'object' in doc['annotation']:
          for key,vals in doc['annotation'].items():
            if(key=='object'):
              for value in attrDict["categories"]:
                if(not isinstance(vals, list)):
                  vals = [vals]
                for val in vals:
                  if str(val['name']) == value["name"]:
                    annotation = dict()
                    annotation["iscrowd"] = 0
                    annotation["image_id"] = image_id
                    x1 = int(val["bndbox"]["xmin"])  - 1
                    y1 = int(val["bndbox"]["ymin"]) - 1
                    x2 = int(val["bndbox"]["xmax"]) - x1
                    y2 = int(val["bndbox"]["ymax"]) - y1
                    annotation["bbox"] = [x1, y1, x2, y2]
                    annotation["area"] = float(x2 * y2)
                    annotation["category_id"] = value["id"]

                    # Tracking the count
                    if(value["id"] == 1):
                      full_lined += 1
                    if(value["id"] == 2):
                      merged_cells += 1
                    if(value["id"] == 3):
                      nolines += 1
                    if(value["id"] == 4):
                      partial_lined += 1
                    if(value["id"] == 5):
                      partial_lined_merged_cells += 1

                    annotation["ignore"] = 0
                    annotation["id"] = id1
                    annotation["segmentation"] = [[x1,y1,x1,(y1 + y2), (x1 + x2), (y1 + y2), (x1 + x2), y1]]
                    id1 +=1
                    annotations.append(annotation)
        else:
          print("File: {} doesn't have any object".format(file))
      else:
        print("File: {} not found".format(file))

  attrDict["images"] = images	
  attrDict["annotations"] = annotations
  attrDict["type"] = "instances"

  # Printing out some statistics
  print(len(images))
  print("full_lined : ",full_lined," merged_cells : ",merged_cells," nolines : ",nolines," partial_lined : ",partial_lined)
  print(len(annotations))

  # Save the final JSON file
  # jsonString = json.dumps(attrDict)
  jsonString = json.dumps(attrDict, indent = 4, sort_keys=True)
  with open("./data/TNDC Dataset/Output Json/test.json", "w") as f:
    f.write(jsonString)

# Path to the txt file (see at the top of this script)
trainFile = "./data/TNDC Dataset/ImageSets/main/test.txt"
trainXMLFiles = list()
with open(trainFile, "r") as f:
	for line in f:
		fileName = line.strip()
		#print(fileName)
		trainXMLFiles.append(fileName + ".xml")

# Path to the pascal voc xml files 
rootDir = "./data/TNDC Dataset/Annotations"

# Start execution
generateVOC2Json(rootDir, trainXMLFiles)
