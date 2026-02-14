# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import joblib
import time

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="Delivery Time Predictor",
    page_icon="🚚",
    layout="wide"
)

# ===============================
# LOAD MODEL
# ===============================
@st.cache_resource
def load_model():
    return joblib.load("best_delivery_time_pipeline.joblib")

model = load_model()

# ===============================
# CUSTOM STYLE
# ===============================
st.markdown("""
<style>
.main-title {
    font-size: 36px;
    font-weight: 700;
}
.subtitle {
    font-size: 18px;
    color: gray;
}
.result-box {
    background-color: #f5f7fa;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
}
.big-number {
    font-size: 32px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# HEADER
# ===============================
st.markdown('<p class="main-title">🚚 Delivery Time Prediction</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Estimate delivery duration using Machine Learning</p>', unsafe_allow_html=True)
st.markdown("---")

# ===============================
# SIDEBAR
# ===============================
st.sidebar.header("📊 Model Information")
st.sidebar.write("**Model:** Linear Regression")
st.sidebar.write("**MAE:** 6.06")
st.sidebar.write("**R²:** 0.82")
st.sidebar.markdown("---")
st.sidebar.write("Built by Raegan Ammar Prawira")

# ===============================
# MAIN LAYOUT
# ===============================
col1, col2 = st.columns(2)

# ===============================
# INPUT SECTION
# ===============================
with col1:
    st.subheader("📦 Order Details")

    distance_km = st.number_input(
        "Distance (km)",
        min_value=0.0,
        value=5.0
    )

    weather = st.selectbox(
        "Weather Condition",
        ["Sunny", "Rainy", "Foggy", "Stormy"]
    )

    traffic_level = st.selectbox(
        "Traffic Level",
        ["Low", "Medium", "High"]
    )

    vehicle_type = st.selectbox(
        "Vehicle Type",
        ["Bike", "Car", "Scooter"]
    )

    time_of_day = st.selectbox(
        "Time of Day",
        ["Morning", "Afternoon", "Evening", "Night"]
    )

    courier_experience_yrs = st.number_input(
        "Courier Experience (years)",
        min_value=0.0,
        value=2.0
    )

    preparation_time_min = st.number_input(
        "Preparation Time (minutes)",
        min_value=0.0,
        value=15.0
    )

    predict_button = st.button("🚀 Predict Delivery Time")

# ===============================
# PREDICTION SECTION
# ===============================
with col2:
    st.subheader("📈 Prediction Result")

    if predict_button:
        with st.spinner("Calculating prediction..."):
            time.sleep(1)

            input_data = pd.DataFrame([{
                "distance_km": distance_km,
                "weather": weather,
                "traffic_level": traffic_level,
                "vehicle_type": vehicle_type,
                "time_of_day": time_of_day,
                "courier_experience_yrs": courier_experience_yrs,
                "preparation_time_min": preparation_time_min
            }])

            prediction = model.predict(input_data)[0]

        st.markdown(
            f"""
            <div class="result-box">
                <p>Estimated Delivery Time</p>
                <p class="big-number">{round(prediction, 2)} minutes</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("")

        # Business Insight
        if prediction <= 30:
            st.success("⚡ Fast Delivery Expected")
        elif prediction <= 60:
            st.warning("🚦 Moderate Delivery Time")
        else:
            st.error("🚨 High Risk of Delay")

        st.markdown("---")
        st.info("Prediction generated using trained regression pipeline.")

# ===============================
# FOOTER
# ===============================
st.markdown("---")
st.caption("© 2026 Delivery Time ML Deployment Project")
