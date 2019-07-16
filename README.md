# Real-time object detection with YOLOv3 in urban street scenes

## Introduction

Alongside accuracy and recall, computational cost is the most important perfor-mance criterion to be optimized in object detection because many applications de-mand real-time detection.

The development of predicting bounding boxes for object detection started with the sliding window approach, which, while predicting appropriate bounding boxes, is very computationally expensive. Later models use selective search (in RCNNs) or region proposal networks (in Faster-RCNNs) —vastly reduced computational cost. YOLO and its derivatives, YOLO9000 and YOLOv3, offer state-of-the art prediction accuracy and leading real-time performance (frames per second). In this project we explore the performance of the YOLOv3 model for detecting objects in street scenes.

## Motivation—Why should we detect objects (in street scenes)?

Object detection has a variety of applications, with the most popular being: trans-portation (e.g. autonomous driving), consumer electronics (e.g. face-detection in smart-phones), surveillance (e.g. face-detection in shop surveillance cameras).Street scenes are interesting subjects for object detection since they present multi-ple classes and varying conditions in lighting, landscape, surroundings, weather and season of year.

## Data set

![Example image from the Berkeley Deep Drive data set][images/example.jpg]

2D Bounding boxes annotated on 100.000 images for bus, traffic light, traffic sign, person, bike, truck, motor, car, train and rider.

Berkeley Deep Drive data-set contains urban street scenes captured by dashboard cameras in cars. The data-set contains images for day and night scenes and varying weather conditions. Furthermore, different cameras have been used to capture the footage, resulting in varying image quality.

Setup
- 70% of data used for training
- 10% of data used for validation
- 20% of data used for testing

Hardware
- Nvidia Tesla K80 - 11GB of VRAM
- 4 Virtual CPUs
- 15 GB ddr4 -RAM

## Predicting Bounding Boxes - You only look once

The idea behind YOLO is to simultaneously predict multiple possible bounding boxes, the confidence for the box that it contains an object and the class probabilities in a single network.

![From the image to predictions][images/prediction.jpg]


Steps of predicting Anchor Boxes:
1. Divide Image into grid of S x S at some output within the CNN
2. Fully convolutional Layers ( [ 1 x 1 ] - Kernel): each cell predicts B anchor boxes and corresponding class prob-abilities as well as an objectiveness score
3. Output is S x S x B x (5 + C) Tensor
4. Repeat prediction on 2 more scales to predict small and big objects

## CNN Architecture

| Architecture 	| Top - 1 	| Top - 5 	| FPS 	|
|--------------	|---------	|---------	|-----	|
| Darknet - 19 	| 74.1    	| 91.8    	| 171 	|
| ResNet - 101 	| 77.1    	| 93.7    	| 53  	|
| ResNet - 152 	| 77.6    	| 93.8    	| 37  	|
| DarkNet - 53 	| 77.2    	| 93.8    	| 78  	|

## Results and Evaluation
