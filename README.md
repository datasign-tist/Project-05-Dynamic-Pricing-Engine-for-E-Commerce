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
- Encoded promotions, product categories, and competitor IDS

### ✅ ETL Orchestration
- Built a modular ETL pipeline in `etl_pipeline.py`
- Automated workflow using Airflow DAG (coming in Phase 4)

------------------------------------------------------------------------------------------------------------
## Steps to construct the folder structure and required files.

1. Create the template.py file --> This will help us avoid manually adding all the required folders and files.
2. Create the requirements.txt ( pip install—r requirements.txt) --> This file contains all the required libraries, and it will install them in one go.
3. Create the setup.py --> requirement.txt file. It will look for this file to install our package as a local package.
4. Add the Logging Functionality in the constructor file inside src/project_name --> This custom logging function will help us debug and track our code when deployed on remote servers.
5. Add the common.py file inside the  utils --> The Utility file helps us reuse the function ( Professional OOps Programming ). We have used the config-box and ensure-annotation for better standard coding.

------------------------------------------------------------------------------------------------------------

## Now, we will follow the workflow process for each data science project step.

### The Workflow Structure :
A.  Update config.yaml  
B.  Update schema.yaml  
C.  Update params.yaml  
D.  Update the entity  
E.  Update the configuration manager in the src config  
F.  Update the components  
G.  Update the pipeline  
H.  Update the main.py  
I.  Update the app.py  

We will perform all the above operations for each data-science project stage.  
We will perform modular coding (OOP Programming).

------------------------------------------------------------------------------------------------------------
