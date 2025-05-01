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
# prompt: genera una grafica de barras apiladas usando las ventas acumuladas filtrando los años de la columna order date y agrega la categoria y sub-categoria

import pandas as pd
import plotly.express as px

# Lee el archivo Excel (asegúrate de que la ruta sea correcta)
try:
    df = pd.read_excel('/content/SalidaFinalVentas.xlsx')  # O la ruta correcta a tu archivo
except FileNotFoundError:
    print("El archivo 'SalidaFinalVentas.xlsx' no se encontró. Asegúrate de que la ruta sea correcta y que el archivo exista en Google Colab.")
    exit()  # Salir del script si no se encuentra el archivo
except Exception as e:
    print(f"Ocurrió un error al leer el archivo: {e}")
    exit()


# Suponiendo que las columnas se llaman 'Order Date', 'Category', 'Sub-Category', y 'Sales'
# Ajusta los nombres si son diferentes en tu archivo.

# Convertir 'Order Date' a tipo datetime si no lo está ya
if not pd.api.types.is_datetime64_any_dtype(df['Order Date']):
    df['Order Date'] = pd.to_datetime(df['Order Date'])


# Filtrar los años (ejemplo: 2020 y 2021)
years_to_filter = [2015, 2016, 2017, 2018]  # Ajusta los años según sea necesario
df_filtered = df[df['Order Date'].dt.year.isin(years_to_filter)]


# Agrupar por año, categoría y subcategoría, sumando las ventas
sales_by_category = df_filtered.groupby([df_filtered['Order Date'].dt.year, 'Category', 'Sub-Category'])['Sales'].sum().reset_index()


# Crear la gráfica de barras apiladas
fig = px.bar(sales_by_category, 
             x='Category', 
             y='Sales', 
             color='Sub-Category', 
             title='Ventas Acumuladas por Categoría y Subcategoría',
             facet_col='Order Date',  # Crea una faceta por cada año
             labels={'Sales': 'Ventas', 'Category': 'Categoría', 'Sub-Category': 'Subcategoría', 'Order Date': 'Año'})

fig.show()

# prompt: genera una grafica de lineas utilizando las ventas acumuladas por el año filtrado "2015-2016-2017-2018" de order date y su categoria

# Suponiendo que las columnas se llaman 'Order Date', 'Category', y 'Sales'
# Ajusta los nombres si son diferentes en tu archivo.

# Convertir 'Order Date' a tipo datetime si no lo está ya
if not pd.api.types.is_datetime64_any_dtype(df['Order Date']):
    df['Order Date'] = pd.to_datetime(df['Order Date'])

# Filtrar los años
years_to_filter = [2015, 2016, 2017, 2018]
df_filtered = df[df['Order Date'].dt.year.isin(years_to_filter)]

# Agrupar por año y categoría, sumando las ventas
sales_by_year_category = df_filtered.groupby([df_filtered['Order Date'].dt.year, 'Category'])['Sales'].sum().reset_index()

# Crear la gráfica de líneas
fig = px.line(sales_by_year_category, 
              x='Order Date', 
              y='Sales', 
              color='Category', 
              title='Ventas Acumuladas por Año y Categoría (2015-2018)')

fig.show()
