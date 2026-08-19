import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

language_csv = os.path.join("static", "data.csv") 
df = pd.read_csv(language_csv)

weather_csv = os.path.join("static", "weather.csv") 
df2 = pd.read_csv(weather_csv)

st.subheader("Languages")
st.dataframe(df)

st.subheader("Weather")
st.dataframe(df2)