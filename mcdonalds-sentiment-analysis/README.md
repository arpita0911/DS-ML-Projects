
---

# McDonald’s Reviews Sentiment Analysis & Visualization

This project analyzes customer reviews of **McDonald’s branches in the US and London** using **Natural Language Processing (NLP)** and **Machine Learning**.
It combines **rule-based sentiment (VADER)** with **Logistic Regression** trained on cleaned and vectorized text to classify reviews into **positive, neutral, and negative sentiments**.
The project further provides **time-based insights** and an **interactive Folium map visualization** of store-level sentiment across locations.

---

## Project Overview

* **Dataset 1 (US Reviews – Kaggle):**

  * Source: [McDonald’s Store Reviews (US)](https://www.kaggle.com/datasets/nelgiriyewithana/mcdonalds-store-reviews)
  * Contains customer reviews with ratings, dates, and geolocation (latitude/longitude).
  * Used for training, testing, and visualization.

* **Dataset 2 (London Reviews – Kaggle):**

  * Source: [Top 10 Recent Comments of All London McDonald’s](https://www.kaggle.com/datasets/lorentzyeung/top-10-recent-comments-of-all-london-mcdonalds)
  * Contains reviews but lacks ratings.
  * Sentiments were predicted using our trained model.

* **Workflow:**

  * Data cleaning & preprocessing (tokenization, stopwords removal).
  * Vectorization using **TF-IDF**.
  * Combined **VADER sentiment analysis** with ML-based classification.
  * Addressed **class imbalance** (neutral reviews).
  * Trained **Logistic Regression model** for sentiment prediction.
  * Evaluation with accuracy, precision, recall, and F1-score.
  * **Visualization:**

    * Time-based analysis of sentiment trends.
    * Location-based sentiment mapping with **Folium + MarkerCluster**.

---

## Tech Stack

* **Python 3.x**
* **Pandas, NumPy** – data manipulation
* **NLTK** – preprocessing & VADER sentiment analyzer
* **Scikit-learn** – TF-IDF, Logistic Regression, evaluation metrics
* **Matplotlib, Seaborn** – plots, heatmaps, confusion matrix
* **Folium** – interactive location-based sentiment visualization

---

## Project Structure

```
├── main.py              # Main script (data cleaning, training, evaluation, visualization)
├── requirements.txt     # Required dependencies
├── README.md            # Project documentation
├── data/                # Kaggle datasets (US & London McDonald’s reviews)
└── outputs/             # Output Dataset and generated map
```

---

## Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/arpita0911/DS-ML_Projects/mcdonalds-sentiment-analysis.git
cd mcdonalds-sentiment-analysis
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

Run the main analysis pipeline:

```bash
python main.py
```

---

## Model Evaluation

Using the **US Reviews** dataset, the model achieved:

* **Accuracy:** 0.82
* **Precision, Recall, F1-score:**

```
              precision    recall  f1-score   support

    Negative       0.83      0.89      0.86      2465
    Neutral        0.55      0.47      0.51       941
    Positive       0.88      0.87      0.87      3142

    accuracy                           0.82      6548
   macro avg       0.75      0.74      0.75      6548
weighted avg       0.81      0.82      0.82      6548
```

---

## Results

* **US Dataset:**

  * Strong performance with **82% accuracy**.
  * Reliable classification of positive and negative reviews.
  * Neutral class slightly harder to distinguish due to imbalance.

* **London Dataset:**

  * Since ratings were not provided, our **trained US model** assigned sentiment labels to reviews.

* **Visualizations:**

  * **Time-based sentiment trends** show how customer satisfaction changes over time.
  * **Location-based Folium map** with:

    * Circle markers sized & colored by positive sentiment percentage.
    * Clustered markers for easy navigation.

---

## Future Improvements

* Experiment with advanced models (**SVM, Random Forest, BERT**).
* Address class imbalance using techniques like **SMOTE** or weighted loss.
* Add interactive **dashboard (Streamlit/Power BI)** for business users.
* Incorporate **topic modeling (LDA)** to extract themes from reviews.

---
