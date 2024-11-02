# Mobile Phone Price Prediction API Documentation

## Overview
This API provides endpoints to manage and predict mobile phone prices based on their specifications. It allows you to create and retrieve mobile phone records, as well as predict price ranges for existing devices.

## Base URL
http://your-domain.com/ or http://localhost:8000/

## Endpoints

### 1. List/Create Mobile Phones
- **URL:** `/api/devices/`
- **Methods:** GET, POST
- **Description:** Get a list of all mobile phones or create a new mobile phone entry

#### GET Response
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

#### POST Request Body
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

### 2. Retrieve Mobile Phone
- **URL:** `/api/devices/<device_id>/`
- **Methods:** GET
- **Description:** Get individual mobile phone record

### 3. Predict Price
- **URL:** `/api/predict/<device_id>/`
- **Method:** POST
- **Description:** predict the price, and save the result in the device entity

## Data Models

### Mobile Phone

| Field         | Type    | Description                                    |
|---------------|---------|------------------------------------------------|
| battery_power | Integer | Total energy a battery can store in mAh        |
| blue          | Integer | Has Bluetooth or not (0/1)                     |
| clock_speed   | Float   | Speed at which microprocessor executes         |
| dual_sim      | Integer | Has dual sim support or not (0/1)             |
| fc            | Integer | Front Camera megapixels                        |
| four_g        | Integer | Has 4G or not (0/1)                           |
| int_memory    | Integer | Internal Memory in Gigabytes                   |
| m_dep         | Float   | Mobile Depth in cm                             |
| mobile_wt     | Integer | Weight of mobile phone                         |
| n_cores       | Integer | Number of cores of processor                   |
| pc            | Integer | Primary Camera megapixels                      |
| px_height     | Integer | Pixel Resolution Height                        |
| px_width      | Integer | Pixel Resolution Width                         |
| ram           | Integer | Random Access Memory in Megabytes              |
| sc_h          | Float   | Screen Height of mobile in cm                  |
| sc_w          | Float   | Screen Width of mobile in cm                   |
| talk_time     | Integer | Longest time that battery charge will last     |
| three_g       | Integer | Has 3G or not (0/1)                           |
| touch_screen  | Integer | Has touch screen or not (0/1)                 |
| wifi          | Integer | Has wifi or not (0/1)                         |
| price_range   | Integer | Price range category (0-3)                    |

## Price Range Categories
- 0: Low Cost
- 1: Medium Cost
- 2: High Cost
- 3: Very High Cost

## Admin Interface
The API includes an admin interface with the following features:
- Import/Export functionality for bulk data management
- List display showing ID, price range, battery power, RAM, and internal memory
- Filtering by price range, 4G, 3G, WiFi, and touch screen
- Search functionality by ID

### Credentials
- **url endpoint:** admin/
- **Username:** admin
- **Password:** admin




## Notes
- All boolean fields (blue, dual_sim, four_g, three_g, touch_screen, wifi) are stored as integers (0/1)
- The price_range field is nullable and can be left blank during creation
- The API uses Django REST Framework's ModelSerializer for data validation and serialization
