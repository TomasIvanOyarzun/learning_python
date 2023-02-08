# forma no optima de sumar valores


def suma(arg):
    result = 0
    for number in arg:
       result += number

    return result

result = suma( [2,1,6,3,-2])

# forma optima, con * en el paremtro le indico que puedo agregar x cantidad de parametros

def suma_2(*numbers):
   print(numbers)
   return sum(numbers)


print(suma_2(2,4,6))