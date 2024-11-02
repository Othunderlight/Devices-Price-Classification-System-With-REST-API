# Mobile Device Price Classification System Documentation

## Project Overview
This project implements an AI-driven system for classifying mobile device prices based on their specifications. The system uses machine learning to predict price ranges (0-3) for mobile devices, helping sellers accurately price their products.

## Implementation Details

### Data Processing
- Dataset loaded from CSV files (train.csv and test.csv)
- Null values removed using dropna()
- Features standardized using StandardScaler
- Data split: 70% training, 15% validation, 15% testing

### Model Architecture
- Algorithm: Logistic Regression (selected for optimal performance)
- Hyperparameter tuning using GridSearchCV
- Best parameters:
  - Determined through cross-validation
  - Optimized for accuracy

### Model Performance Metrics
- Final Model Accuracy on Test Data: 97%
- Average confidence score: 0.92
- Consistent performance across all price ranges

### Feature Analysis
Key insights from exploratory data analysis:
- RAM shows strong positive correlation with price
- Battery power has minimal impact on pricing
- Screen resolution (px_height, px_width) shows limited correlation with price

### Algorithm Selection Rationale
Compared against other algorithms:

| Algorithm        | Speed | Accuracy | Resource Usage | Selected |
|-----------------|-------|-----------|----------------|-----------|
| Logistic Regression | Fast  | High      | Low           | ✓ |
| SVM             | Moderate | High    | High          | |
| Random Forest   | Moderate | Very High| High          | |
| KNN Classifier  | Fast    | Moderate | Moderate      | |

Logistic Regression was chosen for:
- Fast training time
- Low resource requirements
- High accuracy (97%)
- Suitable for linear classification tasks

### Model Persistence
- Model saved using joblib
- Scaler saved separately for preprocessing new data
- File names:
  - best_model.pkl
  - standard_scaler.pkl


### Dataset Description

#### Input Features
- **Device Specifications**
  - **battery_power**: Total energy a battery can store (mAh)
  - **blue**: Bluetooth availability (1/0)
  - **clock_speed**: Microprocessor execution speed (GHz)
  - **dual_sim**: Dual SIM support (1/0)
  - **fc**: Front Camera megapixels
  - **four_g**: 4G support (1/0)
  - **int_memory**: Internal Memory (GB)
  - **m_dep**: Mobile Depth (cm)
  - **mobile_wt**: Device weight
  - **n_cores**: Processor core count
  - **pc**: Primary Camera megapixels
  - **px_height**: Pixel Resolution Height
  - **px_width**: Pixel Resolution Width
  - **ram**: Random Access Memory (MB)
  - **sc_h**: Screen Height (cm)
  - **sc_w**: Screen Width (cm)
  - **talk_time**: Battery life during calls
  - **three_g**: 3G support (1/0)
  - **touch_screen**: Touch screen availability (1/0)
  - **wifi**: WiFi support (1/0)

#### Target Variable
- **price_range**: Device price category
  - 0: Low cost
  - 1: Medium cost
  - 2: High cost
  - 3: Very high cost

## Model Performance
The current model implementation achieves:
- Average confidence score: 0.92
- Consistent performance across all price ranges
- High prediction reliability




