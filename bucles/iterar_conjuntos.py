foods = set(["milanea", "asado", "fideos", "pizza"])

numbers = {2,4,1,8}

# recorriendo foods
for food in foods:
    print(food)

# recorriendo numbers  y los multiplico * 10
print("-----------------")
for i in numbers:
   result = i * 10
   print(result)

print("------------")
# recorriendo 2 o mas conjuntos juntas 

for food,number in zip(foods,numbers):

   print(f'soy foods value : {food}')
   print(f'soy numbers value : {number}')



print("---------")


# forma optima de recorrer una lista

for num in enumerate(numbers):
    #desempaquetar
    index,value = num
    print(f'indice {index} , valor : {value}')
print("---------")
# for / else

for num in numbers:
    print(num)
else:
    print("termino el bucle")    


