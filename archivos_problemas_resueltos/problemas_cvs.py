import pandas as pd

df = pd.read_csv("archivos_problemas_resueltos\\datos.csv")

# convertimos a string los datos de edad , que antes era entero
df["edad"] = df["edad"].astype(str)

print(type(df["edad"][0]))


# reemplazando los apellidos oyarzun por Oyarsun
df["apellido"].replace("oyarzun", "Oyarsun", inplace=True)


# eliminando las filas que tiene datos Nan
df = df.dropna()


# eliminando las filas repetidas

df = df.drop_duplicates()

print(df)

# creando un Csv con el dataframe resultante clean (teniendo en cuenta que el anterior puede tener datos
# repetidos y con valores Nan)

df.to_csv("archivos_problemas_resueltos\\datos_clean.csv")
