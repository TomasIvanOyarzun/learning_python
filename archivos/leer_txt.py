# leer archivo completo

archivo_sin_leer = open("archivos\\prueba.txt",encoding="UTF-8")
archivo = archivo_sin_leer.read
# lee una sola linea
linea_1_sin_leer = open("archivos\\prueba.txt",encoding="UTF-8")

linea_1 = linea_1_sin_leer.readline()

# leer por linea , devuelve una lista
lineas_sin_leer = open("archivos\\prueba.txt",encoding="UTF-8")

lineas = lineas_sin_leer.readlines()


# hay que cerrar los archivos

archivo_sin_leer.close()
linea_1_sin_leer.close()
lineas_sin_leer.close()

print(linea_1)