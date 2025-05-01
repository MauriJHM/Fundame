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

    # prompt: usando el dataframe df, crear un filtro con la columna region y otro con la columna state donde el resultado sea en una misma tabla

# Assuming 'df' is your DataFrame and it has columns named 'Region' and 'State'

region_filter = st.multiselect("Select Region", df['Region'].unique())
state_filter = st.multiselect("Select State", df['State'].unique())


if region_filter and state_filter :
  filtered_df = df[(df['Region'].isin(region_filter)) & (df['State'].isin(state_filter))]
elif region_filter:
  filtered_df = df[df['Region'].isin(region_filter)]
elif state_filter:
  filtered_df = df[df['State'].isin(state_filter)]
else:
  filtered_df = df # No filter applied


st.dataframe(filtered_df)

# Create the pie chart based on the 'State' column
if 'State' in filtered_df.columns:
    fig_pie = px.pie(filtered_df, names='State', title='Distribution by State')
    st.plotly_chart(fig_pie)
else:
    st.error("The 'State' column is not found in the DataFrame.")

