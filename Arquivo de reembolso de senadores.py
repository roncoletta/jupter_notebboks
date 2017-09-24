
# coding: utf-8

# # Gastos publicos dos senadores brasileiros
# # Brazilian senators' outgoing

# In[1]:

import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv('/home/pc/workspace/anaconda/files/senado_federal/ceap_2016.csv', encoding='ISO-8859-9',delimiter=',', low_memory=False, decimal=",")   


# In[3]:

df.head(1)


# # As colunas mais significativas desse arquivo são:
# * Ano
# * Mês 
# * Senador
# * Valor de reembolso
# * Tipo da despesa

# ## Vamos verificar se entre essas colunas temos dados faltando

# ### Criamos um dataframe secundario com apenas essas colunas

# In[4]:

df_limpesa = pd.DataFrame(df, columns=['ANO', 'MES', 'SENADOR', 'VALOR_REEMBOLSADO', 'TIPO_DESPESA'])


# ### Verificamos se nesse dataframe temos campos nullos

# In[5]:

pd.isnull(df_limpesa).any(1).nonzero()


# ### Podemos verificar que a unica linha que possui valor invalido é a 4822
# #### Vamos imprimi-la

# In[6]:

df.loc[[4822]]


# #### Avaliando os dados pode-se verificar que há um alinha em branco

# 
# ### Vamos remover essa linha no dataframe original
# #### Vou usar a coluna mês como referencia

# In[7]:

df = df.dropna(subset=['MES'], axis=0) 


# ### Validando a limpesa

# In[8]:

df_limpesa = pd.DataFrame(df, columns=['ANO', 'MES', 'SENADOR', 'VALOR_REEMBOLSADO', 'TIPO_DESPESA'])
pd.isnull(df_limpesa).any(1).nonzero()


# ### Procurando apenas na coluna MES do dataframe principal

# In[9]:

df['MES'].index[df['MES'].apply(np.isnan)]   


# # Agora que temos dataframe sem defeitos vamos formatar os campos
# 
# 

# In[10]:

df.head(1)


# ## Ano e mês como float... vamos transformá-los em inteiros

# In[11]:

df.ANO = df.ANO.astype(int)
df.MES = df.MES.astype(int)
df.head(1)


# ## E voi-là, vamos listar os tipos

# In[12]:

df.dtypes


# # Vamos exibir o valor mais alto reembolsado

# In[13]:

df.VALOR_REEMBOLSADO.idxmax()


# In[14]:

df.loc[[6502]]


# ## Ano e mês estão corretos, mas o campo DATA esta como Object, vamos transformálo em Date

# In[15]:

pd.__version__


#     cell_date = '13/01/2016'
# from datetime import datetime
# datetime.strptime(cell_date, '%d/%m/%Y').date().format('DD-MM-YYYY')
# 
# #lambda cell_date: datetime.strptime(cell_date, '%d/%m/%Y')
# 

# from datetime import date
# date(cell_date, '%d/%m/%Y')

# pd.to_datetime(df['DATA'], format='%d/%m/%Y')
# 
# df.DATA.apply(lambda cell_date: datetime.strptime(cell_date, '%d/%m/%Y').date())

# In[ ]:




# In[ ]:




# # Limpesa de dados
# # Data cleaning

# In[16]:

df.describe()


# # Dicionário que contém todos os nomes dos politicos sem repetição

# In[17]:

gastos_senadores= {}
nome_senadores=df.SENADOR.unique()


# In[18]:

nome_senadores[0:3]


# In[19]:

for nome in nome_senadores:
    serie_senador = df[df.SENADOR == nome]
    total_reembolso = serie_senador['VALOR_REEMBOLSADO'].sum()
    gastos_senadores[nome] = total_reembolso

df_reembolso_por_senador = pd.DataFrame.from_dict(gastos_senadores, orient='index')
df_reembolso_por_senador.columns = ['VALOR_REEMBOLSADO']


# In[20]:

df_reembolso_por_senador.head(2)


# # Ordenando em ordem decrescente por valor do reembolso

# In[21]:

df_reembolso_por_senador = df_reembolso_por_senador.sort_values('VALOR_REEMBOLSADO', ascending=False)


# # Tell to notebook print the chart inline

# In[22]:

get_ipython().magic('matplotlib inline')


# In[23]:


df_reembolso_por_senador.head(10).plot.barh()


# # Vamos analisar os dados do Paulo Rocha que parece ser o senador com maior gasto

# * Reset dos indexes

# In[24]:

senador_maior_gasto = df[df['SENADOR'] == 'PAULO ROCHA'].reset_index()


# * Contar quantos registros de reembolso Paulo Rocha teve no periodo

# In[25]:

senador_maior_gasto.shape[0]


# # Criando um dataFrame com os valores gastos pelo Paulo Rocha categorizados

# In[26]:

def gastos_categorizado(senador):
    nome_senador = df[df.SENADOR == senador]
    nome_senador = nome_senador.groupby('TIPO_DESPESA')[['SENADOR', 'VALOR_REEMBOLSADO']].sum()
    return nome_senador


    
    
    


# In[27]:

paulo_rocha= gastos_categorizado('PAULO ROCHA')
paulo_rocha.sort_values(by='VALOR_REEMBOLSADO', ascending=False)


# In[28]:

df.head(5)


# # Vamos ver se existem monopólios estabelecidos

# In[29]:

def monopolio():
    empresa = df.groupby(['CNPJ_CPF', 'TIPO_DESPESA'])[['TIPO_DESPESA', 'VALOR_REEMBOLSADO']].sum()
    return empresa

empresa = monopolio()


# In[30]:

empresa.sort_values(by='VALOR_REEMBOLSADO' ,ascending=False)


# In[31]:

empresa.head(3)


# In[32]:

tipo = df.groupby(by=['CNPJ_CPF'],sort=True)['TIPO_DESPESA'].count()


# In[33]:

tipo.sort_values(axis=0,ascending=True)


# In[34]:

tipo.plot(subplots=True)


# In[35]:

df.CNPJ_CPF[['16.978.175/0001-08']]


# In[36]:

def reembolso_por_empresa(cnpj):
    cnpj = df[df.CNPJ_CPF == cnpj]    
    return cnpj

reembolso_por_empresa('16.978.175/0001-08')


# In[ ]:




# In[37]:

df[(df.VALOR_REEMBOLSADO > 1000)]


# # Quantas vezes cada senador pediu reembolso ligado a uma determinada empresa

# In[54]:

qtd_empresa_senador = df.groupby(['CNPJ_CPF','SENADOR'])[['VALOR_REEMBOLSADO']].count().sort_values(by='VALOR_REEMBOLSADO', ascending=False )
qtd_empresa_senador_maior_que_um = qtd_empresa_senador['VALOR_REEMBOLSADO'] > 1


# In[ ]:



