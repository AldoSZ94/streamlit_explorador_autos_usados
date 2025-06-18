import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv("vehicles_us.csv")  # leer los datos

# Mostrar primeras filas (para depuración)
st.write("Primeras filas del conjunto de datos:")
st.write(car_data.head())

# Botón
hist_button = st.button("Construir histograma")

if hist_button:
    st.write("Creación de un histograma para el conjunto de datos de anuncios de venta de coches")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación
build_histogram = st.checkbox("Construir un histograma (checkbox)")

if build_histogram:
    st.write("Construcción de histograma desde checkbox")
    fig2 = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig2, use_container_width=True)
