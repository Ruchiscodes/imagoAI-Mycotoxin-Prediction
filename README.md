# Hyperspectral Imaging Mycotoxin Prediction

## Overview
This repository contains code and documentation for predicting mycotoxin levels in corn samples using hyperspectral imaging and deep learning techniques.

## Repository Structure
```
|-- notebook.ipynb       # Jupyter Notebook for data preprocessing, model training, and evaluation
|-- script.py            # Python script for interactive predictions using Streamlit
|-- report.md            # Project report covering methodology and findings
|-- README.md            # Setup instructions and repository overview
|-- cnn_model.h5         # Trained CNN model
|-- requirements.txt     # Dependencies required to run the project
```

## Installation
### 1. Clone the Repository
```
git clone <repository-url>
cd <repository-name>
```

### 2. Create a Virtual Environment (Recommended)
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

## Running the Project
### 1. Running the Jupyter Notebook
```
jupyter notebook notebook.ipynb
```

### 2. Running the Streamlit App
```
streamlit run script.py
```

## Dataset
- The model expects **CSV files** with **448 spectral features**.
- Ensure that the dataset is preprocessed before prediction.

