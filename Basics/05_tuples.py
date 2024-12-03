## Tuplas ##
my_tuple = (35, 1.73, 'Micky', True)
other_tuple = tuple((32, 24, 24, 19, 53, 40))
print(my_tuple)
print(other_tuple)
print(type(my_tuple))
print(type(other_tuple))

# Recorrer tuplas
print(my_tuple[0])
print(my_tuple[2])
print(my_tuple[-1]) # Último elemento
print(my_tuple[-3]) # Tercer elemento contando desde atrás

# Funciones
print(len(other_tuple)) # Muestra la longitud de la tupla (6)
print(other_tuple.count(24)) # Cuenta la cantidad de veces que se repite un elemento (2)
print(other_tuple.index(19)) # Muestra el índice donde se encuentra el elemento (4)
print(other_tuple[2:5]) # Separa los elementos de la tupla comenzando en [2] y antes de llegar a [5]

# del es una operacion propia del lenguaje
del other_tuple # Elimina la tupla
#print(other_tuple) # Error en consola indicando que other_tuple no está definido
#del other_tuple[2] # Error en consola porque no pueden eliminarse los elementos de la tupla

'''
Las tuplas, a diferencia de las listas, son inmutables
Una vez definida una tupla, no se pueden agregar, modificar o remover elementos
Ej:
my_tuple[2] = 1.80 # Cambiando 1.73 por 1.80
print(my_tuple) # En consola se mostrará error
'''
print(my_tuple + other_tuple) # Se pueden concatenar con el signo +
