# Comentario en Python
print("Hola, mundo!")  # Imprime un mensaje en la consola
# Otro comentario
x = 578  # Asignación de valor a una variable
y = 16670  # Otra asignación
# Suma de dos variables y muestra el resultado
print(x + y)  # Resultado de la suma            
# Fin del programa
# Último comentario
# Comentario adicional al final del archivo

def funcion_ejemplo():
    # Comentario dentro de una función
    return x * y  # Retorna el producto de x e y
resultado = funcion_ejemplo()
print("El resultado de la función es:", resultado)  # Muestra el resultado de la función    
# Comentario final del archivo
# Comentario adicional al final del archivo

vars()  # Muestra las variables actuales en el entorno
sets()  # Muestra los conjuntos actuales en el entorno
bools()  # Muestra los valores booleanos actuales en el entorno
isinstance(x, int)  # Verifica si x es una instancia de int
type(y)  # Muestra el tipo de la variable y

len(str(x))  # Muestra la longitud de la representación en cadena de x
dir()  # Muestra los nombres en el ámbito actual
help(print)  # Muestra la ayuda de la función print
id(x)  # Muestra el identificador único de x
hash(y)  # Muestra el valor hash de y
eval
("x + y")  # Evalúa la expresión x + y como una cadena
exec("z = x + y")  # Ejecuta la asignación de z como una cadena
globals()  # Muestra las variables globales actuales
locals()  # Muestra las variables locales actuales
compile("x + y", "<string>", "eval")  # Compila la expresión x + y

abs(-x)  # Muestra el valor absoluto de -x
all([True, False, True])  # Verifica si todos los elementos son verdaderos
any([True, False, True])  # Verifica si algún elemento es verdadero
bin(x)  # Muestra la representación binaria de x
bool(x)  # Convierte x a un valor booleano
bytearray(b"Hola")  # Crea un bytearray a partir de una cadena
bytes(b"Hola")  # Crea un objeto bytes a partir de una cadena
callable(funcion_ejemplo)  # Verifica si funcion_ejemplo es llam
able
chr(65)  # Convierte el entero 65 a su carácter correspondiente
classmethod(funcion_ejemplo)  # Convierte funcion_ejemplo en un método de clase
compile("x + y", "<string>", "eval")  # Compila la expresión x + y
complex(1, 2)  # Crea un número complejo
del(578)  # Elimina la variable x del entorno
dict(a=1, b=2)  # Crea un diccionario con claves a y b
dir(funcion_ejemplo)  # Muestra los atributos de funcion_ejemplo
divmod(10, 3)  # Devuelve el cociente y el resto de la división
enumerate(['a', 'b', 'c'])  # Devuelve un objeto enumerado
eval("x + y")  # Evalúa la expresión x + y como una cadena
exec("z = x + y")  # Ejecuta la asignación de z como una cadena
filter(lambda a: a > 0, [ -2, 0, 3,
    5])  # Filtra los elementos mayores que 0
float(x)  # Convierte x a un número de punto flotante
format(x, '04d')  # Formatea x con ceros a la izquierda
frozenset([1, 2, 3])  # Crea un conjunto in
mutable
getattr(funcion_ejemplo, '__name__')  # Obtiene el nombre de
# funcion_ejemplo
globals()  # Muestra las variables globales actuales
hasattr(funcion_ejemplo, '__call__')  # Verifica si funcion_ejemplo es llamable
hash(y)  # Muestra el valor hash de y
help(print)  # Muestra la ayuda de la función print
hex(x)  # Muestra la representación hexadecimal de x
id(x)  # Muestra el identificador único de x
input("Ingrese un valor: ")  # Solicita al usuario que ingrese un valor
int("123")  # Convierte la cadena "123" a un entero






