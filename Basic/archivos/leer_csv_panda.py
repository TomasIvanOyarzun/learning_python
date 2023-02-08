import pandas as pd

df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")

# obteniendo los datos de la columns nombre
name = df["nombre"]

# ordenando el data fram por edad

# por defecto se ordena ascendente
df_ordenado_ascendente = df.sort_values("edad")

# lo mismo pero descendente

df_ordenado_descendente = df.sort_values("edad", ascending= False)
#print(df_ordenado_descendente)

# concatenar df

df_concatenado = pd.concat([df,df2])

#print(df_concatenado)


# accediendo a las 3 primeras filas
df_primera_fila = df.head(3)

# accediendo a las 3 ultimas filas
df_ultima_fila = df.tail(3)

#print(df_ultima_fila)


# accediendo a la cantidad de filas y columnas con shape

filas_totales,columnas_totales = df.shape


# obteniendo data estadistica del dataframe

df_info = df.describe()

# accediendo a un elemento especifico del df con loc

element_especifico_loc = df.loc[0, "edad"]

# accediendo a un elemento especifico del df con iloc
# despues de la , es el index de cada propiedad , en este caso nombre , apellido, edad , el 0 seria nombre

element_especifico_iloc = df.iloc[0,0]

# accediendo a todas las filas de una columna , esto equivale a df["apellido"]

apellidos = df.iloc[:,1]

# accediendo a toda la fila 1 con loc

person = df.loc[0,:]

# accediendo a filas < 30

person_menor_30 = df.loc[df["edad"] < 30, :]

print(person_menor_30)