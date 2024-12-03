## Sets ##
my_set = {35, 1.73, 'Micky'}
other_set = set({32, 24, 24, 53, 40})

print(my_set) # Imprime en orden distinto
print(other_set) # Imprime en orden distinto y no muestra datos repetidos
print(type(my_set))
print(type(other_set))

'''
Los sets, a diferencia de las listas y tuplas, no son estructuras ordenadas
Sus elementos son únicos y no admite repetidos
'''

# Funciones
print(len(other_set)) # Muestra la longitud del set (5 porque no cuenta los elementos repetidos)
other_set.add(20) # Agrega un elemento en cualquier posición
print(other_set)
my_set.add('Micky') #No admite el dato repetido
print(my_set) # Solo imprime 'Micky' una vez

print('Micky' in my_set) # (True) porque 'Micky' existe en 'my_set'
print('Mickey' in my_set) # (False) porque 'Mickey' no existe en 'my_set'

other_set.remove(24) # Elimina el elemento del set
print(other_set) # * Solo existe un elemento 24 porque el set no admite repetidos

other_set.clear() # Limpia el set y lo deja sin elementos
print(other_set)

# del es una operacion propia del lenguaje
del other_set
#print(other_set) # Error en consola indicando que other_set no está definido

# Convertir a lista
my_list = list(my_set)
print(my_list)
print(my_list[0])

# Unir sets
language_set = {'JavaScript', 'Python', 'Rust'}
new_set = my_set.union(language_set) # Combina los elementos de manera desordenada
print(new_set)
print(new_set.union({'C#', 'Java', 'Rust'})) # Une los nuevos elementos ignorando los repetidos

print(new_set.difference(my_set)) # Quita los elementos de my_set
