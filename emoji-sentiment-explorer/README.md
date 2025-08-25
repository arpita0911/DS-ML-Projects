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

Five interactive visualizations are available in the **`charts/` folder**. Click the links to view each chart in your browser:

1. **[Top 20 Emojis by Frequency (Bar Chart)](https://htmlpreview.github.io/?https://media.githubusercontent.com/media/arpita0911/DS-ML-Projects/refs/heads/main/emoji-sentiment-explorer/charts/top_20_emojis.html)**
2. **[Bubble Chart (Emoji vs Count vs Sentiment)](https://htmlpreview.github.io/?https://media.githubusercontent.com/media/arpita0911/DS-ML-Projects/refs/heads/main/emoji-sentiment-explorer/charts/emoji_bubble_chart.html)**
3. **[Donut Chart for Overall Sentiment Distribution](https://htmlpreview.github.io/?https://media.githubusercontent.com/media/arpita0911/DS-ML-Projects/refs/heads/main/emoji-sentiment-explorer/charts/sentiment_distribution.html)**
4. **[Word Cloud Approximation](https://htmlpreview.github.io/?https://media.githubusercontent.com/media/arpita0911/DS-ML-Projects/refs/heads/main/emoji-sentiment-explorer/charts/emoji_wordcloud.html)**
5. **[Top Positive / Negative / Neutral Emojis](https://htmlpreview.github.io/?https://media.githubusercontent.com/media/arpita0911/DS-ML-Projects/refs/heads/main/emoji-sentiment-explorer/charts/top_sentiment_emojis.html)**

## Files in Repo

* `data/emojitweets.csv` – Preprocessed dataset (sampled)
* `results/emoji_sentiment_stats.csv` – Emoji-level sentiment statistics
* `notebooks/main.ipynb` – Code for preprocessing, analysis, and visualization
* `charts/` – Folder containing interactive Plotly visualizations
* `README.md` – Project documentation

## Tools & Libraries Used

* Python
* NLTK (VADER Sentiment)
* Pandas, NumPy
* Plotly (Visualizations)




