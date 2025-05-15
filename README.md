# Dynamic Pricing Engine for E-Commerce (End-to-End)

A production-grade machine learning system that dynamically adjusts product prices based on historical demand, competitor pricing, inventory, and user behavior using time-series forecasting and cloud-native MLOps practices.

---

## 🚀 Skills & Tools Required

| Skill/Tool            | Purpose                                  |
|-----------------------|------------------------------------------|
| Python (OOP)          | Modular, reusable code structure         |
| Pandas, NumPy         | Data manipulation & feature generation   |
| AWS S3                | Raw & processed data storage             |
| Airflow               | Automated & scheduled ETL pipelines      |
| Great Expectations    | Data validation                          |
| YAML/JSON             | Configuration & schema definitions       |
| Logging               | Debugging & observability                |
| Unit Testing (pytest) | Test pipeline logic                      |

---

## 📦 Phase 2 – Data Collection & Preparation

In this phase, we focused on building the foundational data pipeline to support dynamic pricing. Here’s what we implemented:

### ✅ Data Sourcing
- Built OOP-based data connectors for sales and inventory data.
- Simulated competitor pricing and promotion datasets.

### ✅ Data Schema & Validation
- Defined schemas using YAML to ensure column consistency and data types.
- Integrated **Great Expectations** for automated checks like nulls, ranges, and anomalies.

### ✅ Feature Engineering
- Created lag features (e.g., 7-day, 30-day sales)
- Added seasonality indicators (day of week, holidays)
- Encoded promotions, product categories, and competitor IDs

### ✅ ETL Orchestration
- Built a modular ETL pipeline in `etl_pipeline.py`
- Automated workflow using Airflow DAG (coming in Phase 4)

### 📁 Output
All cleaned and feature-rich data is exported to:

---
