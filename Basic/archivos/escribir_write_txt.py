# estoy abriendo el archivo pero , con el segundo parametro "w" , estoy dando permiso para escribir
with open("archivos\\prueba.txt", "w", encoding="UTF-8") as archivo:
    # estoy sobreescribiendo el archivo .txt
    # archivo.write("estoy escribiendo el archivo")

    archivo.writelines(["aksdjklasjdlkasjkdas\n", "probando 123\n"])
    archivo.writelines(["aksdjklasjdlkasjkdas\n", "probando 123"])