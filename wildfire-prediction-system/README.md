
---

# **Wildfire Risk Analysis and Prediction System**

## **Overview**

This project performs end-to-end wildfire analysis and large-fire risk prediction using environmental, spatial, and temporal features. It includes full data preprocessing, statistical testing, machine learning modeling with LightGBM, and an interactive Power BI dashboard for decision-making and risk monitoring.

---

## **Dataset Sources**

* **Wildfire Dataset:** `https://www.kaggle.com/datasets/rtatman/188-million-us-wildfires`
* **Weather / Environmental Dataset:** `https://www.kaggle.com/datasets/leternnoz/188-million-us-wildfires-weather-data`

Both datasets were merged using OBJECTID to create a unified modeling dataset.

---

## **Key Features**

*  End-to-end data preprocessing & feature engineering
*  Exploratory Data Analysis focusing on seasonal, spatial, and weather trends
*  Statistical validation (Chi-Square, ANOVA, T-Test)
*  Machine Learning using LightGBM for predicting large fires
*  Model evaluation with recall, accuracy, error rate & calibration
*  Power BI dashboard with interactive filters, KPIs, maps, and prediction visuals

---

## **Project Structure**

```
project/
│── data/                # Raw & processed datasets
│── notebooks/           # EDA,preprocessing, training, evaluation notebook
│── powerbi/             # Power BI dashboard (.pbix)
│── output/              # results and exports for powerbi
│── README.md
│── requirements.txt
```

---

## **Methodology**

### **1. Data Preprocessing**

* Cleaned missing geospatial/weather values
* Extracted temporal features (year, month, season)
* Engineered fire-weather interactions and aggregated weather metrics
* Encoded categorical variables; normalized numeric features

### **2. Statistical Analysis**

* **Chi-Square:** Season and fire size significantly related
* **ANOVA:** Mean temperature differs across fire size classes
* **T-Test:** Large fires occur at significantly higher temperatures

### **3. Machine Learning Model**

* Algorithm: **LightGBM (GBDT)** optimized for recall
* Target variable: `LARGE_FIRE` (binary)
* Key features: latitude, longitude, cause code, temperature, wind speed, precipitation

### **4. Model Evaluation**

* High **recall** for large fire detection
* Balanced with acceptable accuracy and error rate
* Calibration curve validates probability reliability
* Confusion matrix reveals false-positive trade-off

---

## **Power BI Dashboard**

Includes two pages:

### ** Page 1 — Wildfire Trends & Insights**

* KPIs: Total fires, large fires, % large fires, avg fire weather index
* Donut chart: Fire causes
* Geo-map: Large fire concentration
* Trend charts: Fires by year, month, state, county
* Scatter plot: Temperature vs precipitation for large fires

### ** Page 2 — Model Predictions & Performance**

* KPIs: Recall, accuracy, error rate, avg predicted probability
* Distribution of predicted fire risk
* Actual vs predicted probability scatter
* Geo-map of predicted large-fire probability
* Feature importance from LightGBM
* Calibration curve and confusion matrix
* Predicted vs actual large fires by state

---

## **Technologies Used**

### **Languages & Libraries**

* Python (pandas, numpy, LightGBM, sklearn, scipy, matplotlib, seaborn)

### **Dashboard**

* **Microsoft Power BI**

---

## **Installation**

```
pip install -r requirements.txt
```

---

## **How to Run**

1. Place datasets in `/data/`
2. Run notebook or script
3. Export predictions for Power BI
4. Open `Wildfire_Dashboard.pbix` in Power BI

---

## **Results & Insights**

* Hot, dry months (especially summer) show higher large-fire likelihood
* Spatial hotspots detected in high-temperature, low-precipitation regions
* LightGBM effectively captures spatial-temporal risk patterns
* Dashboard supports resource allocation, risk monitoring, and planning

---

## **Future Work**

* Incorporate satellite vegetation indices (NDVI, drought codes)
* Test deep learning and time-series models
* Enable real-time prediction using live weather feeds

---