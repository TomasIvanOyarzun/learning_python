# creamos una funcion que nos devuelva los numeros primos
# entre el 0 y el numero del arg


def is_primo(num):
    for i in range(2, num-1):
        if num % i == 0 : return False
    return True

def get_num_primos(num):
    primos = []
    for i in range(1,num +1):
        result = is_primo(i)
        if result == True : primos.append(i)
    return primos



result = get_num_primos(21)

print(result)


result = lambda num : list(filter(lambda x : all(x % i !=0 for i in range(2, x)), range(1, num+1)))
result_2 = [x for x in range(1,21) if all(x % i !=0 for i in range(2,x)) ]
print(result_2)