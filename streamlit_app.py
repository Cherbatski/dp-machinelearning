import streamlit as st
import pandas as pd

st.title('My machine learnign app')

st.info('lets build machine learning model')
with st.expander('Data'):
  st.write("**Raw Data**")
  my_data=pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
  my_data

with st.expander('Data visualization'):
  st.scatter_chart(data=my_data,x='bill_length_mm',y='body_mass_g',color='species')
with st.sidebar:
  st.header('input features')
  islands=st.selectbox('islands',{'Torgersen','Biscoe','Dream'})
  gender=st.selectbox('gender',{'female','male'})
  bill_length_mm=st.slider('bill length (mm)',{32.1,59.6,43.9})
