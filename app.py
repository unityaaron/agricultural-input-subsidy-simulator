# =====================================================================
# SYSTEM OBJECTIVE: Agricultural Input Subsidy & Profitability Simulator
# Purpose: Academic evaluation tool aligned with Sub-Saharan input policy research.
# Target: Dr. Jacob Ricker-Gilbert alignment (Purdue University)
# =====================================================================

import streamlit as st
import joblib
import pandas as pd

# 1. PAGE SETUP
st.set_page_config(page_title="Input Subsidy Evaluation Simulator", layout="wide")

st.title("🌾 Agricultural Input Subsidy Delivery & Profitability Simulator")
st.markdown("### **Empirical Smallholder Evidence from Edo State, Nigeria**")
st.write("This simulation tool couples a machine learning predictive backend with microeconomic profitability models to analyze how resource prices, training interventions, and structural institutional constraints interact to dictate smallholder farm success.")

st.write("---")

# 2. PANEL 1: STATIC EMPIRICAL FIELD EVIDENCE DASHBOARD
st.subheader("📊 Panel 1: Institutional Constraints & Baseline Field Metrics")
st.write("Before simulating future scenarios, look at the actual documented baseline realities from the study population (50 Smallholder Cassava/Yam Farmers, Edo State):")

# Creating a 4-column metric showcase layout
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="State Fertilizer Subsidy Delivery", value="0%", delta="Target Met: 0/50", delta_color="inverse")
with col2:
    st.metric(label="Land Tenure Insecurity", value="66%", delta="Leased/Unsecured Land", delta_color="inverse")
with col3:
    st.metric(label="Formal Credit Access Rate", value="20%", delta="Only 10/50 Accessing")
with col4:
    st.metric(label="Causal Training Impact", value="+15.68%", delta="Statistically Significant (p<0.05)")

st.info("💡 **Core Empirical Insight:** Multiple linear regression modeling confirms that raw fertilizer volume is statistically insignificant to yield changes when unaccompanied by extension training. Factor efficiency remains locked due to widespread institutional credit and land tenure constraints.")

st.write("---")

# 3. PANEL 2: INTERACTIVE SIMULATOR (USER INPUTS)
st.subheader("🔮 Panel 2: Market Price Shocks & Resource Allocation Scenario Simulator")

# Splitting screen into two functional columns (Left for sliders, Right for outputs)
input_col, output_col = st.columns([1, 1])

with input_col:
    st.markdown("#### **Step 1: Set Market & Farm Parameters**")
    
    # Existing ML Inputs
    farm_size = st.slider("Select Farm Size (Hectares):", min_value=0.5, max_value=10.0, value=2.0, step=0.1)
    fertilizer_qty = st.slider("Select Total Fertilizer Used (kg):", min_value=0, max_value=300, value=50, step=5)
    training_attendance = st.selectbox("Has the farmer attended capacity-building extension training?", options=["No", "Yes"])
    
    # Financial/Academic Price Simulation Inputs
    st.markdown("📈 *Simulate Fertilizer Price Volatility & Spikes:*")
    fertilizer_price_per_kg = st.slider("Fertilizer Market Price (₦ per kg):", min_value=500, max_value=2500, value=1200, step=50)
    crop_price_per_kg = st.slider("Expected Farm-Gate Crop Sale Price (An estimated average return per equivalent yield unit):", min_value=1000, max_value=5000, value=2500, step=100)

# 4. BACKGROUND PROCESSING & MODEL BRAIN EXECUTION
# Machine Learning Variable Encoding
training_encoded = 1 if training_attendance == "Yes" else 0
fertilizer_x_training = fertilizer_qty * training_encoded

# Pack elements into matching DataFrame layout for the machine learning robot
input_data = pd.DataFrame({
    'Farm Size (ha)': [farm_size],
    'Fertilizer Used (kg)': [fertilizer_qty],
    'Training_Encoded': [training_encoded],
    'Fertilizer_x_Training': [fertilizer_x_training]
})

# Wake up your permanent model brain
frozen_robot = joblib.load('machine_learning_model/jpil_random_forest_model.pkl')

# 5. PROFITABILITY CALCULATIONS & DISPLAY PANELS
with output_col:
    st.markdown("#### **Step 2: Live Predictive Economic Evaluation**")
    
    if st.button("Calculate Economic Simulation Outcomes"):
        # Run ML Yield Prediction Model
        predicted_yield_change = frozen_robot.predict(input_data)[0]
        
        # Microeconomic Cost-Benefit Formulas
        # Financial Return = (Yield Improvement % converted to index factor * crop price proxy * farm scale scale factor)
        gross_value_added = (predicted_yield_change / 100.0) * crop_price_per_kg * farm_size * 10 
        total_fertilizer_cost = fertilizer_qty * fertilizer_price_per_kg
        
        # Net Benefit & Cost-Benefit Ratio
        net_economic_benefit = gross_value_added - total_fertilizer_cost
        
        # Avoid division-by-zero errors if fertilizer input is zero
        if total_fertilizer_cost > 0:
            benefit_cost_ratio = gross_value_added / total_fertilizer_cost
        else:
            benefit_cost_ratio = 0.0

        # Output Metric Layout blocks
        st.success(f"📈 **Predicted Yield Change:** {predicted_yield_change:.2f}%")
        st.metric(label="Estimated Net Value Added (Benefit - Input Cost)", value=f"₦{net_economic_benefit:,.2f}")
        st.metric(label="Benefit-to-Cost Efficiency Ratio (BCR)", value=f"{benefit_cost_ratio:.2f}")
        
        st.write("---")
        st.markdown("#### **📋 Strategic Policy Verdict:**")
        
        # Generating customized verdicts reflecting input combination efficiencies
        if benefit_cost_ratio > 1.1 and training_attendance == "Yes":
            st.success("✅ **Profitable & Highly Optimized Scenario:** Fertilizer utilization is economically viable under these price points because the interaction effect of extension training maximizes input return efficiency.")
        elif benefit_cost_ratio > 1.1 and training_attendance == "No":
            st.warning("⚠️ **Marginally Profitable but Sub-Optimized:** While absolute price margins indicate numerical profitability, the return vector remains low. Adding extension training would significantly unlock hidden factor efficiency.")
        else:
            st.error("🚨 **Uneconomic Scenario / Profitability Failure:** The combined input costs outpace productivity gains. High fertilizer prices cannot be sustained under these current management metrics. Structural interventions or training additions are required.")