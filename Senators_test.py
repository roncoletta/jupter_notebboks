
# coding: utf-8

# # Gastos publicos dos senadores brasileiros
# # Brazilian senators' outgoing

# In[4]:

import pandas as pd
df = pd.read_csv('/home/pc/workspace/anaconda/files/senado_federal/ceap_2016.csv', encoding='ISO-8859-9',delimiter=',', low_memory=False, decimal=",",)


# In[5]:

df.head(2)


# # Limpesa de dados
# # Data cleaning

# * Retirando linhas cujo nome do senador não esteja preenchido. (Erase row when senator names is null)

# In[8]:

df = df.dropna(subset=['SENADOR'], axis=0)


# * Retirando linhas cujo valor reembolsado não estaja preenchido. (Erase row when refund value is null)

# In[9]:

df = df.dropna(subset=['VALOR_REEMBOLSADO'], axis=0)


# In[10]:

df.dtypes


# In[12]:

df.describe()


# # Dicionário que contém todos os nomes dos politicos sem repetição

# In[13]:

gastos_senadores= {}
nome_senadores=df.SENADOR.unique()


# In[16]:

nome_senadores[0:3]


# In[23]:

for nome in nome_senadores:
    serie_senador = df[df.SENADOR == nome]
    total_reembolso = serie_senador['VALOR_REEMBOLSADO'].sum()
    gastos_senadores[nome] = total_reembolso

df_reembolso_por_senador = pd.DataFrame.from_dict(gastos_senadores, orient='index')
df_reembolso_por_senador.columns = ['VALOR_REEMBOLSADO']


# In[44]:

df_reembolso_por_senador.head(2)


# # Ordenando em ordem decrescente por valor do reembolso

# In[26]:

df_reembolso_por_senador = df_reembolso_por_senador.sort_values('VALOR_REEMBOLSADO', ascending=False)


# # Tell to notebook print the chart inline

# In[53]:

get_ipython().magic('matplotlib inline')


# In[54]:


df_reembolso_por_senador.plot.barh()


# In[ ]:



