
# creando una lista con list()

lista = list(['Im tomas', 23, 'open work'])

# len() devuelve la cantidad de elementos

cantidad_elementos = len(lista)

# agregando un elemento a la lista

# lo agrega a la lista original
lista.append(True)

# lo agrega a la lista  en un indice especifico

lista.insert(0, False)

# lo agrega, pero puede agregar varios elementros a la vez , por parametro le pasas una lista

lista.extend([2023, 2024])


# eliminamos un elementos de la lista (por su indice) , si no le pasas el indice , sera -1 por defecto


lista.pop()

# elimina elementro por el valor 
lista.remove(23)


# elimina todo de la lista

#lista.clear()

# sort ordena

another_list = list([23,4,1,5,7])

#another_list.sort(reverse=True)

another_list.reverse()
print(another_list)