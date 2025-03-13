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

# Assuming 'df' is your DataFrame and 'Region' is a column in it.
# Check if the 'Region' column exists
if 'Region' in df.columns:
  # Get unique region values
  unique_regions = df['Region'].unique()

  # Create a multiselect widget
  selected_regions = st.multiselect("Select Region(s)", unique_regions)

  # Filter the DataFrame based on selected regions
  if selected_regions:
    filtered_df = df[df['Region'].isin(selected_regions)]
    st.dataframe(filtered_df)
  else:
    st.write("Please select at least one region.")
else:
  st.error("The 'Region' column does not exist in the DataFrame.")

