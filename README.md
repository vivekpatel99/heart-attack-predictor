# heart-attack-predictor-end-to-end-ml-project

## About Dataset

### Context

The [Heart Attack Risk Prediction Dataset](https://www.kaggle.com/datasets/iamsouravbanerjee/heart-attack-prediction-dataset/data) serves as a valuable resource for delving into the intricate dynamics of heart health and its predictors. Heart attacks, or myocardial infractions, continue to be a significant global health issue, necessitating a deeper comprehension of their precursors and potential mitigating factors. This dataset encapsulates a diverse range of attributes including age, cholesterol levels, blood pressure, smoking habits, exercise patterns, dietary preferences, and more, aiming to elucidate the complex interplay of these variables in determining the likelihood of a heart attack. By employing predictive analytics and machine learning on this dataset, researchers and healthcare professionals can work towards proactive strategies for heart disease prevention and management. The dataset stands as a testament to collective efforts to enhance our understanding of cardiovascular health and pave the way for a healthier future.

### Content

This synthetic dataset provides a comprehensive array of features relevant to heart health and lifestyle choices, encompassing patient-specific details such as age, gender, cholesterol levels, blood pressure, heart rate, and indicators like diabetes, family history, smoking habits, obesity, and alcohol consumption. Additionally, lifestyle factors like exercise hours, dietary habits, stress levels, and sedentary hours are included. Medical aspects comprising previous heart problems, medication usage, and triglyceride levels are considered. Socioeconomic aspects such as income and geographical attributes like country, continent, and hemisphere are incorporated. The dataset, consisting of 8763 records from patients around the globe, culminates in a crucial binary classification feature denoting the presence or absence of a heart attack risk, providing a comprehensive resource for predictive analysis and research in cardiovascular health.

### Dataset Glossary (Column-wise)

- **Patient ID** - Unique identifier for each patient
- **Age** - Age of the patient
- **Sex** - Gender of the patient (Male/Female)
- **Cholesterol** - Cholesterol levels of the patient
- **Blood Pressure** - Blood pressure of the patient (systolic/diastolic)
- **Heart Rate** - Heart rate of the patient
- **Diabetes** - Whether the patient has diabetes (Yes/No)
- **Family History** - Family history of heart-related problems (1: Yes, 0: No)
- **Smoking** - Smoking status of the patient (1: Smoker, 0: Non-smoker)
- **Obesity** - Obesity status of the patient (1: Obese, 0: Not obese)
- **Alcohol Consumption** - Level of alcohol consumption by the patient (None/Light/Moderate/Heavy)
- **Exercise Hours Per Week** - Number of exercise hours per week
- **Diet** - Dietary habits of the patient (Healthy/Average/Unhealthy)
- **Previous Heart Problems** - Previous heart problems of the patient (1: Yes, 0: No)
- **Medication Use** - Medication usage by the patient (1: Yes, 0: No)
- **Stress Level** - Stress level reported by the patient (1-10)
- **Sedentary Hours Per Day** - Hours of sedentary activity per day
- **Income** - Income level of the patient
- **BMI** - Body Mass Index (BMI) of the patient
- **Triglycerides** - Triglyceride levels of the patient
- **Physical Activity Days Per Week** - Days of physical activity per week
- **Sleep Hours Per Day** - Hours of sleep per day
- **Country** - Country of the patient
- **Continent** - Continent where the patient resides
- **Hemisphere** - Hemisphere where the patient resides
- **Heart Attack Risk** - Presence of heart attack risk (1: Yes, 0: No)

## ✨ Key Features

- **Modular Design:** using SW development best practices (OOP)
- **Configuration Management:** Uses [Hydra](https://hydra.cc/docs/intro/) for flexible configuration via YAML files and command-line overrides.

## 🛠️ Technologies Used

- **Python:** Core programming language.
- **Jupyter Notebook:** For exploratory data analysis (EDA), model development, and training.
- **AWS:** `IAM` and `S3 Bucket` for storing model artifacts.
- **Docker:** Containerization for consistent environment.
- **VS Code Dev Containers:** Development environment setup.

## Project Structure

## 🔧 Setup & Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/vivekpatel99/heart-attack-predictor-end-to-end-ml-project.git
   cd heart-attack-predictor-end-to-end-ml-project
   ```

2. **Install VS Code Extensions:**

   - Docker (`ms-azuretools.vscode-docker`)
   - Dev Containers (`ms-vscode-remote.remote-containers`)

3. **Set up Environment Variables:**

   - Create a `.env` file in the project root directorusing SW development best practices (OOP)y.
   - Add your Roboflow API key. This is needed if you plan to download datasets directly via Roboflow scripts (if applicable).

   ```dotenv
   # .env
   DB_NAME = ""
   COLLECTION_NAME = ""
   DB_CONNECTION_URL = ""
   AWS_ACCESS_KEY_ID = ""
   AWS_SECRET_ACCESS_KEY = ""
   REGION_NAME = ""
   APP_HOST = ""
   APP_PORT = ""
   ```

   - *Note: The `.env` file is gitignored for security.*

4. **Build and Open in Dev Container:**

   - Open the cloned repository folder in VS Code.
   - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on macOS).
   - Type and select `Dev Containers: Rebuild and Reopen in Container`.
   - This will build the Docker image and start the development container. VS Code will automatically connect to it.

5. **Install Dependencies (inside the container):**

   - Once the container is running, open a terminal within VS Code (`Terminal > New Terminal`).
   - Install the required Python packages:

   ```bash
   uv add -r requirements.txt
   ```

## Data Preparation

## 🏋️ Training

## Models

## 📈 Results & Visualizations

**Validation Metrics:**

## 🖥️ Hardware Specifications

NOTE: To enhance ball detection accuracy, the YOLOv12L model was trained using an image size of 1280x1280. Training was performed using Lightning Studio to ensure sufficient GPU memory was available. The project was developed and tested on the following hardware:
it was developed and tested on the following hardware:

- **CPU:** AMD Ryzen 5900X
- **GPU:** NVIDIA GeForce RTX 3080 (10GB VRAM)
- **RAM:** 32 GB DDR4

While these specifications are recommended for optimal performance, the project can be adapted to run on systems with less powerful hardware.

## 📚 Reference

1. [Vehicle Insurance Data Pipeline](https://github.com/vikashishere/YT-MLops-Proj1/tree/main)
