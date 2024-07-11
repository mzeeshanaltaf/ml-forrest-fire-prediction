import streamlit as st
import pandas as pd


# User inputs
def configure_sidebar_parameters():
    st.sidebar.header('Configuration')
    st.sidebar.subheader('Meteorological Parameters')
    temperature = st.sidebar.number_input('Temperature', min_value=-30, value=25, max_value=50, step=1, format='%d')
    rh = st.sidebar.number_input('Relative Humidity', min_value=0, value=50, max_value=100, step=1, format='%d')
    ws = st.sidebar.number_input('Wind Speed', min_value=0, value=20, max_value=50, step=1, format='%d')
    rain = st.sidebar.number_input('Rain', min_value=0.0, value=15.5, max_value=20.0, step=1.0, format='%f')

    st.sidebar.subheader('Fire Weather Index Parameters')
    ffmc = st.sidebar.number_input('Fine Fuel Moisture Code', min_value=-0.0, value=45.5, max_value=99.0, step=1.0,
                                   format='%f')
    dmc = st.sidebar.number_input('Duff Moisture Code', min_value=0.0, value=5.5, max_value=80.0, step=1.0,
                                  format='%f')
    isi = st.sidebar.number_input('Initial Spread Index', min_value=0.0, value=1.0, max_value=30.0, step=1.0,
                                  format='%f')

    st.sidebar.subheader('Fire Status')
    fire_status = st.sidebar.selectbox('Fire Status', ['Not Fire', 'Fire'])
    # fire_status = 1 if fire_status == 'Fire' else 0

    st.sidebar.subheader('Geographical Parameters')
    region = st.sidebar.selectbox('Region', ['Sidi-Bel', 'Bejaia'])
    # region = 1 if region == 'Sidi-Bel' else 0

    parameters = {
        'Temperature': [temperature],
        'RH': [rh],
        'Ws': [ws],
        'Rain': [rain],
        'FFMC': [ffmc],
        'DMC': [dmc],
        'ISI': [isi],
        'Fire Status': [fire_status],
        'Region': [region]
    }

    # Create DataFrame
    df = pd.DataFrame(parameters)
    return df
