diccionario = {
    "name" : "tomas",
    "surname" : "oyarzun",
    "age" : 23,

}

for datos in diccionario.items():
  key,value = datos
  print(f"la key es : {key} y el value : {value}")