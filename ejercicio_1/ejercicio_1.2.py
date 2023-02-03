frase = input("decime una frase y te digo cuanto tardarias si tuvieras que decirlo: ")
palabras_separadas = frase.split(" ")
cant_palabras = len(palabras_separadas)


if cant_palabras > 100:
    print("Mucho texto(?")

print("------------------------------------")
print(f"dijiste {cant_palabras} y tardarias {cant_palabras / 2} seg en decirlo")
