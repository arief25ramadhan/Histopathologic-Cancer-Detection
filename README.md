# Histopathologic-Cancer-Detection

## Short Description

Identify metastatic tissue in histopathologic scans of lymph node sections.

## Aim

This project aims to classify and label pathology images. 

## Dataset

The pathology images can be downloaded from this link: 

https://www.kaggle.com/c/histopathologic-cancer-detection/data

Files are named with an image id. The train_labels.csv file provides the ground truth for the images in the train folder. The model predict the labels for the images in the test folder. A positive label indicates that the center 32x32px region of a patch contains at least one pixel of tumor tissue. 

Tumor tissue in the outer region of the patch does not influence the label. This outer region is provided to enable fully-convolutional models that do not use zero-padding, to ensure consistent behavior when applied to a whole-slide image.

## Libraries

The libraries required for this project are:

* Numpy
* Panda
* Pytorch

## Sources

Informations and links in this README.md file is heavily based on this webpage from Kaggle:

https://www.kaggle.com/c/histopathologic-cancer-detection/

The project's codes are built and modified from the Udacity Plagiarism Detector's initial code, as provided in this repository: 

https://github.com/udacity/ML_SageMaker_Studies
 
