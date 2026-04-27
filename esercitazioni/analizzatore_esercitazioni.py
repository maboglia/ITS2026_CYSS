import pandas as pd

# file = 'ese01.csv'

# lista = pd.read_csv(file)

# lista.iloc[:,[2,8]].to_csv('mod_' + file)


df1 = pd.read_csv('mod_ese01.csv')
df1['Esercitazione'] = '01'
df2 = pd.read_csv('mod_ese02.csv')
df2['Esercitazione'] = '02'
df3 = pd.read_csv('mod_ese03.csv')
df3['Esercitazione'] = '03'
df4 = pd.read_csv('mod_ese04.csv')
df4['Esercitazione'] = '04'
df5 = pd.read_csv('mod_ese05.csv')
df5['Esercitazione'] = '05'
df6 = pd.read_csv('mod_ese06.csv')
df6['Esercitazione'] = '06'
df7 = pd.read_csv('mod_ese07.csv')
df7['Esercitazione'] = '07'
df8 = pd.read_csv('mod_ese08.csv')
df8['Esercitazione'] = '08'
df9 = pd.read_csv('mod_ese09.csv')
df9['Esercitazione'] = '09'

df_tot = pd.concat([df1, df2, df3, df4,df5,df6,df7,df8,df9])

df_tot.to_csv('mod_ese_tot.csv')


# Pivot#---------------------------------




