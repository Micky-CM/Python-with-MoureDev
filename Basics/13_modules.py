## Modules ##
#import Basics.my_module as my_module # importa el módulo completo

#my_module.sumValues(3, 6, 4)
#my_module.printValue('Hola Python')

from my_module import sumValues, printValue #importa las funciones elegidas
sumValues(4, 3, 2)
printValue('Hola mundo')

import math # math es un módulo integrado de Python

print(math.pi)
print(math.pow(2, 8))
