import pandas as pd 
df = pd.read_excel("inventario.xlsx")
print(df.head())
a = "Parque Estadual"
filtrado = df.query(f"Tipologia == '{a}'") 
print(filtrado.head(10))