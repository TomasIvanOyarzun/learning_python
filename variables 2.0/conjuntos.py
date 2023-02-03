#creando un conunto con set()

conjunto = set({"datos","datos2"})

conjunto2 = {"datos","dato2"}


#metiendo un conjunto dentro de otro conjunto

#crea un conjunto inmutable (hasheable) ,
conjunto3 = frozenset({"datos1","datos2"})


conjunto4 = {conjunto3, "datos3"}


#Teoria de conjuntos 

conjunto_a = {1,2,5,9,3}
conjunto_b = {1,9,3}


# devuelve booleano , dependiendo desde la perspectiva

verificando = conjunto_a.issubset(conjunto_b) #False  conjunto_a no es un SUBconjunto de b
verificando_2 = conjunto_b.issubset(conjunto_a) #True conjunto_b si es un SUBconjunto de a

# 
verificando_3 = conjunto_a.issuperset(conjunto_b) #True
verificando_4 = conjunto_b.issuperset(conjunto_a) #False
print(verificando_3)