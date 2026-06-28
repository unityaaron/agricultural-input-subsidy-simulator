# 🌾 Sub-Saharan Smallholder Input Subsidy Evaluation & Profitability Simulator
### Developed by Unity Aaron

An end-to-end data engineering and predictive machine learning system designed to simulate input subsidy viability, capture market price volatility, and isolate agricultural intervention causality. This system pairs a robust statistical inference engine with an optimized Random Forest Regressor to serve real-time microeconomic policy simulations for smallholder farming systems in Edo State, Nigeria.

🔗 **Live Interactive Web Application:** [Click Here to Launch the Policy Simulator](PASTE_YOUR_NEW_STREAMLIT_URL_HERE)

---

## 📊 Core Architecture & Analytical Modules
The repository is engineered systematically to separate experimental data science from live software deployment:

* **`statistical_inference/`**: Houses multiple OLS regression modeling used to isolate the true treatment effects of agricultural extension training while strictly controlling for confounding physical resource factors (Farm Size, Input Volumes) to address baseline asset bias.
* **`machine_learning_model/`**: Contains the predictive engines, featuring an optimized Random Forest Regressor model, cross-validation scripts, and frozen deployment assets (`.pkl`).
* **`run_pipeline.py`**: An automated, single-click ETL pipeline that ingests raw micro-level operational spreadsheets, executes feature calculations, and exports live predictions.
* **`app.py`**: A public-facing web interface that couples the ML yield prediction backend with real-time financial cost-benefit matrix formulas to simulate fertilizer profitability shocks.

---

## 🧠 Strategic Research Insights & Metrics

### 1. Causal Inference Verification
Through independent T-tests and multiple linear regression controls, the system isolates training as a primary causal driver ($p < 0.05$), unlocking a **15.68 to 16.5 percentage point increase** in yield gains, while baseline fertilizer volume alone proved statistically insignificant under prevailing unmanaged field constraints.

### 2. Feature Interaction Optimization
By formulating an engineered interaction variable ($\text{Fertilizer Used} \times \text{Training Attended}$), the Random Forest model captured a **40.5% Feature Importance weight**, mathematically demonstrating that input resource efficiency is structurally unlocked only when coupled with extension education.

### 3. Model Generalization & Stability
To guarantee prediction stability across varying sub-Saharan smallholder landscapes, the predictive architecture was validated using a strict **5-Fold Cross-Validation** protocol:
* **Out-of-Sample Performance:** Achieved a cross-validated **Average Mean Absolute Error (MAE) of 2.41%**.
* **System Consistency:** Recorded an exceptionally low **Standard Deviation of 0.37%**, proving high resilience against data overfitting.

---

## 🛠️ Repository Deployment & Local Execution

This repository can be cloned, initialized, and pushed to your dedicated GitHub environment using the following command structures:

### 1. Primary Repository Setup & Git Push Sequence
```bash
git init
git add .
git commit -m "Initial commit: Production agricultural policy simulation pipeline"
git branch -M master
git remote add origin [https://github.com/unityaaron/agricultural-input-subsidy-simulator.git](https://github.com/unityaaron/agricultural-input-subsidy-simulator.git)
git push -u origin master