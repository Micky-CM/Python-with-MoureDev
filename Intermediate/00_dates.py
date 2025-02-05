## Dates ##

# Importa los módulos 'datetime', 'time', 'date' y 'timedelta'
from datetime import datetime, time, date, timedelta

# Función para imprimir año, mes, día, hora, minuto y segundo
def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())
# Nota: 'timestamp' es el tiempo en segundos que han transcurrido desde las 0 hrs del 01-enero-1970

# 'datetime' permite obtener: fecha y hora actual, manipular fechas, calcular diferencias de tiempo, formatear fechas, etc.
now = datetime.now()
print_date(now)

year_2025 = datetime(2025, 7, 24)
print_date(year_2025)

# 'time' maneja el tiempo en segundos desde el Epoch (1970) y proporciona funciones para pausar la ejecución o medir el tiempo transcurrido.
current_time = time(13, 50, 35)
print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# 'date' solo maneja fechas sin información de la hora.
current_date = date.today()
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2021, 7, 24)
print(current_date.year)
print(current_date.month)
print(current_date.day)

# Se pueden hacer operaciones con los parámetros de date
current_date = date(current_date.year + 3, current_date.month, current_date.day)
print(current_date.year)

# Se pueden hacer operaciones entre objetos del mismo tipo
diff = year_2025 - now
print(diff)
diff = year_2025.date() - current_date
print(diff)

# 'timedelta' se utiliza para realizar sumas, restas y cálculos con fechas y tiempos.
start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
