
""" 
mostrar por consola del 1 al 100
* multiplos de 3 sustituir por fizz
* multiplos de 5 sustituir por buzz
* multimo de 3 y 5 por fizzbuzz



"""


def fizz_buzz():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} fizzbuzz")
        elif(i % 3 == 0): print(f"{i} fizz")
        elif(i % 5 == 0) : print(f"{i} buzz")
        else : print(i)


"""
 haga una funcion que reciba 2 parametros String,
 y reteornar un booleano en el caso que las palabras sean anagrama
 (una palabra es anagrama cuando tiene la misma cantidad y caracteres, sin importar el orden)
"""


def words_is_anagram(word_1 : str , word_2 : str):
    word1_lower = word_1.lower()
    word2_lower = word_2.lower()

    if (len(word1_lower) != len(word2_lower)) : return False
    elif(word1_lower.find(word2_lower) != -1) : return False
    word1_list = list(word1_lower)
    word2_list = list(word2_lower)
    
    word1_list.sort()
    word2_list.sort()
   
   # no sabia que en python se puede comparar 2 array, siendo este for imnecesario
    for i in enumerate(word1_list):
        index = i
        if word1_list[index] != word2_list[index] : return False

    return True    

    
    

#print(words_is_anagram("Enamoramientos", "Armoniosamente"))



def words_is_anagram_2(word_1 : str , word_2 : str):
    aux = []
    word1_lower = word_1.lower()
    word2_lower = word_2.lower()
    
    if (len(word_1) != len(word_2) ) : return False
    if (word_1 == word_2) : return False

    for words in word1_lower:
        for words_ in word2_lower:

            if words == words_ : aux.append(words_)

       

    return ''.join(aux) == ''.join(word1_lower)

    
def words_is_anagram_3(word_1 : str , word_2 : str):
    
    if (word_1.lower() == word_2.lower()) : return False
    if (len(word_1) != len(word_2) ) : return False


    return sorted(word_1.lower()) == sorted(word_2.lower())
  




#print(words_is_anagram_3("roma", "amor"))       



"""

sucesion de fibinacci , escriba un programa
que muestre por consola los primeros 50 numeros
de la succesion de fibonacci 

"""


def fibonacci(num):
    fib = [0,1]
    a,b = 0,1
    
    while(len(fib) < num):
        c = a + b
        a = b
        b = c

        fib.append(c)
    
    return fib 



print(fibonacci(50))     
