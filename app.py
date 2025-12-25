import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

# Encabezado de la aplicación
st.header("Cuadro de mandos - Análisis de datos de autos")

# Mostrar una vista previa del dataset
st.write("Vista previa del dataset:")
st.write(car_data.head())

# Botón para crear el histograma
if st.button("Mostrar histograma"):
    st.write("Histograma de la primera columna del dataset")

    fig_hist = px.histogram(
        car_data,
        x=car_data.columns[0],
        title="Histograma"
    )

    st.plotly_chart(fig_hist)

# Botón para crear el gráfico de dispersión
if st.button("Mostrar gráfico de dispersión"):
    st.write("Gráfico de dispersión entre las dos primeras columnas del dataset")

    fig_scatter = px.scatter(
        car_data,
        x=car_data.columns[0],
        y=car_data.columns[1],
        title="Gráfico de dispersión"
    )

    st.plotly_chart(fig_scatter)
