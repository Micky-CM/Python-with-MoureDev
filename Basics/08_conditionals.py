## Conditionals ##
my_condition = False

if my_condition:
    print('Se ejecuta la condición del if si es true')

my_condition = 5 * 2

if my_condition == 10: # Si se cumple la condición es igual a True
    print('Se ejecuta la condición del segundo if')

# Empieza una nueva ejecución de decisión
if my_condition > 10:
    print('Es mayor que 10')
# Se pueden conectar varias condiciones con operadores lógicos
elif my_condition > 10 and my_condition <= 20:
    print('Es mayor a 10 y menor que 20')
else:
    print('Es mayor que 20')

print('La ejecución continúa')


# Un string vacío es interpretado como False
my_string = ''
if my_string:
    print('La cadena de texto está vacía') # No imprime nada porque la condición es False

my_string = 'Cadena de texto'
if my_string:
    print('La cadena de texto no está vacía') # Se imprime porque la condición es True