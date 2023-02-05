# import modulo_saludar  ---> modulo_saludar.saludar()
from modulo_saludar import saludar as saludo1 ,saludar_2
# estoy importando lo mismo 2 veces
import modulo_saludar

import carpeta.test


result2 = carpeta.test.otro_saludo("tomas")


result = saludo1("juan")

print(result)


print(result2)

# para ver las propiedades y metodos usamos dir

#print(dir(modulo_salusar))

# accedemos al nombre de this.module

#print(__name__)