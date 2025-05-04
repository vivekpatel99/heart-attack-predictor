import streamlit as st

st.title(
    "Heart Attack Predictor",
)
st.subheader("Enter your details below to predict heart attack risk")


sex = st.selectbox("Sex", ["Male", "Female"])
age = st.number_input("Age", min_value=1, max_value=100)
cholesterol = st.number_input("Cholesterol", min_value=0)
systolic_bp = st.number_input("Systolic Blood Pressure", min_value=0)
diastolic_bp = st.number_input("Diastolic Blood Pressure", min_value=0)
heart_rate = st.number_input("Heart Rate", min_value=0)
blood_suger = st.number_input("Blood sugar", min_value=0)
ck_mb = st.number_input("CK-MB", min_value=0)
troponin = st.number_input("Troponin", min_value=0)

if st.button("Predict"):
    # st.success(f"Predicted {prediction}")')
    st.write("button clicked")
