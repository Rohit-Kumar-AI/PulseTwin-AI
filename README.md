# PulseTwin AI
### A Digital Twin Proof of Concept for Cardiovascular Wellness Monitoring

**Happiest Health CRP Digital Twin Challenge 2026**

PulseTwin AI is an educational healthcare technology prototype that demonstrates how synthetic patient profiles, simulated wearable measurements, and machine learning can be combined in an interactive cardiovascular wellness dashboard.

The project explores a simplified Digital Twin workflow using Python, Streamlit, and scikit-learn. It allows users to interact with fictional patient profiles, explore simulated physiological trends, and examine illustrative machine-learning outputs.

> **Disclaimer:** PulseTwin AI is an educational proof of concept, not a clinically validated medical system. Its synthetic data, predictions, and rule-based observations must not be used for diagnosis, treatment, or real-world medical decision-making.

---

## Table of Contents

- [Project Overview](#1-project-overview)
- [Problem Statement](#2-problem-statement)
- [Proposed Solution](#3-proposed-solution)
- [Key Features](#4-key-features)
- [Healthcare Use Case](#5-healthcare-use-case)
- [Technology Stack](#6-technology-stack)
- [AI and Machine Learning](#7-ai-and-machine-learning)
- [Digital Twin Architecture](#8-digital-twin-architecture)
- [Project Structure](#9-project-structure)
- [Installation and Setup](#10-installation-and-setup)
- [Running the Application](#11-running-the-application)
- [Demonstration Video](#12-demonstration-video)
- [Team Details](#13-team-details)
- [Project Information](#14-project-information)
- [Limitations and Responsible Use](#15-limitations-and-responsible-use)
- [Future Scope](#16-future-scope)
- [Presentation and Architecture Documentation](#17-presentation-and-architecture-documentation)
- [License](#18-license)
- [Acknowledgments](#19-acknowledgments)

---

## 1. Project Overview

PulseTwin AI is a student-developed Digital Twin proof of concept designed to demonstrate a simulated cardiovascular wellness monitoring workflow.

The application combines fictional patient profiles, synthetic physiological measurements, a demonstration machine-learning model, and interactive data visualizations in a single dashboard.

Users can modify example patient measurements, examine illustrative model outputs, explore simulated seven-day wearable trends, and view simple rule-based observations.

The project demonstrates how multiple software components can work together to represent a simplified digital counterpart of a fictional patient.

### Project Goals

- Demonstrate a simplified healthcare Digital Twin architecture.
- Explore synthetic physiological data generation.
- Implement a basic machine-learning workflow.
- Visualize simulated wearable measurements.
- Present patient measurements through an interactive dashboard.
- Explore feature importance and rule-based observations.
- Demonstrate responsible use of AI in a healthcare-oriented prototype.

The application uses synthetic data and does not require real patient records or live medical-device connections.

---

## 2. Problem Statement

Healthcare monitoring can involve multiple physiological measurements, including blood pressure, resting heart rate, sleep duration, physical activity, and blood oxygen saturation.

Presenting these measurements together in an understandable and interactive interface can be challenging.

A Digital Twin-style application provides an opportunity to explore how a digital representation of a person could organize measurements, display trends, and support experimentation with analytical models.

PulseTwin AI addresses this educational problem by demonstrating an integrated dashboard that combines synthetic patient data, simulated wearable measurements, machine-learning experimentation, and simple observation rules.

The project is a software demonstration rather than a solution validated for clinical use.

---

## 3. Proposed Solution

PulseTwin AI implements a simplified Digital Twin workflow through the following components:

1. **Patient Profile:** An interactive representation of a fictional patient.
2. **Synthetic Data Generation:** Programmatically generated physiological measurements for experimentation.
3. **Machine Learning:** A Random Forest classifier trained on synthetic records and illustrative labels.
4. **Interactive Dashboard:** Visual presentation of patient measurements and model outputs.
5. **Wearable Simulation:** A seven-day timeline of fictional physiological measurements.
6. **Rule-Based Observations:** Demonstration rules that identify selected measurement conditions.
7. **Data Export:** CSV export of synthetic records, where implemented.

Together, these components demonstrate the software workflow of a basic healthcare-oriented Digital Twin.

---

## 4. Key Features

### Interactive Patient Profile

Modify selected measurements for a fictional patient and explore how the dashboard responds to changes in the input values.

### Synthetic Dataset Generation

Generate fictional physiological records for machine-learning experimentation without requiring identifiable patient information.

### Random Forest Classification

Use a Random Forest classifier from scikit-learn to demonstrate a supervised machine-learning workflow using synthetic training data.

### Illustrative Model Output

Display the classifier's output for the selected synthetic patient profile.

The output represents the model's response to synthetic training data and is not a clinically meaningful risk estimate.

### Feature-Importance Visualization

Explore the relative importance assigned to input features by the trained Random Forest model.

Feature importance is a model-specific measure and does not establish causation or medical significance.

### Seven-Day Simulated Wearable Timeline

Visualize fictional physiological measurements over a simulated seven-day period.

The timeline demonstrates how wearable-style data might be organized and displayed in a monitoring interface.

### Rule-Based Observations

Display simple observations based on predefined measurement thresholds.

These rules demonstrate basic application logic and are not medical guidelines.

### Synthetic Data Export

Export generated synthetic records to CSV where the application implements this functionality.

---

## 5. Healthcare Use Case

### Cardiovascular Wellness Monitoring

PulseTwin AI demonstrates a simulated cardiovascular wellness monitoring scenario using the following example inputs:

| Input Feature | Description |
|---|---|
| Age | Age of the fictional patient |
| Systolic Blood Pressure | Example systolic blood pressure measurement |
| Body Mass Index (BMI) | Body mass index value |
| Resting Heart Rate | Example resting heart rate |
| Heart-Rate Variability (HRV) | Example heart-rate variability measurement |
| Sleep Duration | Simulated daily sleep duration |
| Daily Steps | Simulated physical activity |
| Peripheral Oxygen Saturation (SpO₂) | Example blood oxygen saturation measurement |

These inputs are used to demonstrate interactive data handling, visualization, and model experimentation.

### Example Workflow

1. Open the dashboard.
2. Select or modify a fictional patient profile.
3. Explore the physiological measurements.
4. View the illustrative machine-learning output.
5. Examine feature importance.
6. Explore simulated seven-day wearable trends.
7. Review rule-based observations.
8. Export synthetic records if the export functionality is available.

**Safety note:** This workflow does not diagnose cardiovascular disease, establish an individual's actual cardiovascular risk, or recommend treatment.

---

## 6. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic and data processing |
| Streamlit | Interactive web dashboard |
| Pandas | Data manipulation and tabular processing |
| NumPy | Numerical computations and synthetic-data generation |
| scikit-learn | Random Forest classification and model evaluation |
| Altair | Interactive data visualization through Streamlit |

### Development Environment

The project is designed to run locally on a Windows computer.

Recommended development tools:

- Windows 10 or Windows 11
- Python
- Visual Studio Code
- Git
- PowerShell or the VS Code integrated terminal

---

## 7. AI and Machine Learning

### Model

**Random Forest Classifier**

### Framework

**scikit-learn**

### Input Features

The demonstration model uses eight example features:

1. Age
2. Systolic blood pressure
3. Body mass index
4. Resting heart rate
5. Heart-rate variability
6. Sleep duration
7. Daily step count
8. Peripheral oxygen saturation

### Training Data

The application generates synthetic records for model experimentation.

These records are not verified clinical observations and should not be interpreted as representative of a real patient population.

### Target Label

The classification target is generated using an illustrative programmatic formula.

It is not derived from verified medical diagnoses, validated clinical datasets, or real patient outcomes.

Consequently, the model learns patterns introduced by the synthetic labeling process rather than clinically established relationships.

### Model Output

The classifier produces an illustrative classification based on the synthetic training data and the selected input measurements.

This output demonstrates the mechanics of a machine-learning prediction workflow.

It is not a diagnosis, a validated cardiovascular risk score, or a prediction of an actual medical outcome.

### Feature Importance

Feature importance can help demonstrate how a tree-based model distributes importance across its input variables.

However, these values:

- Depend on the training data and model configuration.
- Do not establish causal relationships.
- Do not prove that a feature is clinically important.
- May reflect patterns introduced by the synthetic labeling formula.

### Evaluation Limitations

Any reported accuracy or other evaluation metric measures agreement with the synthetic labels under the selected evaluation procedure.

It does not demonstrate clinical accuracy, diagnostic performance, generalization to real patients, or real-world predictive validity.

No claims of clinical validation are made.

---

## 8. Digital Twin Architecture

PulseTwin AI uses a simplified architecture to demonstrate how a fictional patient profile, synthetic data, a machine-learning component, and an interactive dashboard can work together.

### Primary Data Flow

```text
        Fictional Patient Profile
                  |
                  v
         Patient Input Values
                  |
                  v
       Synthetic Data Processing
                  |
                  v
       Random Forest Classifier
                  |
                  v
        Illustrative Model Output
                  |
                  v
        Streamlit Dashboard
```

### Simulated Wearable Data Flow

```text
      Synthetic Physiological Data
                  |
                  v
       Seven-Day Simulated Timeline
                  |
                  v
         Interactive Visualizations
                  |
                  v
        Rule-Based Observations
```

### Main Components

**1. User Interface**

Streamlit provides the interactive dashboard for displaying measurements, accepting user inputs, and presenting results.

**2. Synthetic Data Generator**

Python, NumPy, and Pandas support the generation and processing of fictional physiological records.

**3. Machine-Learning Component**

A scikit-learn Random Forest classifier demonstrates supervised learning using synthetic data and illustrative labels.

**4. Visualization Component**

Interactive charts present simulated wearable measurements and model feature importance.

**5. Observation Component**

Predefined rules generate illustrative observations for selected measurement values.

**6. Export Component**

CSV export supports downloading synthetic records if implemented in the application.

### Architecture Documentation

See [`ARCHITECTURE.md`](ARCHITECTURE.md) for additional information about the system architecture and data flow.

The architecture PDF is intended to be provided as:

`PulseTwinAI_Architecture.pdf`

Include this PDF in the repository before claiming it is available.

---

## 9. Project Structure

The core project structure is expected to resemble the following:

```text
PulseTwin-AI/
├── app.py
├── requirements.txt
├── README.md
├── ARCHITECTURE.md
├── LICENSE
├── .gitignore
└── .streamlit/
    └── config.toml
```

Optional submission documents:

```text
PulseTwinAI_Architecture.pdf
PulseTwinAI_Presentation.pptx
```

The actual repository structure may differ depending on the implemented application.

Only list files as included deliverables when they actually exist in the repository.

---

## 10. Installation and Setup

Follow these steps to run PulseTwin AI locally on Windows.

### Prerequisites

Install the following tools:

- Python
- Git
- Visual Studio Code

Internet access is required to install dependencies.

### Step 1: Clone the Repository

Open PowerShell or the VS Code integrated terminal.

Run:

```powershell
git clone https://github.com/Rohit-Kumar-AI/PulseTwin-AI.git
```

Navigate to the project directory:

```powershell
cd PulseTwin-AI
```

### Step 2: Create a Virtual Environment

```powershell
py -m venv .venv
```

A virtual environment helps isolate the project's Python dependencies from other Python projects.

### Step 3: Install Dependencies

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
```

Install the packages listed in `requirements.txt`:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### Step 4: Verify the Installation

Check the Python version:

```powershell
.\.venv\Scripts\python.exe --version
```

Check whether Streamlit is available:

```powershell
.\.venv\Scripts\python.exe -m streamlit --version
```

### Step 5: Run the Application

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

### Step 6: Open the Dashboard

Streamlit will display a local address in the terminal.

The default address is typically:

```text
http://localhost:8501
```

Open the displayed address in your web browser.

---

## 11. Running the Application

Once the application starts:

1. Open the local dashboard in your browser.
2. Explore the fictional patient profile.
3. Modify the available physiological measurements.
4. Review the illustrative model output.
5. Examine the feature-importance visualization.
6. Explore the simulated wearable timeline.
7. Review the rule-based observations.
8. Test synthetic data export if available.

The available controls and visualizations depend on the application's implementation.

### Troubleshooting

**The `py` command is not recognized**

Install Python for Windows and ensure the Python launcher is available.

**Dependency installation fails**

Check the terminal output for missing packages, Python version incompatibilities, or network errors.

**The dashboard does not open**

Check the terminal for application errors and open the exact local address displayed by Streamlit.

**Port 8501 is already in use**

Stop the other Streamlit process or specify another available port:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py --server.port 8502
```

---

## 12. Demonstration Video

**Expected format:** Unlisted YouTube video.

**Target duration:** 15–20 minutes, according to the challenge submission checklist.

**Demo Video URL:** To be added after recording and uploading the final demonstration.

### Suggested Demonstration Structure

1. Project introduction and problem statement.
2. Overview of the Digital Twin concept.
3. Healthcare use case and proposed solution.
4. System architecture and technology stack.
5. Interactive patient profile.
6. Synthetic-data generation workflow.
7. Random Forest training and illustrative output.
8. Feature-importance visualization.
9. Seven-day simulated wearable timeline.
10. Rule-based observations and CSV export, where supported.
11. Limitations and responsible use.
12. Future improvements and conclusion.

Before submission, upload the actual demonstration video and replace this section with its working URL.

Do not submit the placeholder as a completed video link.

---

## 13. Team Details

| Field | Details |
|---|---|
| Team Name | Rohit Kumar |
| Team Leader | Rohit Kumar |
| Developer | Rohit Kumar |
| Team Members | Rohit Kumar |
| College / University | Pranveer Singh Institute of Technology (PSIT) |
| Location | Kanpur, Uttar Pradesh, India |
| Incubator Information | Not applicable unless associated with an incubator |

---

## 14. Project Information

| Field | Details |
|---|---|
| Project Title | PulseTwin AI |
| Challenge | Happiest Health CRP Digital Twin Challenge 2026 |
| Project Type | Healthcare Technology / Digital Twin / AI and Machine Learning |
| Developer | Rohit Kumar |
| Programming Language | Python |
| Dashboard Framework | Streamlit |
| Machine-Learning Model | Random Forest Classifier |
| Training Data | Synthetic data |
| GitHub Profile | [Rohit Kumar AI](https://github.com/Rohit-Kumar-AI) |
| Project Repository | [PulseTwin AI](https://github.com/Rohit-Kumar-AI/PulseTwin-AI) |
| LinkedIn | [Rohit Kumar](https://www.linkedin.com/in/rohit-k-ai) |
| License | MIT |

---

## 15. Limitations and Responsible Use

PulseTwin AI is an educational proof of concept.

The following limitations are important:

- **Synthetic data:** Patient profiles and generated measurements are fictional.
- **Illustrative labels:** Model targets are generated using a programmatic formula rather than verified clinical outcomes.
- **No clinical validation:** The model has not been validated for medical use.
- **Limited generalizability:** Performance on synthetic data does not establish performance on real-world patient data.
- **No diagnostic capability:** The application is not a medical diagnostic system.
- **No treatment recommendations:** The application does not establish appropriate medical treatment.
- **Illustrative rules:** Threshold-based observations are demonstration logic, not clinical guidelines.
- **No confirmed live device integration:** The prototype does not claim live wearable-device connectivity.
- **No confirmed hospital integration:** The prototype does not claim integration with hospital information systems.
- **No real-patient prediction claims:** The project does not establish that the model can predict cardiovascular disease in actual patients.

### Responsible AI Considerations

Any future clinical application would require appropriate and ethically sourced data, expert clinical review, rigorous independent validation, privacy and security safeguards, bias assessment, and applicable regulatory review.

The prototype should be used only for educational experimentation and software demonstration.

---

## 16. Future Scope

Potential improvements include:

- Integration with authorized wearable-device data sources.
- More comprehensive simulated patient timelines.
- Secure data storage and access controls.
- Improved testing and reproducibility.
- Model comparison and explainability experiments.
- Evaluation using suitable, ethically sourced clinical datasets.
- Assessment of bias and performance across relevant populations.
- Clinical expert review before any consideration of medical use.
- Appropriate regulatory and privacy assessments for future real-world applications.

These are proposed improvements, not claims about existing functionality.

---

## 17. Presentation and Architecture Documentation

The project may include the following supplementary materials:

### Architecture Document

**Filename:** `PulseTwinAI_Architecture.pdf`

The document should explain the architecture, system components, and data flow.

### Project Presentation

**Filename:** `PulseTwinAI_Presentation.pptx`

The presentation should cover:

- Problem statement.
- Proposed solution.
- Healthcare use case.
- Digital Twin architecture.
- Technology stack.
- Synthetic data generation.
- Machine-learning workflow.
- Demonstration results and visualizations.
- Limitations and responsible use.
- Future scope.

Ensure both files are present in the public repository before describing them as completed deliverables.

---

## 18. License

This project is intended to be distributed under the MIT License.

See [`LICENSE`](LICENSE) for the applicable terms.

Ensure the repository contains the correct license file before claiming the project is distributed under this license.

---

## 19. Acknowledgments

PulseTwin AI is developed as a student proof of concept for the Happiest Health CRP Digital Twin Challenge 2026.

The project explores the educational application of synthetic physiological data, machine-learning experimentation, and interactive visualization within a simplified healthcare Digital Twin workflow.

It demonstrates how software components can be combined to create an interactive prototype while emphasizing the limitations of synthetic data and the importance of responsible AI in healthcare.

---

**Project:** PulseTwin AI  
**Developer:** Rohit Kumar  
**Institution:** Pranveer Singh Institute of Technology (PSIT)  
**Challenge:** Happiest Health CRP Digital Twin Challenge 2026  
**License:** MIT  
**Status:** Student Proof of Concept
