
###############################################################################
# programa que realiza los conversiones de temperatura (celsius, farenheit, kelvin)

# Convierte los grados celsius en fahrenheit 
def temp_fahrenheit(valor: str):
    f = ((9 * int(valor)) / 5)+32
    print('\n ', f,'F')

#convierte los grados farenheit en celsius    
def temp_celsius_fahr(valor: str):
    c = (5 * (float(valor)-32)) / 9
    print('\n ', round(c), '°C')
    return c

#convierte los grados kelvin a celsius    
def temp_celsius_kelvin(valor: str):
    c = int(valor)- 273
    print('\n ', c, '°C')
    return c

# convierte los grados celsius en kelvin
def temp_kelvin(valor: str):
    k = int(valor)+273
    print('\n ', k, 'K')
    
print("\nCONVERSION DE ESCALAS TERMOMETRICAS\n")
print(" 1.GRADOS CELSIUS     2.GRADOS FAHRENHEIT     3. GRADOS KELVIN\n")
escala = input(" Ingresa la opcion de escala termometrica para la conversion: ")

if escala == '1':
    entrada = input(' Ingresa los grados Celsius: ')
    temp_fahrenheit(entrada)
    temp_kelvin(entrada)

elif escala == '2':
    entrada = input(' Ingresa los grados Fahrenheit: ')
    temp_kelvin(temp_celsius_fahr(entrada))

elif escala == '3':
    entrada = input(' Ingresa los grados Kelvin: ')
    temp_fahrenheit(temp_celsius_kelvin(entrada))

else:
    print(' OPCION NO VALIDA !!')
