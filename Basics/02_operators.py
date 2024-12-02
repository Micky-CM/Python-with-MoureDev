## Operadores aritmeticas ##
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(9 / 4)
print(9 % 4)
print(9 // 4)
print(5 ** 3)

print('hola ' + str(5)) # (hola 5)
print('hola ' * 3) # (hola hola hola)


## Operadores comparativos ##
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
print(4 > 3 == 3) # (true)

print('Hola' > 'Python') # (false)
print('aaa' >= 'aba') # Orden alfabético por ASCII (true)
print('aaa' >= 'AAA') # Orden alfabético por ASCII (false)
print(len('aaa') >= len('bbb')) # Cuenta los caracteres (true)


## Operadores lógicos ##
print(5 == 5 and 4 > 5)  # (false)
print(5 == 5 or 4 > 5)  # (true)
print(5 == 5 or 4 > 5 and 2 < 3)  # (true)
print(not(3 == 3)) # (false)
print(3 > 4 and 'hola' > 'Python')  # (false)
print(3 > 4 or 'hola' > 'Python')   # (true)
