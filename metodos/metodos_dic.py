diccionario = {
    "channel" : 'NindaYT',
    "age" : 2014,
    "subs" : 19200


}

# nos devuelve todas las key de este diccionario
dic_keys = diccionario.keys()

# obtenemos el valor pasandole por parametro la key

dic_value = diccionario.get("subs")

# eliminar los elemento del diccionario

#diccionario.clear()

# eliminar pop()
diccionario.pop("age")

# obteniendo elementos del diccionario pero iterables

dic_items = diccionario.items()

print(dic_items)