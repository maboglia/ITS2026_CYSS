# devi installare pandas  python -m pip install pandas

import pandas as pd
import matplotlib

df = pd.read_csv('moto.csv')

# print(df.head())
# print(df.tail(3))
# print(df.shape)
# print(df.columns)
# print(df.dtypes)
# print(df.info())
# print(df.describe())
# print(df[["Modello", "Prezzo (€)"]])

# for i in range(0, len(df)):
#     print(df.iloc[i, 0:3] )
#     print("\n\n\n")

# df_max_20000 = df[df["Prezzo (€)"] > 5000]

# df_max_20000.plot.bar(x="Modello")

# matplotlib.pyplot.show()

df.to_html("moto.html")
df.to_excel("moto.xlsx")
