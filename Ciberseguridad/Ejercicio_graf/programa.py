import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Ciberseguridad/Estadistica_Descriptiva/housing.csv')


df.head()


df.tail()

mediacuartos = df['total_rooms'].mean()
print('Media de los cuartos:', mediacuartos)

columna = 'median_house_value'

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

df['price_bins'] = pd.cut(df['median_house_value'], bins=10)
tabla_frecuencias = df.groupby('price_bins')['population'].sum().reset_index()

categorias = tabla_frecuencias['price_bins'].astype(str)
frecuencias = tabla_frecuencias['population']


plt.figure(figsize=(10, 6))
plt.bar(categorias, frecuencias, color='#43d53a')

plt.title('Población y Costo Promedio de la Casa')
plt.xlabel('Rango de Precio de Casas')
plt.ylabel('Población')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
