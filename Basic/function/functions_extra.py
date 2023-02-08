def frase(nombre, apellido , adjetivo):
    return f"Hola {nombre} {apellido} , sos muy {adjetivo}"


# el orden de los argumentos importan , a menos que hagamos keywords arguments , entonces podemos definirlo
# sin importar el orden
la_frase = frase(adjetivo= "crack", apellido="oyarzun", nombre= "tomas")


# usamos keywords parameters , definimos por defecto que ese parametro tenga x valor 
# entonces  si no lo definis en el argumentos , usa el por defecto y 
# si no viceversa...
def frase_2(nombre, apellido , adjetivo="genio"):
    return f"Hola {nombre} {apellido} , sos muy {adjetivo}"


la_frase_2 = frase_2("tomas", "oyarzun")
print(la_frase_2)