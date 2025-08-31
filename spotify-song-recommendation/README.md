
---

# Spotify Song Recommendation System

This project builds a **song recommendation system** using a **Spotify tracks dataset**.
It leverages **audio features**, **K-Means clustering**, and **PCA** to recommend songs with a **similar vibe** to a given input song.
Users can input a song name, and the system returns **15 songs most similar** in audio characteristics and musical style.

Dataset used: [Spotify Tracks Attributes and Popularity – Kaggle](https://www.kaggle.com/datasets/melissamonfared/spotify-tracks-attributes-and-popularity)

---

## Project Overview

* **Dataset: Spotify Tracks Attributes and Popularity (Kaggle)**

  * Contains information about tracks including audio features and metadata.
  * Columns include:

    * `track_name`, `artists`, `album_name`, `popularity`
    * Audio features: `danceability`, `energy`, `valence`, `tempo`, `acousticness`, `instrumentalness`, `speechiness`, `liveness`, `loudness`, `duration_ms`, `key`, `mode`, `time_signature`
    * `track_genre`

* **Workflow:**

  * Data preprocessing: cleaned data, handled missing values, scaled numerical features.

  * **K-Means clustering** on scaled audio features to group similar songs.

  * Evaluated cluster quality using **Calinski-Harabasz Index** and **Davies-Bouldin Index**:

    ```
    Without PCA:
      Calinski-Harabasz Index: 11498.44
      Davies-Bouldin Index: 2.55

    With PCA + Clustering:
      Calinski-Harabasz Index: 101921.37
      Davies-Bouldin Index: 0.68
    ```

  * Dimensionality reduction with **PCA** improved cluster compactness and separation.

  * Built a **recommendation system**: user inputs a song name, and the system returns **15 most similar songs**.

---

## Tech Stack

* **Python 3.x** – programming
* **Pandas, NumPy** – data manipulation
* **Seaborn, Matplotlib** – visualization
* **Scikit-learn** – scaling, PCA, K-Means, clustering evaluation, similarity
* **SciPy** – statistical analysis

---

## Project Structure

```
├── notebooks/main.py    # Main script (preprocessing, clustering, recommendation system)
├── requirements.txt     # Required dependencies
├── README.md            # Project documentation
├── data/                # Spotify tracks dataset (CSV from Kaggle)
```

---

## Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/arpita0911/DS-ML_Projects/spotify-song-recommendation.git
cd spotify-song-recommendation
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

Run the main recommendation pipeline:

```bash
python main.py
```

**Example interaction:**

```
Enter the song name: Heather

Similar vibe songs:
-----------------
Song 1
Song 2
Song 3
...
Song 15
```

*Note:* The input song **must exist in the dataset**.

---

## Clustering Evaluation

* **Without PCA:**

```
Calinski-Harabasz Index: 11498.44
Davies-Bouldin Index: 2.55
```

* **With PCA + Clustering:**

```
Calinski-Harabasz Index: 101921.37
Davies-Bouldin Index: 0.68
```

* PCA significantly improved cluster compactness and separation, leading to better recommendations.

---

## Results

* The system recommends songs **similar in vibe and audio characteristics**.
* Using PCA, the recommendations are more **accurate and relevant** compared to clustering without dimensionality reduction.
* Users can explore new songs while maintaining the **musical style** of their input track.

---
