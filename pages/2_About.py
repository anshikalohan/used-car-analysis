import streamlit as st

st.write("""
# About This Project

This project is my first data analysis and visualization dashboard, built using Streamlit. It focuses on exploring and uncovering insights from a dataset of used cars — particularly around pricing, specifications, and trends across different brands and features.
## Objectives:
Perform data cleaning and preprocessing on raw car listings

Conduct Exploratory Data Analysis (EDA) to understand key patterns

Identify outliers, correlations, and influential features

Build a foundation for predictive modeling (optional)

## Tools Used:
Pandas & NumPy for data manipulation

Matplotlib & Seaborn for visualizations

Streamlit for interactive web-based dashboard

## Dataset Features:
Car brand, model, year, mileage, fuel type, engine size

Transmission type, exterior and interior colors

Flags for clean title and accident history

Final selling price of the car


         """)


url="https://www.kaggle.com/datasets/taeefnajib/used-car-price-prediction-dataset"
st.info("""
#### The dataset can be found [HERE](https://www.kaggle.com/datasets/taeefnajib/used-car-price-prediction-dataset)
"""
)
