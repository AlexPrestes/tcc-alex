import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df_resultado_liquido = pd.read_csv('Informes/inf_trimestral_fii_resultado_contabil_financeiro.csv')

filter_cnpj = df_resultado_liquido.CNPJ_Fundo == '11.728.688/0001-47'

print(df_resultado_liquido[filter_cnpj][['Data_Referencia','Rendimento_Liquido_Pagar']])