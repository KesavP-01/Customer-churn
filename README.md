
# Customer Churn Prediction using Neural Networks

## Overview

This repository contains a neural network model built with TensorFlow and Keras for predicting customer churn. The model processes customer data, learns patterns, and classifies customers as likely to churn or not. It achieves a robust accuracy of **86.3%** on the test data. The dataset used for training and evaluation is located in the `data` folder.

## Features

- Preprocessing of customer data, including feature scaling and categorical encoding.
- Sequential neural network model with dense layers and ReLU activations.
- Model training using binary cross-entropy loss and Adam optimizer.
- Model evaluation via accuracy and confusion matrix metrics.

## Project Structure

```plaintext
Customer-churn-main/
│
├── data/                   # Contains the customer churn dataset (Churn.csv)
├── models/                 # Folder for saving trained models
├── scripts/                # Python scripts for training and evaluating the model
├── churnModel.egg-info/    # Package information
├── setup.py                # Setup file for project dependencies and installation
├── LICENSE                 # Project license
└── README.md               # Project documentation
```
## Installation
**Clone the repository:**

```
git clone https://github.com/KesavP-01/Customer-churn.git
```
**Navigate to the project directory:**
```
cd Customer-churn-main
```
**Install the required dependencies:**
```
pip install -r requirements.txt
```
## Usage
Ensure the dataset Churn.csv is available in the data folder.

**Run the Python script to train the model:**
```
python scripts/neural_network_churn.py
```

## Results

The neural network achieved an accuracy of **86.3%** on the test data. The confusion matrix highlights the model's performance across different classes, demonstrating its effectiveness in predicting customer churn.
