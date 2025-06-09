import pandas as pd
import numpy as np

datos = pd.read_csv('ATP_DATA.csv', encoding='latin1')
print(datos.head())
print(datos.info())
nuevo=pd.DataFrame(datos)
print(nuevo)
nuevo= nuevo.replace(np.nan,"0")
print("*****IMPRESIÓN SIN NAN******")
print(nuevo.info())
print("*****ESTADÍSTICAS SIN NAN****")

print(nuevo.describe())
print("*****ESTADÍSTICAS SOLAMENTE NÚMEROS****")
print(nuevo.describe(include=[np.number]))

nuevo= nuevo.replace("N/A","0")
nuevo= nuevo.replace("NR","0")
print(nuevo.describe())
nuevo['WRank']= nuevo.WRank.astype(int)
nuevo['Wsets']= nuevo.Wsets.astype(int)
print("*****ESTADÍSTICAS DESPUÉS DE REEMPLAZAR N/A Y NR****")
print(nuevo.describe())