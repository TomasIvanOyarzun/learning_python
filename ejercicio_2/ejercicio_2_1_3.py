# crear una funcion  que muestre la serie de fubonacci desde el 0 hasta el arg
from functools import reduce

def fibonacci(num):
    fib = [0,1]
    a,b = 0,1
    for i in range(num):
        if a+b > num: return fib
        c = a + b
        a = b
        b = c
        fib.append(c)
    return fib   


fib =[0,1]
a,b = 0,1

#result = fibonacci(35)
#print(result)


# serie fubonacci

def fubonacci_serie(num):
    if num <= 1 : return 1

    return fubonacci_serie(num -1) + fubonacci_serie(num -2)


#result_serie = fubonacci_serie(8)
#print(result_serie)



# sumar lista con recursion

def sum_list(lista):
    if len(lista) > 1:
        return lista.pop() + sum_list(lista)
    else:
        return lista[0]
    
   
  
   
filter_list_2 = [number for number in [2,3,4,5,6] if number > 0 ]
filter_list_3 = list(filter(lambda x : x % 2 == 0, [2,3,7]))
sum_list_4 = reduce((lambda x,y : x+y),[2,3,5,7,9])
result = sum_list([2,4,5,5,2,1,1])

print(sum_list_4)