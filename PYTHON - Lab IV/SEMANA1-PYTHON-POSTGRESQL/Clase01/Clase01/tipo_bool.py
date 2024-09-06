
# Bool contiene valores de T o F
# Los tipos numericos en F para el 0, y T para los demas valores
valor = 0.0
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

valor =  0.1
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

# Tipo str -> F '' (cadena vacia). T para los demas valores
valor = ''
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

valor = 'hola'
resultado = bool(valor)
print(f'Valor: {valor}, Resultado: {resultado}')

#Tipo colecciones -> F para colecciones vacias
#Tipo colecciones -> T para todas las demas
#Lista
valor = []
resultado = bool(valor)
print(f'Valor de una lista vacia: {valor}, Resultado: {resultado}')

valor = [2, 3, 4]
resultado = bool(valor)
print(f'Valor de una lista con elementos: {valor}, Resultado: {resultado}')

#Tupla
valor = () # Vacia F  y con elem es T
resultado = bool(valor)
print(f'Valor de una tupla vacia: {valor}, Resultado: {resultado}')

valor = (5, 6) # Vacia F  y con elem es T
resultado = bool(valor)
print(f'Valor de una tupla con elementos: {valor}, Resultado: {resultado}')


#Diccionario
valor = {}
resultado = bool(valor)
print(f'Valor de un diccionario vacio: {valor}, Resultado: {resultado}')

#valor = {'Nombre': 'Juan', 'Apellido': 'Perez'}
resultado = bool(valor)
print(f'Valor de un diccionario con elementos: {valor}, Resultado: {resultado}')

# Sentencias de control con bool
if (1,):
    print('Regresa verdadero')
else:
    print('Regresa falso')

# ciclos
variable = 17
while variable:
    print('Regresa verdadero')
    break
else:
    print('Regresa falso')