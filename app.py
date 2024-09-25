import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.title('Car Sales Data Analysis') 
st.header('Exploratory Data Analysis of Car Ads')  

hist_button = st.button('Build Histogram')

if hist_button:  
    st.write('Creating a histogram for the odometer readings...')
    
    fig = px.histogram(car_data, x='odometer', title='Histogram of Odometer Readings')

    st.plotly_chart(fig, use_container_width=True)

scatter_button = st.button('Build Scatter Plot')   
if scatter_button:  
    st.write('Creating a scatter plot for price vs. odometer...')
    fig_scatter = px.scatter(car_data, x='odometer', y='price', title='Scatter Plot of Price vs. Odometer')
    st.plotly_chart(fig_scatter, use_container_width=True)
    