# Devices Price Classification System

## Project Overview
The Devices Price Classification System is an AI-driven application designed to predict mobile device prices based on their specifications. This system utilizes machine learning to classify prices into categories (0-3), helping sellers accurately price their products.

## Project Components
This project consists of two main components:

1. **Mobile Phone Price Prediction API**: 
   - Provides endpoints to manage and predict mobile phone prices based on specifications.
   - Built using Django REST Framework.

2. **Mobile Device Price Classification System**:
   - Implements machine learning algorithms to classify mobile device prices.
   - Built using Python and various machine learning libraries.

## API Documentation
### Overview
The API allows users to create, retrieve, and predict mobile phone records. 

### Base URL
- `http://your-domain.com/` or `http://localhost:8000/`

### Endpoints
1. **List/Create Mobile Phones**
   - **URL**: `/api/devices/`
   - **Methods**: GET, POST
   - **Description**: Retrieve a list of all mobile phones or create a new entry.

   **GET Response Example**:
   ```json
   [
       {
           "id": 1,
           "battery_power": 1000,
           "blue": 1,
           "clock_speed": 2.2,
           ...
           "price_range": 3
       }
   ]
   ```

   **POST Request Body Example**:
   ```json
   {
       "battery_power": 1000,
       "blue": 1,
       "clock_speed": 2.2,
       "dual_sim": 1,
       "fc": 8,
       "four_g": 1,
       "int_memory": 64,
       "m_dep": 0.7,
       "mobile_wt": 180,
       "n_cores": 8,
       "pc": 12,
       "px_height": 1920,
       "px_width": 1080,
       "ram": 4096,
       "sc_h": 15.5,
       "sc_w": 7.5,
       "talk_time": 20,
       "three_g": 1,
       "touch_screen": 1,
       "wifi": 1,
       "price_range": null
   }
   ```

2. **Retrieve Mobile Phone**
   - **URL**: `/api/devices/<device_id>/`
   - **Methods**: GET
   - **Description**: Retrieve an individual mobile phone record.

3. **Predict Price**
   - **URL**: `/api/predict/<device_id>/`
   - **Method**: POST
   - **Description**: Predict the price and save the result in the device entity.

### Data Models
The API uses the following data model for mobile phones:

| Field         | Type    | Description                                    |
|---------------|---------|------------------------------------------------|
| battery_power | Integer | Total energy a battery can store in mAh        |
| blue          | Integer | Has Bluetooth or not (0/1)                     |
| clock_speed   | Float   | Speed at which microprocessor executes         |
| dual_sim      | Integer | Has dual sim support or not (0/1)             |
| ...           | ...     | ...                                            |
| price_range   | Integer | Price range category (0-3)                    |

### Price Range Categories
- 0: Low Cost
- 1: Medium Cost
- 2: High Cost
- 3: Very High Cost

## Machine Learning Implementation
### Overview
The machine learning component of the project classifies mobile device prices based on their specifications.

### Data Processing
- Datasets are loaded from CSV files (train.csv and test.csv).
- Null values are removed, and features are standardized.
- Data is split into training (70%), validation (15%), and testing (15%).

### Model Architecture
- **Algorithm**: Logistic Regression
- **Performance**: Achieved 97% accuracy on test data with an average confidence score of 0.92.

### Model Persistence
- The model and scaler are saved using joblib for future predictions.
- [Best Model](algorithm/best_model.pkl)
- [Standard Scaler](algorithm/standard_scaler.pkl)

## Conclusion
This project provides a comprehensive solution for mobile device price classification, integrating a robust API with a powerful machine learning model. The system is designed to assist sellers in accurately pricing their products based on detailed specifications.

For further details, please refer to the individual documentation files:
- [Mobile Phone Price Prediction API Documentation](backend/docs.md)
- [Mobile Device Price Classification System Documentation](algorithm/docs.md)
