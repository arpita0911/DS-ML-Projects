---

# **Algerian Forest Fires Prediction System**

## **Overview**

This project performs fire risk prediction using the Fire Weather Index (FWI) for Algerian forest fires. It includes data preprocessing, exploratory data analysis, regression modeling with Ridge Regression, and a Flask-based web application for real-time fire risk assessment.

---

## **Dataset Information**

* **Source:** Algerian Forest Fires Dataset
* **Total Instances:** 244 (122 from each region)
* **Time Period:** June 2012 to September 2012
* **Regions:** 
  - Bejaia (northeast Algeria)
  - Sidi Bel-abbes (northwest Algeria)
* **Classes:** Fire (138 instances) and Not Fire (106 instances)

### **Attribute Information**

**Weather Data Observations:**
* **Temperature:** Maximum temperature at noon (°C) — Range: 22 to 42
* **RH:** Relative Humidity (%) — Range: 21 to 90
* **Ws:** Wind speed (km/h) — Range: 6 to 29
* **Rain:** Total daily rainfall (mm) — Range: 0 to 16.8

**FWI System Components:**
* **FFMC:** Fine Fuel Moisture Code — Range: 28.6 to 92.5
* **DMC:** Duff Moisture Code — Range: 1.1 to 65.9
* **DC:** Drought Code — Range: 7 to 220.4
* **ISI:** Initial Spread Index — Range: 0 to 18.5
* **BUI:** Buildup Index — Range: 1.1 to 68
* **FWI:** Fire Weather Index (target variable) — Range: 0 to 31.1

---

## **Key Features**

* End-to-end data preprocessing & feature engineering
* Exploratory Data Analysis focusing on temporal and regional trends
* Feature correlation analysis and outlier detection
* Machine Learning using Ridge Regression for FWI prediction
* Model evaluation with MAE and R² Score
* Flask web application with interactive UI for real-time predictions

---

## **Project Structure**

```
project/
│── data/
│     └── Algerian_forest_fires_cleaned_dataset.csv
│     └── Algerian_forest_fires_dataset.csv
│── notebooks/
│     ├── Data Cleaning and EDA.ipynb
│     └── Model Training.ipynb
│── models/
│     ├── ridge.pkl
│     └── scaler.pkl
│── templates/
│     └── home.html
│── application.py
│── requirements.txt
└── README.md
```

---

## **Methodology**

### **1. Data Preprocessing**

* Cleaned missing values and removed whitespace
* Extracted temporal features (day, month, year)
* Handled outliers and data inconsistencies
* Encoded categorical variables (Classes, Region)
* Normalized features using StandardScaler

### **2. Exploratory Data Analysis**

* **Temporal Analysis:** August and September showed peak fire activity
* **Regional Patterns:** Both regions exhibited similar fire trends with August being critical
* **Correlation Analysis:** Identified strong relationships between FWI components
* **Distribution Analysis:** Examined feature distributions and class imbalance

### **3. Machine Learning Model**

* **Algorithms Tested:** Linear Regression, Lasso, Ridge, ElasticNet
* **Final Model:** Ridge Regression (L2 regularization)
* **Target Variable:** Fire Weather Index (FWI)
* **Key Features:** Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region

### **4. Model Evaluation**

* Evaluated using Mean Absolute Error (MAE)
* Assessed using R² Score for variance explanation
* Ridge Regression selected for optimal bias-variance trade-off
* Model validated on test set for generalization

---

## **Flask Web Application**

### **Features**

* User-friendly web interface for fire risk prediction
* Real-time FWI calculation based on input parameters
* Form validation and error handling
* RESTful API endpoint for predictions

### **Input Parameters**

* Temperature (°C)
* Relative Humidity (%)
* Wind Speed (km/h)
* Rainfall (mm)
* FFMC index
* DMC index
* ISI index
* Classes (0 = Not Fire, 1 = Fire)
* Region (0 = Bejaia, 1 = Sidi Bel-abbes)

---

## **Technologies Used**

### **Languages & Libraries**

* Python (pandas, numpy, scikit-learn, matplotlib, seaborn)
* Flask (web framework)
* pickle (model serialization)

### **Machine Learning**

* Ridge Regression with StandardScaler preprocessing

---

## **Installation**

```bash
pip install -r requirements.txt
```

**Required Libraries:**
```
Flask
numpy
pandas
scikit-learn
matplotlib
seaborn
```

---

## **How to Run**

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd algerian-forest-fires-prediction
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the Flask application:**
   ```bash
   python application.py
   ```

4. **Access the web interface:**
   ```
   http://localhost:5000
   ```

5. **Make predictions:**
   * Enter weather and FWI component values
   * Click "Predict" to get FWI prediction

---

## **API Endpoint**

### **POST** `/predictdata`

**Request Body (form-data):**
```json
{
  "Temperature": 30,
  "RH": 50,
  "Ws": 15,
  "Rain": 0,
  "FFMC": 85.5,
  "DMC": 25.3,
  "ISI": 8.2,
  "Classes": 1,
  "Region": 0
}
```

**Response:**
Returns predicted FWI value displayed on web page

---

## **Results & Insights**

* **Seasonal Patterns:** Fire incidents peak during summer months (August and September)
* **Regional Analysis:** Both Bejaia and Sidi Bel-abbes regions show similar fire patterns
* **Weather Impact:** Temperature, humidity, and wind speed significantly influence fire risk
* **Model Performance:** Ridge Regression provides robust predictions with good generalization
* **FWI Components:** FFMC, DMC, and ISI are strong predictors of fire weather conditions

---

## **Future Work**

* Incorporate real-time weather API integration
* Implement ensemble methods (Random Forest, XGBoost) for comparison
* Add time-series forecasting for long-term fire risk prediction
* Create interactive dashboards using Plotly or Streamlit
* Deploy to cloud platforms (AWS, Azure, Heroku)
* Add geospatial visualization for fire risk mapping
* Implement model retraining pipeline with new data

---

## **Acknowledgments**

* Dataset based on Algerian forest fires research
* FWI system components from Canadian Forest Fire Weather Index System
* Built with Flask, scikit-learn, and modern data science tools

---
