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

# prompt: usando el dataframe df, crear un filtro con la columna region que sea sidebar

import pandas as pd
import streamlit as st
import plotly.express as px

# Lee el archivo Excel
try:
  df = pd.read_excel('SalidaFinalVentas.xlsx')

  # Verifica si la columna 'Region' existe en el DataFrame
  if 'Region' in df.columns:
    # Crea un filtro para la columna "Region" en la barra lateral
    selected_region = st.sidebar.selectbox("Selecciona una región", df['Region'].unique())

    # Filtra el DataFrame según la selección del usuario
    filtered_df = df[df['Region'] == selected_region]

    # Crea la gráfica de ventas por región con los datos filtrados
    fig = px.bar(filtered_df, x='Region', y='Ventas', title=f'Ventas por Región ({selected_region})')
    st.plotly_chart(fig)

    # Muestra el DataFrame filtrado
    st.dataframe(filtered_df)
  else:
      st.error("La columna 'Region' no se encuentra en el archivo.")

except FileNotFoundError:
  st.error("El archivo 'SalidaFinalVentas.xlsx' no se encontró.")
except Exception as e:
  st.error(f"Ocurrió un error al leer el archivo: {e}")
