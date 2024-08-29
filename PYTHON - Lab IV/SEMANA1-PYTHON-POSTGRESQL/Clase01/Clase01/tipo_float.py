#Profundizamos en el tipo float
a = 3.0

#Constructor de tipo float -> puede recibir int y de tipo str
a = float(10) #Le pasamos un tipo int
a = float('10')
print(f'a: {a:.2f}')

# Notacion exponencial (para valores + o -) cantidad de ceros
#Valor positivo
a = 3e5 # Al 3 le agrega 5 ceros
print(f'a: {a:.2f}')

# Valor negativo
a = 3e-5
print(f'a: {a:.5f}')

# Calquier calculo que incluya float cambia todo a float

a = 4.0 + 5
print(a)
print(type(a))

