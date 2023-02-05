

numbers = [2 , 1, 3, 9, 12, 13]

multiplicar = lambda x : x*2


# creando una funcion para saber si es par

def num_par(num):
    if num % 2 == 0:
        return True
    
numeros_pares = list(filter(num_par, numbers))

# el us de lambda me ahorro lineas de codigo
numeros_impares = list(filter(lambda num : num % 2 == 1 , numbers))
print(numeros_impares)
