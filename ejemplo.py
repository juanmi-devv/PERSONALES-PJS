#funciones en python

# Procedimiento porque no tiene return
def sumar(a, b):
    resultado = a + b
    print("El resultado de la suma es:", resultado)

# Funcion porque tiene return
def doble(x):
    return x * 2

suma = sumar(5, 10)
print("El resultado de la suma es:", suma)

miVariable = doble(40)

print("Escribir cosas en pantalla", miVariable)

