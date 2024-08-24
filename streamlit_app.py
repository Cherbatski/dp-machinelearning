import streamlit as st
import pandas as pd

st.title('My machine learnign app')

st.info('lets build machine learning model')

my_data=pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
my_data
