#creando un diccionario con dict() , tambien sirve para crear diccionarios vacios

diccionario = dict(name="tomas",surname="oyarzun")

# otra forma

diccionario_2 = {'name' : 'tomas' , 'surname' : 'oyarzun'}


# las listas no puede ser claves (keys)  y usamos frozenset para meter conjuntos o listas como clave ya que ahora es inmutable

diccionario = { frozenset(list(["tomas","123"])) : "value123"}

# accedo al valor
# print(diccionario[frozenset(list(["tomas","123"]))])


#print(hash((1,2,3)))


# creando un diccionario con fromkeys()

diccionario_3 = dict.fromkeys(["asdasdas"])
 # {'asdasdas': None}

diccionario_4 = dict.fromkeys(["nombre", "otroNombre"] , "tomas")

# {'nombre': 'tomas', 'otroNombre': 'tomas'}
print(diccionario_4)