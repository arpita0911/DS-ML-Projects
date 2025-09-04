
---

# Airbnb Price Prediction & Analysis

This project predicts **Airbnb listing prices** using **Machine Learning**.
It leverages **data preprocessing, feature engineering, and tree-based models** to capture the relationships between listing characteristics (room type, property type, location, amenities, etc.) and price.
The project also compares the performance of **Linear Regression, Random Forest, and XGBoost** models.

---

## Project Overview

* **Dataset:**

  * Source: [Airbnb Listings Dataset – Kaggle](https://www.kaggle.com/datasets/lovishbansal123/airbnb-data/data)
  * Contains listing details for multiple US cities: room type, property type, number of bedrooms, amenities, host information, location (latitude/longitude), reviews, and price.

* **Workflow:**

  * Data cleaning & missing value imputation.
  * Feature engineering:

    * Numeric features: `bathrooms`, `bedrooms`, `beds`, `accommodates`, `num_amenities`, etc.
    * Categorical features: one-hot encoding (`room_type`, `bed_type`, `property_type_simplified`, `cancellation_policy`, `city`)
    * Frequency encoding for `neighbourhood` and `zipcode`
    * Derived features: `days_since_first_review`, `days_since_last_review`, `host_days`, `bathrooms_per_guest`, `beds_per_guest`
    * Sentiment score attached to `description`
  * Train/test split (80/20)
  * Scaling numeric features for regression (optional for tree-based models)
  * Model training: Linear Regression, Random Forest, XGBoost
  * Evaluation using **RMSE, MAE, R² score**
  * Feature importance analysis & visualizations

---

## Tech Stack

* **Python 3.x**
* **Pandas, NumPy** – data manipulation
* **Scikit-learn** – preprocessing, regression models, evaluation metrics
* **XGBoost** – advanced regression model
* **Matplotlib, Seaborn** – visualization

---

## Project Structure

```
├── main.py              # Main script: preprocessing, training, evaluation, visualizations
├── requirements.txt     # Required dependencies
├── README.md            # Project documentation
├── data/                # Airbnb Kaggle dataset
```

---

## Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/arpita0911/DS-ML_Projects/airbnb-price-prediction.git
cd airbnb-price-prediction
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

Run the main analysis and model pipeline:

```bash
jupyter notebook
```

---

## Model Evaluation

| Model               | RMSE  | MAE   | R²     |
| ------------------- | ----- | ----- | ------ |
| Linear Regression   | 0.46  | 0.35  | 0.5834 |
| Random Forest (log) | 0.414 | 0.301 | 0.6666 |
| XGBoost (log)       | 0.386 | 0.279 | 0.7098 |

* **Note:** Target variable is log-transformed `log_price`. RMSE and MAE are on log scale. Actual price error roughly translates to `exp(RMSE)` multiplicative error.

---

## Results

* **Linear Regression:**

  * Captures general trends but struggles with non-linear relationships.
  * R² \~0.58, moderate predictive power.

* **Random Forest:**

  * Handles nonlinearities and feature interactions better.
  * R² \~0.67, lower RMSE/MAE than Linear Regression.

* **XGBoost:**

  * Best performance among the three models.
  * R² \~0.71, lowest RMSE and MAE.
  * Captures subtle feature interactions and non-linear effects.

---

## Feature Importance (Top Features – XGBoost)

| Feature                  | Importance |
| ------------------------ | ---------- |
| room\_type\_Private room | 0.34       |
| room\_type\_Shared room  | 0.23       |
| bedrooms                 | 0.09       |
| is\_new\_listing         | 0.058      |
| city\_SF                 | 0.04       |
| bathrooms                | 0.02       |
| city\_DC                 | 0.016      |
| city\_LA                 | 0.015      |
| ...                      | ...        |

* Room type and location dominate pricing decisions.
* Other features like `bathrooms`, `bedrooms`, `amenities`, and `cancellation_policy` contribute moderately.

---

## Visualizations

* **Actual vs Predicted Prices** – scatter plot with perfect prediction line
* **Residuals Plot** – shows distribution of prediction errors
* **Prediction Error Histogram** – error distribution analysis
* **Feature Importance Bar Chart** – top 20 features driving predictions

---

