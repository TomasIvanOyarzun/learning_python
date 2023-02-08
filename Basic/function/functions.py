# creando una simple funcion

def saludar(name):
    print(f"hola que tal {name}")





def saludar_2(name, sexo):
  
    sexo = sexo.lower()
    if sexo == 'hombre':
        adjetivo = "crack"
    elif sexo == 'mujer':  
        adjetivo = "reina"
    else : adjetivo = "nose"

    print(f"hola {name}, como estas {adjetivo}")     



saludar_2("tomas", "Hombre")    



# funcion para saber si la password es correcta

bdd = list()

def hash_password(password):
    bdd.append(hash(password))
    return bdd



    

# password_hashed = hash_password("hola123")


