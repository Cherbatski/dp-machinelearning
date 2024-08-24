import streamlit as st
import pandas as pd

st.title('My machine learnign app')

st.info('lets build machine learning model')
with st.expander('Data'):
  st.write("**Raw Data**")
  my_data=pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
  my_data
# bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g
with st.expander('Data visualization'):
  st.scatter_chart(data=my_data,x='bill_length_mm',y='body_mass_g')
