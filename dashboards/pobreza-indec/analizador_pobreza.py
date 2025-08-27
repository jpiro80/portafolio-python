import pandas as pd
import streamlit as st
import plotly.express as px

# Cargar el archivo CSV con la codificación y el separador correctos
df = pd.read_csv("pobreza_indec.csv", encoding='latin1', sep=';', header=1)

# Limpiar y renombrar las columnas para un mejor análisis
df = df.dropna(how='all')
df = df.rename(columns={'Unnamed: 1': 'tasa_pobreza'}) # Ejemplo, revisa tu archivo.

# Título del dashboard
st.title("📊 Análisis de Pobreza en Argentina (INDEC)")

# Mostrar las dimensiones de los datos
st.write("Dimensión del DataFrame:", df.shape)

# Mostrar las primeras 5 filas de los datos
st.dataframe(df.head())

# Crear un gráfico de barras interactivo con Plotly
fig = px.bar(df, x=df.columns[0], y="tasa_pobreza", title="Tasa de Pobreza por Provincia")

# Mostrar el gráfico en el dashboard
st.plotly_chart(fig)