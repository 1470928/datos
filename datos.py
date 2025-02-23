import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

archivo_excel = '2025-2-7-iolp-buildings.xlsx'
df = pd.read_excel(archivo_excel)

label_encoder = LabelEncoder()

columnas_categoricas = df.select_dtypes(include=['object']).columns

for columna in columnas_categoricas:
    df[columna] = label_encoder.fit_transform(df[columna])

columnas_numericas = df.select_dtypes(include=['number']).columns
df[columnas_numericas] = df[columnas_numericas].fillna(df[columnas_numericas].median())

df["Suma_Total"] = df[columnas_numericas].sum(axis=1)

scaler = MinMaxScaler()
df[columnas_numericas] = scaler.fit_transform(df[columnas_numericas])

df.to_excel('2025-2-7-iolp-buildings-para-modelo.xlsx', index=False)

print("Conversión de los datos.")