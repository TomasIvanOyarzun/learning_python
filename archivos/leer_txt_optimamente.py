# ABRIMSO EL ARCHIVO .TXT CON WITH OPEN
with open("archivos\\prueba.txt", encoding="UTF-8") as archivo:
    # leemos el archivo y lo muestro por consola
    print(archivo.read())

    # no es necesario cerrarlo .close
