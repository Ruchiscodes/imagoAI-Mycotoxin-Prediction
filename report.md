# Hyperspectral Imaging for Mycotoxin Prediction

## 1. Introduction
This project uses hyperspectral imaging data to predict mycotoxin levels in corn samples. The goal is to preprocess the spectral data, reduce dimensionality, train a model, and evaluate its performance.

## 2. Data Preprocessing
### 2.1 Handling Missing Values
- Checked for missing values and handled them appropriately.
- Dropped non-numeric columns to ensure consistency.

### 2.2 Feature Scaling
- Standardized spectral data to have a mean of 0 and variance of 1 using `StandardScaler`.

## 3. Dimensionality Reduction
### 3.1 Principal Component Analysis (PCA)
- Applied PCA to reduce redundant information and improve computational efficiency.
- Selected principal components explaining **95% variance**.

## 4. Model Training
### 4.1 Convolutional Neural Network (CNN)
- Designed a CNN to learn spectral patterns and predict mycotoxin levels.
- Input shape: **(448, 1)** corresponding to spectral features.
- Output: Regression value representing mycotoxin level.

### 4.2 Training & Hyperparameters
- Optimizer: Adam
- Loss function: Mean Squared Error (MSE)
- Number of epochs: **50**
- Batch size: **32**

## 5. Model Evaluation
### 5.1 Metrics
- **Mean Absolute Error (MAE)**: Measures average prediction error.
- **R² Score**: Evaluates model performance.

### 5.2 Results
| Metric  | Value  |
|---------|--------|
| MAE     | X.XX   |
| R² Score | X.XX   |

## 6. Key Findings & Future Improvements
- The CNN performed well but can be improved with more training data.
- Feature selection methods beyond PCA, like Autoencoders, can be explored.
- Data augmentation techniques may enhance generalization.

## 7. Conclusion
This project successfully demonstrates the application of hyperspectral imaging in predicting mycotoxin levels. Future work can focus on refining the model and exploring different dimensionality reduction techniques.
