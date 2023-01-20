import pandas as pd
import streamlit as st
import plotly.express as px


readFile = st.file_uploader("Wybierz plik")

if readFile is not None:
    with st.spinner("Wczytywanie..."):
        df = pd.read_csv(readFile)
        st.write(df)
        tab1, tab2 = st.tabs(["Histogram", "Scatter plot"])
        with tab1:
            st.plotly_chart(px.scatter(df), theme="streamlit", use_conatiner_width=True)
        with tab2:
            st.plotly_chart(px.histogram(df), theme="streamlit", use_conatiner_width=True)