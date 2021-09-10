# -*- coding: utf-8 -*-
"""SeleçãoProjeto_DevPython.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13fXharF1c2bgnev-Hy92WXHiVhviIljP

**OBS: Para saber se o etanol é mais vantajoso, basta dividir o preço do litro do etanol pelo da gasolina. Se o resultado for inferior a 0,7, o etanol r é o melhor para abastecer. Se for maior que 0,7, então a gasolina é melhor**
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import urllib.request
import json
import ssl


mostrar_dados = pd.read_csv('2021-04-gasolina-etanol.csv', sep=',' , error_bad_lines=False)
print(mostrar_dados)

meses = ['Jan' , 'Fev', 'Mar', 'Abr']
plt.xlabel('Mês')
plt.ylabel('Média/Litros')
plt.hist(meses)
plt.show()

df = np.dtype('float64')  # 64-bit floating-point number


preco_litro_etanol = 4.27
preco_litro_gasolina = 5.73

 
df = pd.DataFrame({
    'Estado': ['AP', 'AP', 'AP', 'AP', 'BA', 'PE', 'PE', 'ES', 'ES' ,'ES'],
    'valor_compra': [69, 99, 75, 99, 89, 36, 52, 57, 49, 57]
})


df = df[['Estado', 'valor_compra']].groupby('Estado').max()
#df.info()
print(df)


media_por_litro = preco_litro_etanol / preco_litro_gasolina
media_por_litro = preco_litro_etanol / preco_litro_gasolina

if preco_litro_etanol < 0.7:
    print("O álcool é melhor para abastercer e mais vantojoso")
elif preco_litro_gasolina > 0.7:
    print("A Gasolina é melhor para abastercer e mais vantajoso")
