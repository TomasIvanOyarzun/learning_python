


sum_two_numbers = lambda first_num,second_num : first_num + second_num



def sum_two():
    num_1 = 2
    return lambda n2,n3: num_1 + n2 + n3

hola = sum_two()
print(hola(2,2))
