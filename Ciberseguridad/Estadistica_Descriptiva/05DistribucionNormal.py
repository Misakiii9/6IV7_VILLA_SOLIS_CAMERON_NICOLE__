import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

#vamos a crear una semilla random 
np.random.seed(0) 

#vamos a obtener los parametros que necesitamos para la distribucion normal 

media = 0 
sigma1 = 1 
sigma2 = 2 
sigma3 = 3  
n_muestras = 1000 

#generar la distribucion  
data1 = np.random.normal(media,sigma1, n_muestras) 
data2 = np.random.normal(media,sigma2, n_muestras) 
data3 = np.random.normal(media,sigma3, n_muestras) 

#configurar el grafico 
plt.figure(figsize=(10,6)) 

#graficarlo como un histograma 
plt.hist(data1, bins=(30), color='blue', density=True, label='Desviacion Estandar: 1', alpha=0.5) 
plt.hist(data2, bins=(30), color='red', density=True, label='Desviacion Estandar: 2', alpha=0.5) 
plt.hist(data3, bins=(30), color='green', density=True, label='Desviacion Estandar: 3', alpha=0.5) 


#Formato ala grafica 
plt.title('Comparacion de Distribucion Estandar con una semilla random') 
plt.xlabel('Valor') 
plt.ylabel('Densidad') 

plt.axhline(0, color='black', linewidth=0.5, ls='--') 
plt.axvline(0, color='black', linewidth=0.5, ls='--') 

plt.legend() 
plt.grid() 


import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

base_dir = r"C:\Users\Cameron\Desktop\6IV7_VILLA_SOLIS_CAMERON_NICOLE\Ciberseguridad\Estadistica_Descriptiva"
archivo_df2 = "Catalogo_sucursal.xlsx"
archivo_df = "proyecto1.xlsx"

ruta_df2 = os.path.join(base_dir, archivo_df2)
ruta_df = os.path.join(base_dir, archivo_df)

df2 = pd.read_excel(ruta_df2)
df = pd.read_excel(ruta_df)

#1 
columna = 'ventas_tot'  
columna2 = 'suc'         
columna_id = 'id_sucursal'  

for id in df2[columna_id].unique():
    ventas = df[df[columna_id] == id][columna].sum()
    sucursal_info = df2[df2[columna_id] == id][columna2].values
    sucursal = sucursal_info[0] if len(sucursal_info) > 0 else 'Desconocida'
    print(f'Ventas totales de {sucursal}: {ventas}\n')

#2
con=0
sin=0
for adeudo in df['B_adeudo']:
    if adeudo == 'Con adeudo':
        con +=1
    else:
        sin+=1

socios= con +sin
porcon=(con*100)/socios
porsin=(sin*100)/socios

print('socios con adeudo: ',con,', ',porcon,'%','\n')
print('socios sin adeudo: ',sin,', ',porsin,'%','\n')

#3 - Gráfica de barras de ventas en el tiempo
df['fec_ini_cdto'] = pd.to_datetime(df['fec_ini_cdto'])
df = df.sort_values(by='fec_ini_cdto')

ventas_totales = df['ventas_tot']
tiempo = df['fec_ini_cdto']

plt.figure(figsize=(12, 6))
plt.bar(tiempo, ventas_totales, color='#a8f3ea')  

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())

plt.title('Ventas totales al pasar el tiempo')
plt.xlabel('Tiempo')
plt.ylabel('Ventas totales')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#4 - Desviación estándar por sucursal en el tiempo
df['B_mes'] = pd.to_datetime(df['B_mes'], format='%Y-%m')
df_merged = df.merge(df2, on='id_sucursal', how='left')

df_std = df_merged.groupby(['B_mes', 'suc'])['pagos_tot'].std().reset_index()
colores = plt.cm.Set2(np.linspace(0, 1, df_std['suc'].nunique()))

plt.figure(figsize=(12, 6))
for i, (sucursal, grupo) in enumerate(df_std.groupby('suc')):
    plt.bar(grupo['B_mes'], grupo['pagos_tot'], color=colores[i], label=f'Sucursal: {sucursal}', alpha=0.8, width=20)

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())

plt.title('Desviación Estándar de los Pagos Realizados por Sucursal en el Tiempo')
plt.xlabel('Mes')
plt.ylabel('Desviación Estándar de Pagos Totales')
plt.xticks(rotation=45)
plt.legend(title='Sucursal')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#5 - Deuda total por sucursal
deuda1='adeudo_actual'

for id in df2[columna_id].unique():
    deudas = df[df[columna_id] == id][deuda1].sum()
    sucursal_info = df2[df2[columna_id] == id][columna2].values
    sucursal = sucursal_info[0] if len(sucursal_info) > 0 else 'Desconocida'
    print(f'Deuda total de los clientes en {sucursal}: ${deudas}\n')

#6 - Porcentaje de utilidad
for id in df2[columna_id].unique():
    deudas = df[df[columna_id] == id][deuda1].sum()
    ventas = df[df[columna_id] == id][columna].sum()
    porUtilidad =((ventas-deudas)/ventas)*100
    sucursal_info = df2[df2[columna_id] == id][columna2].values
    sucursal = sucursal_info[0] if len(sucursal_info) > 0 else 'Desconocida'
    print(f'Porcentaje de utilidad de {sucursal}: {porUtilidad:.2f}%\n')

#7 - Gráfico circular (pastel) de ventas por sucursal
ventas_por_sucursal = df_merged.groupby('suc')['ventas_tot'].sum()

plt.figure(figsize=(8, 8))
plt.pie(
    ventas_por_sucursal, 
    labels=ventas_por_sucursal.index, 
    autopct='%1.1f%%', 
    colors=plt.cm.Pastel1.colors, 
    startangle=140
)
plt.title('Distribución de Ventas Totales por Sucursal')
plt.show()

#8 - Gráfico combinado: deuda total vs margen de utilidad
deuda_por_sucursal = df_merged.groupby('suc')['adeudo_actual'].sum()
ventas_por_sucursal = df_merged.groupby('suc')['ventas_tot'].sum()
utilidad_por_sucursal = ((ventas_por_sucursal - deuda_por_sucursal) / ventas_por_sucursal) * 100

fig, ax1 = plt.subplots(figsize=(12, 6))

# Barras de deuda
color = '#e76f51'  # Rojo terracota
ax1.set_xlabel('Sucursal')
ax1.set_ylabel('Deuda Total ($)', color=color)
ax1.bar(deuda_por_sucursal.index, deuda_por_sucursal, color=color, alpha=0.8, label='Deuda Total')
ax1.tick_params(axis='y', labelcolor=color)

# Línea de margen de utilidad
ax2 = ax1.twinx()
color = '#2a9d8f'  # Verde esmeralda
ax2.set_ylabel('Margen de Utilidad (%)', color=color)
ax2.plot(utilidad_por_sucursal.index, utilidad_por_sucursal, color=color, marker='o', linestyle='-', linewidth=2, label='Margen de Utilidad')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Deuda Total vs. Margen de Utilidad por Sucursal')
fig.tight_layout()
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
plt.show()
