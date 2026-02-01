# GridMind  
**AI-powered Grid Anomaly Explanation & Decision Support System**

## Project Vision

Modern power grids are becoming increasingly complex due to the rapid integration of renewable energy sources such as wind and solar.  
While large volumes of operational data are available, **grid operators still struggle to quickly understand *why* anomalies happen and *what actions* should be taken**.

**GridMind** is an AI-driven decision support system designed to:
- Detect anomalies in power grid time-series data
- Explain their likely root causes using domain knowledge
- Provide actionable, human-readable operational recommendations

Rather than being just a prediction or alerting tool, GridMind acts as a **junior grid analyst**, supporting engineers and operators in real-world decision-making.

---

## Potential Value

GridMind addresses key challenges in the energy sector:

- **Reduced incident response time**  
  Automated anomaly explanations reduce the need for manual investigation.

- **Knowledge preservation**  
  Encodes expert knowledge and operational guidelines into an AI-accessible system.

- **Improved renewable integration**  
  Helps operators understand volatility caused by weather-driven generation.

- **Consistent decision-making**  
  Provides standardized explanations and recommendations across teams.

---

## Target Use Case

- Transmission and distribution system operators (e.g. Dutch and EU grid operators)
- Energy consultants and analysts
- Control room operators supporting real-time grid operations

---

## System Overview

GridMind combines **time-series machine learning**, **explainable AI**, and **LLM-based Retrieval-Augmented Generation (RAG)** into a single system.

---

## Project Structure
![Workflow](assets/project_architecture.png)

---

## Core Components

### 1. Data Ingestion
- Collects and validates power grid and weather data
- Supports ENTSO-E and KNMI public datasets
- Ensures reproducibility and traceability

### 2. Time-Series Machine Learning
- Short-term forecasting models
- Residual-based anomaly detection
- Designed for robustness and interpretability

### 3. Explainability Engine
- Identifies contributing factors behind anomalies
- Bridges raw model outputs and domain reasoning

### 4. LLM-based RAG System
- Retrieves relevant grid rules, incidents, and documentation
- Generates structured explanations and operational suggestions
- Ensures responses are grounded in verified sources

### 5. API & Deployment
- RESTful API built with FastAPI
- Containerized with Docker
- Designed for cloud-native deployment

---

## Tech Stack

- **Language**: Python
- **Data & ML**: pandas, scikit-learn, PyTorch (optional)
- **Explainability**: SHAP, rule-based logic
- **LLM & NLP**: OpenAI-compatible LLMs, embeddings, vector databases
- **Backend**: FastAPI
- **MLOps**: Docker, GitHub Actions (planned)
- **Cloud**: Azure / GCP compatible

---

## Project Status

**Work in progress**  
This project is being developed incrementally, following a production-oriented and consultancy-style workflow.

---



