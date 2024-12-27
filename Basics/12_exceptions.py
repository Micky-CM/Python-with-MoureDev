## Exceptions Handling ##
number1, number2 = 5, 2
number2 = '2'

# try - except
try:
    print(number1 + number2)
    print('Se ejecutó con éxito')
except: # Se ejecuta si se produce una excepción
    print('Se ha producido un error')

# try - except - else
try:
    print(number1 + number2)
    print('Se ejecutó con éxito')
except:
    print('Se ha producido un error')
else: # Se ejecuta si NO se produce una excepción
    print('La ejecución continúa correctamente')

# try - except - else - finally
try:
    print(number1 + number2)
    print('Se ejecutó con éxito')
except:
    print('Se ha producido un error')
else:
    print('La ejecución continúa correctamente')
finally: # Se ejecuta siempre
    print('La ejecución continúa')

# Excepciones por tipo
try:
    print(number1 + number2)
    print('Se ejecutó con éxito')
except ValueError:
    print('Se ha producido un ValueError')
except TypeError:
    print('Se ha producido un TypeError')

# Captura de la información de la excepción
try:
    print(number1 + number2)
    print('Se ejecutó con éxito')
except Exception as error:
    print(error)

