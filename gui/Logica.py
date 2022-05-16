###############################################################################
# programa que realiza los conversiones de temperatura (celsius, farenheit, kelvin)

# Convierte los grados celsius en fahrenheit 
def temp_fahrenheit(valor: int):
    f = ((9 * int(valor)) / 5)+32
    return f

#convierte los grados farenheit en celsius    
def temp_celsius_fahr(valor: int):
    c = (5 * (float(valor)-32)) / 9
    return c

#convierte los grados kelvin a celsius    
def temp_celsius_kelvin(valor: int):
    c = valor - 273
    return c

# convierte los grados farenheit en kelvin
def temp_kelvin(valor: int):
    celsius = temp_celsius_fahr(valor)
    k = celsius+273
    return k

# convierte los grados celsius en kelvin
def kelvin_celsius(valor:int):
    k = valor + 273
    return k

# convierte los grados kelvin a farenheit
def kelvin_faren(valor:int):
    celsius = temp_celsius_kelvin(valor)
    print(celsius)
    faren = temp_fahrenheit(celsius)
    return faren

#print("\nCONVERSION DE ESCALAS TERMOMETRICAS\n")
#print(" 1.GRADOS CELSIUS     2.GRADOS FAHRENHEIT     3. GRADOS KELVIN\n")
#escala = input(" Ingresa la opcion de escala termometrica para la conversion: ")

#if escala == '1':
#    entrada = input(' Ingresa los grados Celsius: ')
#    temp_fahrenheit(entrada)
#    temp_kelvin(entrada)

#elif escala == '2':
#    entrada = input(' Ingresa los grados Fahrenheit: ')
#    temp_kelvin(temp_celsius_fahr(entrada))

#elif escala == '3':
#    entrada = input(' Ingresa los grados Kelvin: ')
#    temp_fahrenheit(temp_celsius_kelvin(entrada))

#else:
#    print(' OPCION NO VALIDA !!')
