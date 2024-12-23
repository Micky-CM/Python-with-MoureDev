## Loops ##

# While
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
    # Se puede anidar condicionales (if, elif, else)
else: # Ejecutar un else junto a while es propio de Python
    print('Mi condición es mayor o igual que 10')
# No se puede ejecutar 'if' ni 'elif' junto a while porque estas llevan condicional

print('La ejecución continúa')

while my_condition < 20:
    my_condition += 2
    if my_condition == 16:
        print('Mi condición es 16')
        break # Detiene la ejecución del ciclo
    print(my_condition)

# For
my_list = [32, 24, 24, 62, 19, 53, 40]
# Recorre los elementos de variables iterables (listas, tuplas, sets y diccionarios)
for element in my_list:
    print(element)

my_dict = {'name': 'Miguel', 'nick': 'Micky', 'age': 35}
# En diccionarios imprime solamente las claves o llaves
for element in my_dict:
    print(element)

# Para imprimir valores se usa .values()
for element in my_dict.values():
    print(element)
    if element == 'Micky':
        break # Detiene la ejecución en este punto
        #continue # Regresa al ciclo sin ejecutar lo que está debajo
    print('Se ejecuta') # No se muestra si se usa continue
else:
    print('El bucle for para el diccionario finalizó')

print('Ejecución terminada')