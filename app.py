import streamlit as st

st.set_page_config(page_title="Employee Attrition Prediction")

st.title("Employee Attrition Prediction")

age = st.number_input("Age", min_value=18, max_value=65, value=27)
salary = st.number_input("Salary", min_value=10000, value=32000)
years = st.number_input("Years of Experience", min_value=0, max_value=40, value=2)

if st.button("Predict"):
    if years < 3 and salary < 40000:
        st.error("⚠️ Employee May Leave")
    else:
        st.success("✅ Employee Will Stay")
