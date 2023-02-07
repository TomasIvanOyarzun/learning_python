# tenemos 2 lista, una con nombre y otra con apellido

names = ["tomas", "maria", "matias", "sasha", "pepe"]
lastname = ["oyarzun", "aguilar", "fernandez", "gimenez", "pepote"]


# Registar en un txt de forma optima

with open("archivos_problemas_resueltos\\name_lastname","w") as file:
    

    [file.writelines(f"Nombre: {i}\nApellido: {z}\n--------\n") for i,z in zip(names,lastname)]
    #for i,z in zip(names,lastname):
        #file.writelines(f"Nombre: {i}\nApellido: {z}\n--------\n")
 