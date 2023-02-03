number = input('ingrese un numero: ')

# input siempre va a devolver un string , es decir que si quiero por
# ej hacer op. aritmetica , tendria que parsearlo a un entero
# en este caso int() si le paso algo que no sea un numero tira un error
# lo manejo con try except finally
try:
 result = int(number) * 2 
 print(result)
except(KeyError):
    print(KeyError()) 
    
  

