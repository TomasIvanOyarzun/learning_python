foods = ("milanea", "asado", "fideos", "pizza")

numbers = (2,4,1,8)

# recorriendo foods
for food in foods:
    print(food)

# recorriendo numbers  y los multiplico * 10
print("-----------------")
for i in numbers:
   result = i * 10
   print(result)

print("------------")
# recorriendo 2 o mas listas juntas 

for food,number in zip(foods,numbers):

   print(f'soy foods indice {foods.index(food)} : {food}')
   print(f'soy numbers indice {numbers.index(number)} : {number}')

# forma no optima de recorrer una lista por su indice

print("---------")

for num in range(len(numbers)):
    print(numbers[num])

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


