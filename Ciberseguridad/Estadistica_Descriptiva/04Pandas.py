import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Ciberseguridad/Estadistica_Descriptiva/cotizacion.csv')


print(df.head())

print(df.tail())


print(df.iloc[7])

print(df['ocean_proximity'])

mediacuartos =  df['total_rooms'].mean()
print('Media de los cuartos: ', mediacuartos)


medianapopularidad = df['population'].median()
print('Mediana de popularidad: ', medianapopularidad)

std_age = df['housing_median_age'].std()
print('Desviación Estándar de años: ', std_age)


filtrodeloceano = df[df['ocean_proximity'] == "ISLAND"]
print("filtro de proximidad del oceano:\n", filtrodeloceano)

plt.scatter(df["ocean_proximity"][:10],df['median_house_value'][:10])

"hay que definir a x y a y"
plt.xlabel('Proximidad')
plt.ylabel('Precio')

plt.title('Gráfico de dispersión de proximidad del oceano vs precio')
plt.show()
