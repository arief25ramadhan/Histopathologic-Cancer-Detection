# Histopathologic-Cancer-Detection

## Short Description

Identify metastatic tissue in histopathologic scans of lymph node sections.

## Aim

This project aims to classify and label pathology images. 

## Dataset

The pathology images can be downloaded from this link: 

https://www.kaggle.com/c/histopathologic-cancer-detection/data

The dataset contains of 220025 images; 60% of them are from normal patients, and 40% contains tumor pixel. Each image is colored with size of 96x96 pixel. Tumor tissue in the outer region of the patch does not influence the label. This outer region is provided to enable fully-convolutional models that do not use zero-padding, to ensure consistent behavior when applied to a whole-slide image.

## GPU

To train the network with a GPU, follow this tutorial:

https://www.youtube.com/watch?v=tPq6NIboLSc

## Libraries

The libraries required for this project are:

* Numpy
* Panda
* Tensorflow
* Keras
* Scikit Learn
* Matplotlib

## Files

There are two jupyter notebook files in this repository. It is important to go to the first file (1_data_explore.ipynb) before the second one (2_model.ipynb). The description of each file is:

* 1_data_explore.ipynb: explore dataset, crop images, split data into training and validation set
* 2_model.ipynb: build, train, plot, and test model


## Sources

Informations and links in this README.md file is heavily based on this webpage from Kaggle:

https://www.kaggle.com/c/histopathologic-cancer-detection/

The project's codes are built and modified from this repositories: 

https://github.com/gsurma/histopathologic_cancer_detector

https://github.com/Terrance-Whitehurst/Keras-Histopathologic-Cancer-Detection

https://github.com/darien-schettler/histopathologic-cancer-detection
