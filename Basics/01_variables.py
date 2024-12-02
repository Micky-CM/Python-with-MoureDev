## Variables ##
my_str_variable = 'My string variable' # snake_case o minúsculas
print(my_str_variable)

int_variable = 5
print(int_variable)

int_to_str_variable = str(int_variable)
print(int_to_str_variable)
print(type(int_to_str_variable)) # type es para mostrar el tipo de dato

bool_variable = False
print(bool_variable)

# Funsion len()
print(len(my_str_variable))

# Concatenación de variables en un print
print(my_str_variable, int_to_str_variable, bool_variable)
print('The value is: ', bool_variable)

# Variables en una sola linea
name, surname, nick, age = 'Miguel', 'Colque', 'Micky', 35

# Concatenar con formato f""
print(f"My name is: {name} {surname}, I'm {age} years old and my nick is {nick}")

# Input para pedir datos al usuario
# Las variables pueden ser reasignadas
name = input('What\'s your name? ') # Se usa \ para escapar caracteres reservados (\')
age = input('How old are you? ')

print(name)
print(age)
