import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st

data = pd.read_csv('amazon-orders.csv')
df = data.copy()
#Drop some columns without any data
df = df.drop(columns=['Purchase Order Number', 'Shipping Address Street 2', 'Group Name', 'Buyer Name'])
#Convert payment data from string to float
df['Total Charged'] = df['Total Charged'].str.replace('$','').astype(float)
df['Tax Charged'] = df['Tax Charged'].str.replace('$','').astype(float)
df['Total Promotions'] = df['Total Promotions'].str.replace('$','').astype(float)
df['Tax Before Promotions'] = df['Tax Before Promotions'].str.replace('$','').astype(float)
df['Shipping Charge'] = df['Shipping Charge'].str.replace('$','').astype(float)
df['Subtotal'] = df['Subtotal'].str.replace('$','').astype(float)

#Convert date to date-time format
df['Order Date'] = pd.to_datetime(df['Order Date'],format="%m/%d/%y")

# print(df.head())

total_spend = df['Total Charged'].sum()
mean_spend = df['Total Charged'].mean()
median_spend = df['Total Charged'].median()
max_spend = df['Total Charged'].max()
min_spend = df['Total Charged'].min()

total_tax = df['Tax Charged'].sum()

tax_rate = (total_tax/total_spend)*100

total_shipping_spend = df['Shipping Charge'].sum()
mean_shipping_spend = df['Shipping Charge'].mean()

#fig_total_spend = px.bar(df,x='Order Date',y='Total Charged')
#fig_total_spend.show()

#fig_total_tax = px.bar(df,x='Order Date',y='Tax Charged')
#fig_total_tax.show()

#fig_carrier = px.histogram(df,x='Carrier Name & Tracking Number')
#fig_carrier.show()

st.title('Amazon Spending Habits Dashboard')
st.divider()
st.markdown('*This dashboard uses a generated dataset and is not real purchases*')
st.divider()
st.header('Data')
st.dataframe(df)
st.header('Spending')
spend_vars = ['Total Charged', 'Tax Charged']
selection = st.radio(label='Transaction',options=spend_vars)
fig_total_spend = px.bar(df,x='Order Date',y=selection)
st.plotly_chart(fig_total_spend)