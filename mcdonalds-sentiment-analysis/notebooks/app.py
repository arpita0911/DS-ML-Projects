import streamlit as st
import pickle
import numpy as np
import re, string
from nltk.corpus import stopwords
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
import os



stop_words = set(stopwords.words('english'))

base_path = os.path.dirname(__file__)  
model_path = os.path.join(base_path, "../output/sentiment_model.pkl")
tfidf_path = os.path.join(base_path, "../output/tfidf.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(tfidf_path, "rb") as f:
    tfidf = pickle.load(f)


# VADER
analyzer = SentimentIntensityAnalyzer()

stop_words = set(stopwords.words("english"))

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\d+", "", text)
    words = text.split()
    words = [word for word in words if word not in stop_words]
    words = word_tokenize(text)
    words = [w for w in words if w not in stop_words or w in ['not', 'no']]
    
    return ' '.join(words)



# Streamlit UI
st.title("🍔 McDonald's Review Sentiment Predictor")
st.write("Enter your review and get instant sentiment analysis!")

review = st.text_area("Type your review here:")

if st.button("Predict Sentiment"):
    if review.strip() != "":
        # --- Clean text for TF-IDF ---
        cleaned_review = clean_text(review)
        tfidf_features = tfidf.transform([cleaned_review]).toarray()

        # --- VADER on raw/original ---
        vader_scores = analyzer.polarity_scores(review)
        vader_features = np.array([
            vader_scores["pos"],
            vader_scores["neu"],
            vader_scores["neg"],
            vader_scores["compound"]
        ]).reshape(1, -1)

        # --- Combine features ---
        final_features = np.hstack((tfidf_features, vader_features))

        # Define mapping
        mapping = {0: "Negative", 1: "Neutral", 2: "Positive"}

        # Predict
        prediction = model.predict(final_features)[0]
        prob = model.predict_proba(final_features)[0]

        # Get label
        label = mapping[prediction]

        # Show result with confidence
        if prediction == 2:
            st.success(f"✅ {label} Review ({prob[2]*100:.2f}% confidence)")
        elif prediction == 1:
            st.info(f"😐 {label} Review ({prob[1]*100:.2f}% confidence)")
        else:
            st.error(f"❌ {label} Review ({prob[0]*100:.2f}% confidence)")

    else:
        st.warning("⚠️ Please enter a review.")
