
# Neural Network for Churn Prediction

## Overview
This code implements a neural network using TensorFlow and Keras for predicting customer churn. The dataset used for training and evaluation is provided in the file Churn.csv.



## Usage
- Clone or download the repository containing the code.
- Ensure that Churn.csv is present in the same directory as the Python script.
- Run the Python script neural_network_churn.py.

## Description
### Preprocessing Phase:

- The dataset is loaded from Churn.csv.
- Features and labels are extracted.
- Categorical features are encoded using one-hot encoding.
- The dataset is split into training and testing sets.
- Features are standardized using standard scaling.
### Neural Network Initialization:

- A Sequential model is initialized.
- Dense layers with ReLU activation functions are added.
- The output layer uses a sigmoid activation function for binary classification.
- The model is compiled using binary cross-entropy loss and Adam optimizer.
- Training is performed on the training set with validation split and specified batch size and epochs.
### Predictions:

- Predictions are made on the test set.
- Thresholding is applied to convert probabilities to binary predictions.
- Confusion matrix and accuracy score are calculated for model evaluation.

## Results

- Achieved a accuracy of **93.6%** on the given data.
