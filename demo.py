# prompt: imprimir dataframe usando streamlit
import plotly.express as px
import streamlit as st
import pandas as pd

# Lee el archivo Excel
try:
  df = pd.read_excel('SalidaFinalVentas.xlsx')
  st.dataframe(df) # Muestra el DataFrame en Streamlit
except FileNotFoundError:
  st.error("El archivo 'SalidaFinalVentas.xlsx' no se encontró.")
except Exception as e:
  st.error(f"Ocurrió un error al leer el archivo: {e}")

# Lee el archivo Excel
try:
  df = pd.read_excel('SalidaFinalVentas.xlsx')
  
  # Verifica si la columna 'Region' existe en el DataFrame
  if 'Region' in df.columns:
    # Crea la gráfica de ventas por región
    fig = px.bar(df, x='Region', y='Sales', title='Ventas por Región') # Reemplaza 'Ventas' con el nombre de tu columna de ventas
    st.plotly_chart(fig)
  else:
      st.error("La columna 'Region' no se encuentra en el archivo.")
  
  st.dataframe(df) # Muestra el DataFrame en Streamlit
except FileNotFoundError:
  st.error("El archivo 'SalidaFinalVentas.xlsx' no se encontró.")
except Exception as e:
  st.error(f"Ocurrió un error al leer el archivo: {e}")

# prompt: usando el dataframe df, crear un filtro con la columna region

# Suponiendo que 'df' ya está definido y contiene la columna 'Region'

# Crea un filtro para seleccionar filas donde la región sea igual a 'Norte'
region_filtro = df['Region'] == 'Norte'  # Reemplaza 'Norte' con la región deseada

# Aplica el filtro al DataFrame
df_filtrado = df[region_filtro]

# Muestra el DataFrame filtrado
print(df_filtrado)


# En Streamlit:
# Crea un selector de regiones
selected_region = st.selectbox('Selecciona una Región', df['Region'].unique())

# Filtra el DataFrame según la región seleccionada
filtered_df = df[df['Region'] == selected_region]

# Muestra el DataFrame filtrado
st.dataframe(filtered_df)
