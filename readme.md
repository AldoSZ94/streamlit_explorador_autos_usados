# Explorador de Datos de Vehículos

Este proyecto es una aplicación web interactiva desarrollada con **Streamlit**. Permite explorar datos de vehículos usados en Estados Unidos a partir de un archivo CSV. Incluye visualizaciones como histogramas de los odómetros de los vehículos.

## 📁 Descripción

La aplicación realiza lo siguiente:

- Carga los datos desde `vehicles_us.csv`
- Muestra las primeras filas del conjunto de datos
- Permite generar histogramas interactivos de la columna `odometer` mediante:
  - Un **botón**
  - Una **casilla de verificación**

Las gráficas están hechas con `plotly.express`, lo que proporciona una visualización moderna e interactiva.

## 🛠 Tecnologías utilizadas

- Python 🐍
- Pandas
- Plotly Express
- Streamlit
