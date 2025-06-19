import streamlit as st
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

st.write("""
         # Data Analysis
         """)


df = pd.read_csv('used_cars_.csv')

df.dropna(axis=0, inplace=True)
df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
df['milage'] = df['milage'].str.replace(',', '').str.extract(r'(\d+)').astype(float)
df['engine_size'] = df['engine'].str.extract(r'(\d+\.\d+)\s*[Ll]')
df['accident_flag'] = df['accident'].apply(lambda x: 0 if 'None reported' in x else 1)
df['clean_title_flag'] = df['clean_title'].apply(lambda x: 1 if x.strip().lower() == 'yes' else 0)

from datetime import datetime
current_year = datetime.now().year
df['car_age'] = current_year - df['model_year']

df = df.drop(columns=['engine', 'accident', 'clean_title'])

invalid_fuel_types = ['–', 'not supported']
invalid_transmissions = ['–']

df = df[~df['fuel_type'].isin(invalid_fuel_types)]
df = df[~df['transmission'].isin(invalid_transmissions)]

fuel_counts = df['fuel_type'].value_counts()
rare_fuels = fuel_counts[fuel_counts < 30].index
df['fuel_type'] = df['fuel_type'].replace(rare_fuels, 'Other')

brand_counts = df['brand'].value_counts()
rare_brands = brand_counts[brand_counts < 30].index
df['brand'] = df['brand'].replace(rare_brands, 'Other')

brands = st.sidebar.multiselect("Select Brand(s)", df['brand'].unique(), default=df['brand'].unique())
df_filtered = df[df['brand'].isin(brands)]

st.subheader("Car Count by Brand")
brand_counts = df_filtered['brand'].value_counts()
st.bar_chart(brand_counts)

st.subheader("Average Price by Brand")
avg_price = df_filtered.groupby('brand')['price'].mean().sort_values(ascending=False)
st.bar_chart(avg_price)

st.subheader("Price vs Mileage")
fig, ax = plt.subplots()
sns.scatterplot(data=df_filtered, x='milage', y='price', hue='brand', ax=ax)
st.pyplot(fig)

st.subheader("Correlation Heatmap")
fig, ax = plt.subplots()
sns.heatmap(df_filtered.select_dtypes(include='number').corr(), annot=True, fmt=".2f", cmap='coolwarm', ax=ax)
st.pyplot(fig)

st.subheader("Boxplot: Price by Fuel Type")
fig, ax = plt.subplots()
sns.boxplot(data=df_filtered, x='fuel_type', y='price', ax=ax)
st.pyplot(fig)
