frutas = ["naranja", "manzana", "banana", "pera", "uva", "sandia"]
numbers = [2,4,6,10]

# saltar esa iteracion con el continue
for fruta in frutas:
    if fruta == 'manzana':
        continue
    print(fruta)

# cortar con el bucle con break

for fruta in frutas:
    print(fruta)
    if fruta == 'pera':
        break    


# recorriendo cadenas
print("----")
cadenas = "hola soy tomas"

for cadena in cadenas:
    print(cadena)   

print("----")

# nueva lista multiplicado * 2 con la original
new_numbers = list()
for number in numbers:
    new_numbers.append(number * 2)
    
print(new_numbers)


# lo mismo pero en 1 sola linea


new_numbers_2 = [x * 2 for x in numbers]

print(new_numbers_2)