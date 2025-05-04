# heart-attack-predictor-end-to-end-ml-project

## About Dataset

### Context

The [Heart Attack Risk Prediction Dataset](https://www.kaggle.com/datasets/sukhmandeepsinghbrar/heart-attack-dataset/data) were collected at Zheen hospital in Erbil, Iraq, from January 2019 to May 2019. The attributes of this dataset are: age, gender, heart rate, systolic blood pressure, diastolic blood pressure, blood sugar, ck-mb and troponin with negative or positive output. According to the provided information, the medical dataset classifies either heart attack or none. The gender column in the data is normalized: the male is set to 1 and the female to 0. The glucose column is set to 1 if it is > 120; otherwise, 0. As for the output, positive is set to 1 and negative to 0.

### Dataset Glossary (Column-wise)

- **Age** - Age of the patient
- **Gender** - Gender of the patient (1-Male, 0-Female)
- **Heart Rate** - Heart rate of the patient
- **Blood Pressure** - Blood pressure of the patient (systolic and diastolic)
- **Blood Sugar** - Blood sugar levels of the patient
- **CK-MB** - Concentration of the CK-MB biomarker
- **Troponin** - Concentration of the Troponin biomarker
- **Diagnostic Outcome** - Diagnostic outcome for the patient

## ✨ Key Features

- **Modular Design:** using SW development best practices (OOP)
- **Configuration Management:** Uses [Hydra](https://hydra.cc/docs/intro/) for flexible configuration via YAML files and command-line overrides.

## 🛠️ Technologies Used

- **Python:** Core programming language.
- **Jupyter Notebook:** For exploratory data analysis (EDA), model development, and training.
- **AWS:** `IAM` and `S3 Bucket` for storing and loading model artifacts.
- **FastAPI:** for interacting with the model
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
