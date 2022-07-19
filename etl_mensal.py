import wget
import numpy as np
import pandas as pd
import os
from zipfile import ZipFile

url_base = 'http://dados.cvm.gov.br/dados/FII/DOC/INF_MENSAL/DADOS/'
files_name = [ f'inf_mensal_fii_{ano}.zip' for ano in range(2016, 2022) ]

for file_name in files_name:
    file_zip = url_base + file_name
    wget.download(file_zip)

for file_name in files_name:
    ZipFile(file_name, 'r').extractall('CSV')


sulfixo = ['ativo_passivo', 'complemento', 'geral']

for fix in sulfixo:
    df = pd.DataFrame()
    for ano in range(2016, 2022):
        file_name = f'CSV/inf_mensal_fii_{fix}_{ano}.csv'
        df_csv = pd.read_csv(file_name, sep=';', decimal='.', encoding='ISO-8859-1', low_memory=False)
        df = pd.concat([df, df_csv])
    
    df.to_csv(f'informes/inf_mensal_fii_{fix}.csv', index=False)