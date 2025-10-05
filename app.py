import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Análisis Exploratorio de Datos", layout="wide")
st.title("📊 Análisis de Datos de Vehículos")

# Carpeta de archivos
csv_folder = "data"
csv_files = [f for f in os.listdir(csv_folder) if f.endswith(".csv")]

selected_file = st.selectbox("Selecciona un archivo CSV", csv_files)
df = pd.read_csv(os.path.join(csv_folder, selected_file))

st.subheader("Vista previa de los datos")
st.dataframe(df.head())

st.subheader("Resumen estadístico")
st.write(df.describe())

# Columnas numéricas
numeric_cols = df.select_dtypes(include="number").columns.tolist()

if numeric_cols:
    # ======= HISTOGRAMA =======
    if st.checkbox("📊 Quiero ver un histograma"):
        selected_col = st.selectbox("Selecciona una columna para el histograma", numeric_cols, key="hist")
        if st.button("Generar Histograma"):
            fig = px.histogram(df, x=selected_col, title=f"Distribución de {selected_col}")
            st.plotly_chart(fig, use_container_width=True)

    # ======= DIAGRAMA DE DISPERSIÓN =======
    if st.checkbox("🔵 Quiero ver un diagrama de dispersión"):
        col_x = st.selectbox("Columna X", numeric_cols, key="x_axis")
        col_y = st.selectbox("Columna Y", numeric_cols, key="y_axis")
        if st.button("Generar Diagrama de Dispersión"):
            fig2 = px.scatter(df, x=col_x, y=col_y, title=f"Dispersión: {col_x} vs {col_y}")
            st.plotly_chart(fig2, use_container_width=True)

else:
    st.warning("No hay columnas numéricas disponibles para graficar.")
