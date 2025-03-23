# House Price Prediction API

## Overview
This is a **Machine Learning-based API** that predicts house prices based on given input features. The API is deployed on **Render** and is accessible via an HTTP request.

## Deployment Link
**Base API URL:** [House Price Prediction API](https://house-price-prediction-1-d7xc.onrender.com)

## API Endpoints

### 1️⃣ Check if API is Running
**Endpoint:** `/`
- **Method:** GET
- **Description:** Returns a simple message confirming that the API is running.
- **Example Response:**
  ```json
  {
      "message": "House Price Prediction API is running!"
  }
  ```

### 2️⃣ Predict House Price
**Endpoint:** `/predict`
- **Method:** POST
- **Description:** Accepts JSON input and returns the predicted house price.
- **Request Format:** JSON
- **Example Request Body:**
  ```json
  {
    "area": 3000,
    "bedrooms": 2,
    "bathrooms": 1,
    "stories": 0,
    "parking": 1,
    "mainroad_yes": 0,
    "guestroom_yes": 1,
    "basement_yes": 0,
    "hotwaterheating_yes": 1,
    "airconditioning_yes": 1,
    "prefarea_yes": 1,
    "furnishingstatus_semi-furnished": 1,
    "furnishingstatus_unfurnished": 0
}
  ```
- **Example Response:**
  ```json
  {
      "predicted_price": 450000
  }
  ```

## How to Use
### Using **Postman**
1. Open **Postman**
2. Select **POST** as the request type
3. Enter the prediction **API Endpoint:**
   ```
   https://house-price-prediction-1-d7xc.onrender.com/predict
   ```
4. Go to the **Body** tab
5. Select **raw** and set the format to **JSON**
6. Enter the JSON input as shown above
7. Click **Send**
8. View the **predicted price** in the response

## Technologies Used
- **Flask** (Backend API Framework)
- **Scikit-learn** (Machine Learning Model)
- **Render** (Deployment)

## Author
Created by **Arpit-528**

