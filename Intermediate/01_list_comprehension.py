## List Comprehension ##

# Sintaxis: elemento 'for' para iterar el elemento 'in' lugar donde iterará
my_list = [i for i in range(7)]
print(my_list)
# Nota: puede ser rango, lista, tupla

# El elemento puede ser modificado dentro de la list comprehension
my_list = [i * i for  i in range(7)]
print(my_list)

def sum_five(number):
    return number + 5
# El elemento está siendo modificado por la función 'sum_five'
my_list = [sum_five(i) for  i in range(7)]
print(my_list)

# También puede incluirse una condicional dentro de la list comprehension
even_numbers = [num for num in range(1, 21) if num % 2 == 0]
print(even_numbers)