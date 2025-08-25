# Emoji Sentiment Analysis

This project analyzes the sentiment associated with different emojis in tweets.

## Dataset

* Source: [Emojify Data (English)](https://www.kaggle.com/datasets/rexhaif/emojifydata-en) from Kaggle
* Original dataset was very large, so a **sample was taken** for analysis.
* The dataset was preprocessed into a CSV file with three columns:

  * **tweet** – Original tweet text with emoji
  * **text** – Tweet text without emoji
  * **emoji** – Extracted emoji from the tweet

## Sentiment Analysis

To analyze sentiment:

1. **Preprocessing:** Extracted tweet text and emojis into separate columns.
2. **Sentiment Assignment:** Used **VADER (Valence Aware Dictionary and sEntiment Reasoner)** from `nltk.sentiment.vader` to classify tweet text (without emojis) into **Positive, Negative, or Neutral** categories.
3. **Emoji Sentiment Mapping:** Assigned each emoji the sentiment of its corresponding tweet.
4. **Statistical Summary:** Calculated, for each emoji:

   * Total count (frequency)
   * Percentage of Positive, Negative, and Neutral sentiment occurrences
   * Stored results in `emoji_sentiment_stats.csv`

This mapping allowed analysis of which emojis are most commonly associated with each sentiment type.

## Visualizations (Plotly)

Five interactive visualizations were created:

1. **Top 20 Emojis by Frequency (Bar Chart)**
2. **Bubble Chart (Emoji vs Count vs Sentiment)**
3. **Donut Chart for Overall Sentiment Distribution**
4. **Word Cloud Approximation**
5. **Top Positive / Negative / Neutral Emojis**

## Files in Repo

* `data/emojitweets.csv` – Preprocessed dataset (sampled)
* `results/emoji_sentiment_stats.csv` – Emoji-level sentiment statistics
* `notebooks/main.ipynb` – Code for preprocessing, analysis, and visualization
* `README.md` – Project documentation

## Tools & Libraries Used

* Python
* NLTK (VADER Sentiment)
* Pandas, NumPy
* Plotly (Visualizations)
