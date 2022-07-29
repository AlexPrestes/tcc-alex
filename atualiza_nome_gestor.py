import numpy as np
import pandas as pd
import requests
import time

url = 'https://raw.githubusercontent.com/AlexPrestes/tcc-alex/main/'

lista_gestor = pd.read_csv(url + 'cadastro/lista_cnpj_gestores.csv', dtype = {'CNPJ_Gestor': str, 'Nome_Gestor': str})

print('Download git ...')

url_cnpj = 'https://receitaws.com.br/v1/cnpj/'

lista_cnpj = []
lista_nome = []

print('Inicio consulta ...')
for cnpj in lista_gestor.CNPJ_Gestor.unique():
  r = requests.get(url_cnpj + cnpj)
  
  if r.json()['status'] == 'OK':
    lista_cnpj.append(cnpj)
    lista_nome.append(r.json()['nome'].lower())

  print(r.json()['status'], cnpj)
  
  time.sleep(21)


print('Fim consulta ...')

lista_final = pd.DataFrame({'CNPJ_Gestor':lista_cnpj, 'Nome_Gestor':lista_nome})

print('Gerando CSV ...')

lista_final.to_csv('lista_final.csv')

print('Fim')
