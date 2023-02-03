# funciones integras de python


# conseguir el numero mas alto , lista / tuplas
numbers = (2,1,5,9,23)

max_number = max(numbers)


# conseguir el numero menor , lista / tuplas


max_number = min(numbers)
print(max_number)


# redondeando decimales


decimal = round(12.9232423, 2)

print(decimal)

# retorna false  si , es 0 , vacio , None / True si se pasa tipo de datos no vacios

result_bool = bool([0])

# retorna True si todos los valores son verdaderos o existen

result_all = all([2,43,5,[0],[2], None])

# suma todos los numeros de los iterables

sum_total = sum(numbers)
print(sum_total)