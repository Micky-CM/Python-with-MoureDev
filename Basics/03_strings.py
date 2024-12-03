## Strings ##
my_string = 'Mi string' # El uso de comillas simples o dobles es indistinto
other_string = "Otro string"

print(len(my_string)) # Muestra la longitud del string (9)
print(len(other_string)) # longitud del contenido de la variable (11)

print(my_string + ' ' + other_string) # Se pueden concatenar con el signo +

line_break_string = 'Este es un String\ncon salto de línea'
print(line_break_string)

tab_string = '\tEste es un string con tabulación'
print(tab_string)

# Se usa \ para escapar caracteres reservados
scape_string = '\\tEste es un string \\n escapado'
print(scape_string)

# Formateo
name, age = 'Micky', 35
print('My name is {} and I´m {} years old'.format(name, age))
print('My name is %s and I´m %d years old' %(name, age)) # %s para strings y %d para integers
print(f'My name is {name} and I´m {age} years old') # Más práctico y más utilizado

# Desempaquetado de caracteres
language = 'Python'
a, b, c, d, e, f = language
print(a)
print(b)
print(e)

# División
language_slice = language[1:3]
print(language_slice)
language_slice = language[2:]
print(language_slice)
language_slice = language[-3]
print(language_slice)

# Reverse
reversed_language = language[::-1] # Invierte el orden del string
print(reversed_language)

# Funciones
print(language.capitalize()) # Conviete la primera letra mayúscula
print(language.upper()) #Convierte todas las letras en mayúsculas
print(language.lower()) #Convierte todas las letras en minúsculas
print(language.count('t')) #Cuenta cuántas 't' tiene el string
print(language.isnumeric()) #Para saber si es un número
print(language.isupper()) #Para saber si las letras son mayúsculas
print(language.startswith('py')) #Para saber si el string comienza con 'Py'. Importan las mayúsculas