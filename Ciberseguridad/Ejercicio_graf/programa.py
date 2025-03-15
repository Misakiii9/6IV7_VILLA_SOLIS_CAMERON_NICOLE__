import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Ciberseguridad/Estadistica_Descriptiva/housing.csv')

# Mostrar las primeras 5 filas
df.head()

# Mostrar las últimas 5 filas
df.tail()

# Obtener la media de la columna de total de cuartos
mediacuartos = df['total_rooms'].mean()
print('Media de los cuartos:', mediacuartos)

# Selección de la columna a analizar
columna = 'median_house_value'

# Calcular estadísticas descriptivas
mediana = df[columna].median()
media = df[columna].mean()
moda = df[columna].mode()[0]
rango = df[columna].max() - df[columna].min()
varianza = df[columna].var()
desviacion_estandar = df[columna].std()

print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Rango: {rango}")
print(f"Varianza: {varianza}")
print(f"Desviación Estándar: {desviacion_estandar}")

# Agrupar precios de casas por rangos y contar la población
df['price_bins'] = pd.cut(df['median_house_value'], bins=10)
tabla_frecuencias = df.groupby('price_bins')['population'].sum().reset_index()

# Extraer categorías y frecuencias
categorias = tabla_frecuencias['price_bins'].astype(str)
frecuencias = tabla_frecuencias['population']

# Graficar
plt.figure(figsize=(10, 6))
plt.bar(categorias, frecuencias, color='#43d53a')

plt.title('Población y Costo Promedio de la Casa')
plt.xlabel('Rango de Precio de Casas')
plt.ylabel('Población')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Mostrar gráfico
plt.show()
