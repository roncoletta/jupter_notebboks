
# coding: utf-8

# In[1]:

import pandas as pd

df = pd.read_csv('/home/pc/workspace/anaconda/files/20130131_Remuneracao_Servidores.csv', encoding='ISO-8859-9',delimiter=';', low_memory=False, decimal=",",)


# In[ ]:




# In[2]:

#df.dtypes


# In[3]:

#df.head(20)


# # Transformar a coluna ano em numerico

# In[4]:

#df['ANO']=pd.to_numeric(df['ANO'], errors='coerce')
#df.head(3)


# In[5]:

#import numpy as np
#df[df['ANO'].apply(np.isnan)]


# In[6]:

#df.tail(20)


# In[7]:

#df.drop(df['ANO'].apply(np.isnan))


# In[8]:

#df.count()


# In[9]:

#df[2375831:2375833]


# In[10]:

#df[df.ANO == np.isnan]


# In[11]:

#df.describe()


# In[12]:

#df.mean()


# In[13]:

#df.sort('REMUNERAÇÃO BÁSICA BRUTA (R$)')


# In[14]:

df2 = pd.DataFrame(df, columns=['ANO','MES','ID_SERVIDOR_PORTAL','NOME','CPF','REMUNERAÇÃO BÁSICA BRUTA (R$)', 'REMUNERAÇÃO APÓS DEDUÇÕES OBRIGATÓRIAS (R$)'])
df2.tail(2)


# In[15]:

df3 = df2.drop([2375831,2375832])
df3.tail(5)


# In[16]:

df_sorted = df3.sort_values( by=['REMUNERAÇÃO BÁSICA BRUTA (R$)', 'ANO', 'MES'])
df_sorted.tail(4)


# # Importe do arquivo de todos os servidores

# In[17]:

df_descricao = pd.read_csv('/home/pc/workspace/anaconda/files/20130131_Servidores.csv', encoding='ISO-8859-9',delimiter='\t', low_memory=False, decimal=",",)




# In[18]:

df_descricao.head(2)


# In[19]:

###df_descricao.query('NOME' == 'CELSO LUIZ NUNES AMORIM')


# In[20]:

new_df = pd.DataFrame(df_descricao, columns=['NOME'])

new_df.head(4)
new_df
#s.where(s == 'CELSO LUIZ NUNES AMORIM')


# In[21]:

df_descricao.drop_duplicates()


# In[22]:

df_descricao.count()


# In[23]:

#df_descricao.JORNADA_DE_TRABALHO.str.split(' ', 1)


# In[24]:

df_descricao.columns


# # Criando um dataframe de 10 posicoes e recuperando apenas colunas importantes

# In[25]:

df_comeco = df_descricao[0:10]
df_comeco.TIPO_VINCULO
df_resumo = pd.DataFrame(df_comeco, columns=['ID_SERVIDOR_PORTAL', 'NOME', 'CPF', 'MATRICULA', 'DESCRICAO_CARGO', 'NIVEL_FUNCAO', 'FUNCAO', 'CODIGO_ATIVIDADE','ATIVIDADE','UORG_LOTACAO','ORG_LOTACAO', 'ORGSUP_LOTACAO', 'TIPO_VINCULO', 'REGIME_JURIDICO','DATA_INGRESSO_CARGOFUNCAO','DATA_INGRESSO_ORGAO'])


# In[26]:

df_resumo.head(10)


# # 

# In[27]:

df_resumo.dtypes


# # Adicionando coluna Salario de janeiro de 2013 sem dados

# In[28]:

import numpy as np 

df_resumo['Salario-janeiro-2013']= 0.0


# In[29]:

df_resumo.head(2)


# # Transformar em Data

# In[30]:

df_resumo['DATA_INGRESSO_CARGOFUNCAO'] = pd.to_datetime(df_resumo['DATA_INGRESSO_CARGOFUNCAO'], errors='coerce')
df_resumo.head(2)


# In[31]:

df_resumo['DATA_INGRESSO_ORGAO'] = pd.to_datetime(df_resumo['DATA_INGRESSO_ORGAO'], dayfirst=True,errors='coerce')
df_resumo.head(2)


# # Ordenar pelo cpf

# In[32]:

df_resumo_ordenada = df_resumo.sort_values( by=['CPF'])
df_resumo_ordenada.tail(4)


# In[33]:

df3.head(1)


# # Recupera informações de uma determinada posicao na matrix
# ## Coluna ano primeiro registro
# 

# In[34]:

df3.ANO[1:2]


# ## Coluna CPF os dois primeiros registros

# In[35]:

df3.CPF[0:2]


# ## Coluna REMUNERAÇÃO BÁSICA BRUTA (R): os dois primeiros registros

# In[36]:

df3['REMUNERAÇÃO BÁSICA BRUTA (R$)'][0:2]


# In[37]:

#indexSalario = pd.Index(df3.ANO, df3.CPF, df3['REMUNERAÇÃO BÁSICA BRUTA (R$)'])


# In[38]:

file = open(file='/home/pc/workspace/anaconda/files/servidores_pequeno.csv', mode='w')


# # Cria um arquivo csv com as 5 primeiras linhas do arquivo original

# In[39]:

#df3[0:10].to_csv
df_head= df3.head(5)
file = open(file='/home/pc/workspace/anaconda/files/servidores_pequeno.csv', mode='w')
df_head.to_csv(path_or_buf=file,  encoding='ISO-8859-9', mode='w')
file.flush
file.close()


# # Cria dois indexes a partir de duas colunas do arquivo

# In[40]:

pd.Index([df3['CPF'], df3['ANO'], ])


# In[ ]:




# In[ ]:



