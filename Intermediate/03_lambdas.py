## Lambdas ##

# Es una función anónima que se define sin nombre. Se utiliza para crear pequeñas funciones locales

# Nombre función = 'lambda' argumento : expresiones (return)
sum_two_values = lambda ft_value, sd_value: ft_value + sd_value
print(sum_two_values(3, 4))

multiply_values = lambda ft_value, sd_value: ft_value * sd_value - 3
print(multiply_values(2, 4))

def sum_three_values(value):
    return lambda ft_value, sd_value: ft_value + sd_value + value
print(sum_three_values(6)(3, 4))
