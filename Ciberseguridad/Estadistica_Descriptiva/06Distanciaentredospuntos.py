import numpy as np 
import pandas as pd 
from scipy.spatial import distance 

#Definimos las coordenadas de nuestro sistema de tiendas 
 
tiendas = { 
    'Tienda A': (1,1), 
    'Tienda B': (1,5), 
    'Tienda C': (7,1), 
    'Tienda D': (3,3), 
    'Tienda E': (4,8)   
} 

#Convertir las coordenadas en un frame para facilitar el calculo 

df_tiendas = pd.DataFrame(tiendas).T 
df_tiendas.columns = ['X', 'Y'] 
print('Coordendas de las tiendas: ') 
print(df_tiendas) 

#Inicializamos los dataframe de lo que vamos a obtener para el calculo de distancias 

distancias_punto1 = pd.DataFrame(index=df_tiendas.index, columns=df_tiendas.index) 
distancias_punto2 = pd.DataFrame(index=df_tiendas.index, columns=df_tiendas.index) 
distancias_punto3 = pd.DataFrame(index=df_tiendas.index, columns=df_tiendas.index) 

#vamos a calcular las distancias 

for i in df_tiendas.index: 
    for j in df_tiendas.index: 
        #defino la distancia euclidiana del primer punto 
        distancias_punto1.loc[i, j] = distance.euclidean(df_tiendas.loc[i], df_tiendas.loc[j]) 
        distancias_punto2.loc[i, j] = distance.cityblock(df_tiendas.loc[i], df_tiendas.loc[j]) 
        distancias_punto3.loc[i, j] = distance.chebyshev(df_tiendas.loc[i], df_tiendas.loc[j])         

#mostrar resultados 

print('\nDistancia Euclidiana entre cada una de las tiendas: ') 
print(distancias_punto1)  

print('\nDistancia Manhatthan entre cada una de las tiendas: ') 
print(distancias_punto2) 

print('\nDistancia Chebyshev entre cada una de las tiendas: ') 
print(distancias_punto3) 

 
#----------------------------------------#

#Calcularemos las distancias entre todos los pares de puntos y determinaremos cuáles están más alejados entre sí y cuáles están más cercanos, utilizando las distancias Euclidiana, Manhattan y Chebyshev.
#Ejercicio: Determinación de Distancias entre Puntos
#Puntos en el Plano

#Los puntos en el plano son los siguientes:

#    Punto A: (2, 3)
#   Punto B: (5, 4)
#    Punto C: (1, 1)
#    Punto D: (6, 7)
#    Punto E: (3, 5)
#    Punto F: (8, 2)
#    Punto G: (4, 6)
#    Punto H: (2, 1)

# Definimos las coordenadas de los puntos en el plano
puntos = {
    'Punto A': (2, 3),
    'Punto B': (5, 4),
    'Punto C': (1, 1),
    'Punto D': (6, 7),
    'Punto E': (3, 5),
    'Punto F': (8, 2),
    'Punto G': (4, 6),
    'Punto H': (2, 1)
}

# Convertimos las coordenadas en un DataFrame
df_puntos = pd.DataFrame(puntos).T
df_puntos.columns = ['X', 'Y']
print('Coordenadas de los puntos:')
print(df_puntos)

# Inicializamos los DataFrames para las distancias
distancias_euclidiana = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)
distancias_manhattan = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)
distancias_chebyshev = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)

# Calculamos las distancias entre todos los pares de puntos
for i in df_puntos.index:
    for j in df_puntos.index:
        distancias_euclidiana.loc[i, j] = distance.euclidean(df_puntos.loc[i], df_puntos.loc[j])
        distancias_manhattan.loc[i, j] = distance.cityblock(df_puntos.loc[i], df_puntos.loc[j])
        distancias_chebyshev.loc[i, j] = distance.chebyshev(df_puntos.loc[i], df_puntos.loc[j])

# Mostramos las matrices de distancias
print('\nDistancia Euclidiana entre cada par de puntos: ')
print(distancias_euclidiana)

print('\nDistancia Manhattan entre cada par de puntos: ')
print(distancias_manhattan)

print('\nDistancia Chebyshev entre cada par de puntos: ')
print(distancias_chebyshev)

# Función para encontrar los puntos más cercanos y más lejanos
def encontrar_extremos(distancias, tipo):
    # Convertimos los valores a float para comparaciones numéricas
    distancias_numeric = distancias.astype(float)
    # Excluimos la diagonal (distancias de un punto consigo mismo)
    np.fill_diagonal(distancias_numeric.values, np.nan)
    
    # Encontramos el valor mínimo y máximo
    min_dist = np.nanmin(distancias_numeric.values)
    max_dist = np.nanmax(distancias_numeric.values)
    
    # Encontramos los pares correspondientes
    min_pares = [(i, j) for i in distancias_numeric.index for j in distancias_numeric.columns 
                 if distancias_numeric.loc[i, j] == min_dist]
    max_pares = [(i, j) for i in distancias_numeric.index for j in distancias_numeric.columns 
                 if distancias_numeric.loc[i, j] == max_dist]
    
    print(f'\n{tipo}:')
    print(f'Par más cercano: {min_pares[0][0]} y {min_pares[0][1]} con distancia {min_dist}')
    print(f'Par más lejano: {max_pares[0][0]} y {max_pares[0][1]} con distancia {max_dist}')

# Determinamos los puntos más cercanos y más lejanos para cada métrica
encontrar_extremos(distancias_euclidiana, 'Distancia Euclidiana')
encontrar_extremos(distancias_manhattan, 'Distancia Manhattan')
encontrar_extremos(distancias_chebyshev, 'Distancia Chebyshev')

   

         