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
with st.expander('Data Feature'):
  st.header('input features')
  islands=st.selectbox('islands',{'Torgersen','Biscoe','Dream'})
  bill_length_mm=st.slider('bill length (mm)',32.1,59.6,43.9)
  bill_depth_mm=st.slider('bill depth (mm)',13.1,21.5,17.2)
  flipper_length_mm=st.slider('flipper length (mm)',172.0,231.0,201.0)
  body_mass_g=st.slider('body mass g',2700.0,6300.0,4207.0)
  gender=st.selectbox('gender',{'female','male'})

# create Dataframe
  data={'islands':islands,
  'bill_length_mm':bill_length_mm,
  'bill_depth_mm':bill_depth_mm,
  'flipper_length_mm=st':flipper_length_mm,
  'body_mass_g':body_mass_g,
  'gender': gender      
  }
  input_df=pd.DataFrame(data, index=[0])
  input_df
