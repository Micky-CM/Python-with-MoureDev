## Dictionaries ##
my_dict = {'name': 'Miguel', 'nick': 'Micky', 'age': 35}
other_dict = dict({1: 'id', 2: 1.77, 3: 'text'})
print(type(my_dict))
print(type(other_dict))

# Se puede separar por saltos de línea para legibilidad
my_dict = {
    'name': 'Miguel',
    'nick': 'Mike',
    'age': 35,
    'languages': {'Python', 'JavaScript', 'C#'} # set dentro del diccionario
}
print(my_dict)

# Acceder a elentos
print(my_dict['name']) # Muestra el valor de la clave 'name'
#print(my_dict[35]) # Error en consola porque solo se puede pasar la clave
my_dict['nick'] = 'Micky' # Actualiza el valor de una clave
print(my_dict['nick'])
my_dict['address'] = 'Micky Street' # Agrega una nueva llave con su respectivo valor
print(my_dict)


# Funciones
print(len(my_dict)) # Muestra la longitud de la lista (4)
print(other_dict.clear()) # limpia el diccionario y lo define como 'None'

# del es una operacion propia del lenguaje
del my_dict['address'] # Elimina un elemento del diccionario accediendo a la clave
print(my_dict)

print('Micky' in my_dict) # (False) No realiza la búsqueda por el valor
print('nick' in my_dict) # (True) Solo busca por la clave

print(my_dict.items()) # Muestra todos los ítems del diccionario
print(my_dict.keys()) # Solo muestra las llaves del diccionario
print(my_dict.values()) # Solo muestra los valores del diccionario

new_dict = dict.fromkeys(my_dict) # Copia el diccionario conservando solamente las llaves
print(new_dict) # Todos los valores son 'None'
# Puede tener sentido para transformar esta copia en una lista, una tupla o un set
print(list(new_dict)) # Las claves pasan a ser elementos de una lista