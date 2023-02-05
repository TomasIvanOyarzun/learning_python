# importar un modulo afuera de nuestra ruta

import sys


sys.path.append('C:\\Users\\Admin\\Desktop\\python\\ejercicio_2')
import ejercicio_2_1_3


result = ejercicio_2_1_3.fibonacci(34)

print(result)