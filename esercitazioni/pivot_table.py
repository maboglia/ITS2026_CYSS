import pandas as pd

file = 'mod_ese_tot.csv'

lista = pd.read_csv(file)

old_name = lista.columns[2]
lista.rename(columns={old_name: 'Nome'}, inplace=True)

# Convert 'Consegna file' to a binary indicator: 1 if delivered, 0 if not
# We'll consider any non-null value as a delivered file.
lista['File Consegnato'] = lista['Consegna file'].notna().astype(int)

pivot_table = pd.pivot_table(
    lista,
    values='File Consegnato', # Now use the new numeric column
    index='Nome',
    columns='Esercitazione',
    aggfunc='sum', # This will now correctly sum 0s and 1s
    fill_value=0
)

# Add a 'Total' column for the sum of deliveries for each student
pivot_table['Totale Consegnate'] = pivot_table.sum(axis=1)

display(pivot_table)