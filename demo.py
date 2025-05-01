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
# prompt: de la columna "Order Date", filtra el año "2015-2016-2017-2018" y de ahi crea una nueva columna que se llame "Año"

import pandas as pd

# Lee el archivo Excel
try:
    df = pd.read_excel('SalidaFinalVentas.xlsx')

    # Filtra las filas donde la columna "Order Date" contiene los años especificados
    years_to_filter = ["2015", "2016", "2017", "2018"]
    df_filtered = df[df['Order Date'].astype(str).str.contains('|'.join(years_to_filter))]

    # Crea una nueva columna "Año" extrayendo el año de la columna "Order Date"
    df_filtered['Año'] = pd.to_datetime(df_filtered['Order Date']).dt.year

    # Muestra el DataFrame filtrado con la nueva columna
    print(df_filtered.head())

except FileNotFoundError:
    print("El archivo 'SalidaFinalVentas.xlsx' no se encontró.")
except KeyError:
    print("La columna 'Order Date' no se encontró en el archivo.")
except Exception as e:
    print(f"Ocurrió un error: {e}")

   
