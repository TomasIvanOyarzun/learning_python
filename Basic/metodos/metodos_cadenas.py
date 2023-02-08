cadena1 = 'hola soy tomas'
cadena2 = '432432423f'
number = 2323

# dir(object) te dice que metodos disponibles de ese objeto o valor pasado en el parametro

# result = dir(cadena1)

#  pasa a mayuscula
result = cadena1.upper()
#  pasa a minuscula
result1 = cadena1.lower()

# primera letra en mayuscula
result2 = cadena1.capitalize()

# buscamos una cadena  en otra cadena , si no encuntra devuelve -1

result_find = cadena1.find('tomas')

# buscamos una cadena en otra cadena , pero si no existe tira un error (hay que manejar ese error)
result_index = cadena1.index('tomas')



# comprueba si es un numero dentro de un string, pero solo devuelve true si todos son numeros
result_is_numeric = cadena2.isnumeric()

# devuelve la cantidad de coincidencias

result_coincidencia = cadena1.count("a")

# devuelve la longitud de esa cadena

result_length = cadena1.__len__() | len(cadena1)



# verifica si la cadena empieza igual que la cadena pasada por parametro , boolean

result_start_string = cadena1.startswith('Ho')

# verifica si la cadena termina igual que la cadena pasada por parametro , boolean

result_end_string = cadena1.endswith('mas')

# reemplaza la cadena si la encuentra , y la reemplaza por la que indiques, si no encuentra devuelve la cadena original

result_replace = cadena1.replace('hola', 'nada')

# devuelve una list de la cadena , separadas por lo que indiques por parametros


result_list = cadena1.split(" ")
print(result_list)