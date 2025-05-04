import pyrootutils
import streamlit as st

pyrootutils.setup_root(
    search_from=__file__,
    indicator=[".git", "pyproject.toml"],
    pythonpath=True,
    dotenv=True,
)

from api_model import HeartAttackData  # noqa: E402

from src.entity.config_entity import HeartAttackPredictorConfig  # noqa: E402
from src.pipline.prediction_pipeline import HeartAttackClaassifier  # noqa: E402
from src.pipline.training_pipeline import TrainingPipeline  # noqa: E402


def ui() -> None:
    st.set_page_config(page_title="Heart Attack Predictor", page_icon="❤️", layout="centered")

    # st.image("your_logo.png", width=80)
    st.title("Heart Attack Predictor")
    st.markdown("Enter your details below to assess your risk.")
    with st.form("risk_form"):
        co1, col2 = st.columns(2)
        with co1:
            age = st.number_input("Age", min_value=14, max_value=130)
            gender = st.selectbox("Gender", ["Male", "Female"])
            heart_rate = st.number_input("Heart Rate", min_value=20, max_value=200)
        with col2:
            systolic_bp = st.number_input("Systolic Blood Pressure", min_value=30, max_value=250)
            diastolic_bp = st.number_input("Diastolic Blood Pressure", min_value=30, max_value=250)
            blood_suger = st.number_input("Blood sugar", min_value=30, max_value=550)
            ck_mb = st.number_input("CK-MB", min_value=0, max_value=300)
            troponin = st.number_input("Troponin", min_value=0, max_value=15)

        if st.form_submit_button("Predict Risk"):
            input_data = {
                "gender": 0 if gender == "Female" else 1,
                "age": age,
                "heart_rate": heart_rate,
                "systolic_blood_pressure": systolic_bp,
                "diastolic_blood_pressure": diastolic_bp,
                "blood_sugar": blood_suger,
                "ck_mb": ck_mb,
                "troponin": troponin,
            }
            data = HeartAttackData(**input_data)
            df = data.to_dataframe()
            classifier = HeartAttackClaassifier(prediction_pipeline_config=HeartAttackPredictorConfig())
            prediction = classifier.predict(df)[0]
            st.success(f"Predicted: {'Heart Attack' if prediction == 1 else 'No Heart Attack'}")
    with st.sidebar:
        st.header("Admin Tools")
        if st.button("Retrain Model"):
            training_pipeline = TrainingPipeline()
            training_pipeline.run_pipeline()
            st.success("Model retrained successfully!")


if __name__ == "__main__":
    ui()
# import streamlit as st

# st.set_page_config(page_title="Heart Attack Predictor", page_icon="❤️", layout="centered")

# st.image("your_logo.png", width=80)
# st.title("Heart Attack Predictor")
# st.markdown("Enter your details below to assess your risk.")

# with st.form(key="risk_form"):
#     col1, col2 = st.columns(2)
#     with col1:
#         age = st.number_input("Age", min_value=14, max_value=130, help="Your age in years")
#         gender = st.selectbox("Gender", ["Male", "Female"])
#         heart_rate = st.number_input("Heart Rate", min_value=20, max_value=200)
#     with col2:
#         systolic_bp = st.number_input("Systolic BP", min_value=30, max_value=250)
#         diastolic_bp = st.number_input("Diastolic BP", min_value=30, max_value=250)
#         blood_sugar = st.number_input("Blood Sugar", min_value=30, max_value=550)
#         ck_mb = st.number_input("CK-MB", min_value=0, max_value=300)
#         troponin = st.number_input("Troponin", min_value=0, max_value=15)
#     submitted = st.form_submit_button("Predict Risk")
