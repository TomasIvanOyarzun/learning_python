with open("archivos\\prueba.txt", "a", encoding="UTF-8") as archivo:
    # estoy sobreescribiendo el archivo .txt
    # archivo.write("estoy escribiendo el archivo")

    archivo.writelines(["aksdjklasjdlkasjkdas\n", "probando 123\n"])
    archivo.writelines(["aksdjklasjdlkasjkdas\n", "probando 123"])