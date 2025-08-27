
---

# Handwritten Digit Classifier (MNIST – CNN)

This project implements a **Convolutional Neural Network (CNN)** to classify handwritten digits (0–9) using the **MNIST dataset**.
It demonstrates supervised learning, model evaluation, and visualization of results.

---

## 📌 Project Overview

* Dataset: **MNIST** (60,000 training + 10,000 test grayscale digit images).
* Model: CNN with convolution, pooling, dropout, and dense layers.
* Task: Classify digits (0–9) with high accuracy.
* Evaluation: Accuracy, confusion matrix, and classification report.
* Visualization: Predictions with actual labels and heatmap of confusion matrix.

---

## ⚙️ Tech Stack

* **Python 3.x**
* **TensorFlow / Keras**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **Pandas**
* **Scikit-learn**

---

## 📂 Project Structure

```
├── main.py              # Main training and evaluation script
├── requirements.txt     # Required dependencies
├── README.md            # Project documentation
```

---

## 🚀 Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/arpita0911/DS-ML_Projects/handwritten-digit-classifier.git
cd handwritten-digit-classifier
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Run the training and testing script:

```bash
python main.py
```

---

## 📊 Model Evaluation

* Prints **training/validation accuracy & loss**.
* Displays **confusion matrix**.
* Shows **classification report** with precision, recall, F1-score.
* Visualizes **predicted vs actual digits**.

Example visualization:

```
Predicted: 7, Actual: 7
Predicted: 2, Actual: 2
Predicted: 1, Actual: 1
```

---

## ✅ Results

* Achieved **\~98% test accuracy** on MNIST dataset.
* Model correctly classifies most handwritten digits with minimal errors.

---

## 🔮 Future Improvements

* Experiment with **deeper CNN architectures**.
* Use **data augmentation** to improve robustness.
* Deploy as a **web app (Flask/Streamlit)** for interactive digit prediction.

---
