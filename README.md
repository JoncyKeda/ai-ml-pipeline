# ⚙️ AI ML Pipeline Orchestrator (End-to-End MLOps System)

---

## 📌 Overview

This project implements a **complete machine learning pipeline** that automates the entire workflow from raw data to a trained model.

Unlike basic ML projects, this system follows a **pipeline-based architecture**, similar to real-world production systems used in companies.

The pipeline performs:

* Data ingestion
* Data preprocessing
* Model training
* Model evaluation
* Model saving

---

## 🎯 Problem Statement

The system predicts whether a loan application should be approved or rejected based on applicant details like income, credit score, and employment history.

---

## 📊 Dataset Description

The dataset simulates a **loan approval system**.

### Features:

* **age** → Applicant age
* **income** → Annual income
* **credit_score** → Creditworthiness
* **loan_amount** → Requested loan
* **employment_years** → Work experience

### Target:

* **label**

  * 1 → Loan Approved
  * 0 → Loan Rejected

---

## 🧠 Tech Stack

* Python
* Pandas
* Scikit-learn
* Joblib

---

## 🏗️ Architecture

```text
Data → Preprocessing → Training → Evaluation → Model Storage
```

---

## 📂 Project Structure

```text
ai-ml-pipeline/
│
├── main.py
├── pipeline/
├── data/
├── models/
```

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python main.py
```

---

## 📊 Output Example

```
Model Accuracy: 0.85
```

---

## 🧠 How It Works

1. Loads dataset
2. Splits into train/test
3. Trains Random Forest model
4. Evaluates performance
5. Saves trained model

---

## 🎯 Use Cases

* Loan approval systems
* Risk prediction
* Financial analytics
* ML workflow automation

---

### 👨‍💻 Author: 
**Joncy Keda - AI Developer**
