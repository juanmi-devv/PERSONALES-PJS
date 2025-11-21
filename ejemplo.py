#funciones en python

# Procedimiento porque no tiene return
# def sumar(a, b):
#     resultado = a + b
#     print("El resultado de la suma es:", resultado)

# # Funcion porque tiene return
# def doble(x):
#     return x * 2

# suma = sumar(5, 10)
# print("El resultado de la suma es:", suma)

# miVariable = doble(40)

# print("Escribir cosas en pantalla", miVariable)

while True:
    num = int(input("Ingrese un numero: "))

    if num >= 5 and num < 10:
        print("El número está entre 5 y 10")
        if num == 7:
            print("El numero es 7")
    elif num == 7:
        print("El numero es 7")
    else:
        print("El número no está entre 5 y 10")  

