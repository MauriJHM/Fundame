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
 prompt: genera una grafica de lineas utilizando las ventas acumuladas por el año filtrado "2015-2016-2017-2018" de order date y su categoria

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
