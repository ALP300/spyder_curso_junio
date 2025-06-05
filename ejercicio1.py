# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 16:45:28 2025

@author: aitor
"""

import pandas as pd
import numpy as np
datos={'Nombre':['Leonardo','Darik','Julio','Alex'], 'Calificaciones':[
    '60','70','70', '80'], 'Deportes':['Natación','Basquet', 'Fútbol', 'Fútbol'],
    'Materias':['Química','Matemática', 'Historia', 'vida']
       }
df= pd.DataFrame(datos)
print(df)