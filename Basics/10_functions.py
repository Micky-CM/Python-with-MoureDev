## Funtions ##
def my_function(): # Definición de la función
    print('Esto es una función')

my_function() # LLamada de la función

def sum_values(number_1, number_2): # Parámetros: Variables que se esperan recibir
    print(number_1 + number_2)

sum_values(4, 3) # Argumentos: Valores que se envían a los parámetros
sum_values(7.83, 5)
sum_values('5', '4') # Concatena strings
#sum_values('6', 7) # No concatena enteros con stings

def sum_values_with_return(value_1, value_2):
    return value_1 + value_2

result = sum_values_with_return(3.45, 8.25)
print(result)

def print_name(name, surname):
    print(f'{name}, {surname}')

print_name('Miguel', 'Colque')

def print_name_default(name, surname, nick='Sin apodo'):
    print(f'Nombre completo: {name} {surname}, Apodo: {nick}')

print_name_default('Brais', 'Moure', 'MoureDev')
print_name_default('Winston', 'Churchill')

# Con asterisco en el parámetro se puede pasar cualquier cantidad de argumentos
def print_texts(*texts):
    print(type(texts)) # Python interpreta la variable como una tupla
    print(texts)

print_texts('Hola', 'Python')
print_texts('Django', 'FastAPI', 'Flask')
