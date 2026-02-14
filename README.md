# 🚚 Delivery Time Prediction – Machine Learning Deployment

This project builds an end-to-end Machine Learning pipeline to predict food delivery time and proposes a business strategy to reduce expectation–reality misalignment in delivery services.

Live App:
👉 https://deliveryprediction-kavdt8h2ccxtkc3tdzzstm.streamlit.app

---

## 📌 Problem Statement

In food delivery services, the core issue is not only delay, but the mismatch between estimated delivery time (ETA) and actual arrival time.

When the system shows:
> ETA: 40 minutes  
But the order arrives in 55 minutes  

Customers perceive this as service failure.

This project focuses on:
- Predicting delivery duration
- Understanding distribution variability
- Reducing underestimation risk
- Designing ETA strategy beyond raw model output

---

## 🎯 Objectives

1. Analyze key factors affecting delivery time
2. Build an interpretable regression model
3. Compare multiple algorithms
4. Deploy the model into a public Streamlit app
5. Propose percentile-based ETA strategy

---

## 🧠 Key Insights

### 1️⃣ Distribution is Right-Skewed
Delivery time distribution shows a right skew, meaning a small number of extreme delays significantly affect the mean.

This increases underestimation risk if using mean prediction only.

### 2️⃣ Distance is the Strongest Driver
Delivery distance shows near-linear relationship with duration, making Linear Regression a strong baseline model.

### 3️⃣ Model Performance
- Model: Linear Regression
- MAE: ~6 minutes
- R²: ~0.82

More complex models (Random Forest, XGBoost) only gave marginal improvement, so linear regression was selected for interpretability and stability.

---

## 📊 Percentile-Based Risk Analysis

To manage delivery uncertainty, percentile segmentation was analyzed:

- P5  = 24 minutes  
- P95 = 95 minutes  

Meaning:
- 5% fastest deliveries finish within 24 minutes
- 95% deliveries finish within 95 minutes
- Only 5% exceed 95 minutes (SLA breach risk zone)

This enables risk-adjusted ETA strategies.

---

## 🚀 Business Recommendation

Instead of relying purely on mean prediction:

### Short Distance
Use mean prediction (low variability)

### Medium Distance
Use mean + buffer or P75

### Long Distance
Use P75–P90 to reduce underestimation risk

Optional:
Display ETA range (e.g., 40–55 minutes) for high-variance segments to manage customer expectations.

---

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Streamlit
- Joblib

---

## 📦 Project Structure

