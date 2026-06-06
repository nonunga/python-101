
# ╔══════════════════════════════════════════════════════════════╗
# ║            Python para noobs #1 — hecho por nono             ║
# ╚══════════════════════════════════════════════════════════════╝
# Detalles que a uno no le dicen antes de empezar, pero son
# buenos de saber para evitar confusiones en el futuro.
#
# Python es un lenguaje de alto nivel y de tipado dinámico. ¿Qué significa
# esto? Que hace una banda de cosas por uno.
#
# En otros lenguajes al definir una variable hay que decirle
# de qué tipo, como en java:
#
#   String nombre = "antonio"
#
# En python no, él infiere el tipo de la variable dependiendo
# del valor. Yo puedo solo hacer lo siguiente:
#
#   nombre = "antonio"
#
# y ya sabe qué nombre es de tipo string.
# Y si luego la actualizo y hago (aunque no tenga sentido):
#
#   nombre = 1
#
# ahora la variable es de tipo entero (integer) sin tener que
# decírselo explícitamente.
#
# =============================================================
#
# Otra cosa importante de saber, aunque no lo terminen de entender
# completamente, es que python es un lenguaje interpretado.
# ¿Qué significa eso? A diferencia de otros lenguajes que se tienen
# que compilar (convertir a binario para que lo ejecute la máquina)
# antes de correr, como C o Java, python se interpreta en el momento
# que uno ejecuta el archivo.
#
# Los archivos de python, la máquina los lee de arriba para abajo.
# Entonces si yo hago:
#
#   nombre = "antonio"  # creo la variable y le asigno un valor
#   nombre = "carlos"   # reasigno el valor de la variable
#   print(nombre)       # imprimo el valor luego de haberlo reasignado
#
# va a imprimir "carlos"
#
# =============================================================
# También es importante notar que python es un lenguaje indentado, que significa esto?
# Que a diferencia de otros lenguajes que suan llaves {} para definir los bloques de codigo python usa indentacion.
# Personalmente, eso me parese una cagada, pero es lo que hay.
#
# Ejemplo bien indentado:
#
#     def nombre_de_funcion():
#         print("Hola")
#
#
# Ejemplo mal indentado:
#     def nombre_de_funcion2():
#     print("Hola")
#
# esta segunda está mal indentada y va a dar error porque va a detectar que hay una funcion vacia, aquí tecnicamente print
# no está dentro de la funcion.
#
# =============================================================
# Por último el standard para nombrar cosas en python es el Snake_case o sea asi:
# mi_variable en vez de miVariable.
# Ahora sí podemos iniciar con la primera clase.



# ╔══════════════════════════════════════════════════════════════╗
# ║                      TIPOS DE DATOS                          ║
# ╚══════════════════════════════════════════════════════════════╝

entero = 1            # int — Números enteros, incluye negativos.
entero_negativo = -1
decimal = 1.1         # float — Numeros decimales. Para mayor exactitud matematica.
texto = "1111-2222"   # str — Cadena de caracteres, para texto.
booleano = True       # bool — Verdadero o falso, se llama booleano por la matematica booleana (1 y 0)
nulo = None           # None — nulo tal cual, se usa mucho para validar condiciones e.g: si x no es nulo entonces... algo pasa.

# =============================================================
# Como saber el tipo de una variable? con la función type()
# python te devuelve el tipo de cualquier variable o valor.
#
#   type(variable) o type("valor")
#
# Pista para resolver el ejercicio: Esta función devuelve el tipo, pero no lo imprime.
#
# Ejercicio 1: imprima el tipo de cada variable que definimos arriba.
# =============================================================









# =============================================================
#
# epico, ahora tratemos de combinar tipos de datos para ver que se puede y que no.
# Las variables que definimos antes están disponibles a traves del archivo entero entonces podemos seguir usándolas sin tener que volver
# a asignarles un valor.

# int + float

result = entero + decimal # Resultado de la suma de un entero y un decimal: 2.1
# Se conserva el decimal y la variable result queda como float.
# (float y decimal en este contexto es lo mismo, realmente se les dice números de punto flotante).
print(type(result)) #OUTPUT: <class 'float'>

# ¿Qué pasa si intentamos imprimir el resultado de la operacion anterior junto con texto?

# print("Resultado: " + result)

# Eso va a tirar error.
# TypeError: can only concatenate str (not "float") to str.
#Python no nos deja concatenar un string con otra cosa que no sea string.
# Hay que convertir el valor de result de float a string para concatenarlo.
# En python es muy fácil uno simplemente hace:

str(result)

# Entonces uno puede hacer:
print("Resultado: " + str(result)) #Output: Resultado: 2.1

# las funciones de conversion son los mismos nombres de los tipos
int()    # convierte a entero
float()  # convierte a decimal
str()    # convierte a texto
bool()   # convierte a booleano

#Cuando uno quiere imprimir un valor y no necesariamente lo quiere convertir, puede usar un placeholder en el string de esta manera

print(f"Resultado de la suma de un entero y un decimal: {result}")

# Ojo a la 'f' al inicio del string, sin eso no funciona.
# Otra manera simple es hacerlo:
print("Resultado de la suma de un entero y un decimal:", result)

# La diferencia es que con f-strings la variable va exactamente donde uno quiere dentro del texto.
# Con coma las variables siempre van al final separadas por espacios, o sea, menos control.

# Ejemplos de cada uno:

print(f"Resultado de la suma de un entero ({entero}) y un decimal({decimal}) es: {result}")
# Salida:
# Resultado de la suma de un entero (1) y un decimal(1.1) es: 2.1

print("Resultado de la suma de un entero y un decimal:", entero, decimal, result)
# Salida
# Resultado de la suma de un entero y un decimal: 1 1.1 2.1

# Okay sigamos combinando cosas a ver que pasa.
# Tratemos de multiplicar un string. Y aunque suena ridículo python si nos deja.

# Ejemplo:

print("ja " * 3) #Salida: ja ja ja

# Otra cosa vacilona que se me ocurre mostrarles
# es esto que es súper poco intuitivo al inicio, pero tiene sentido conforme uno va entendido como sirven las
# cosas por debajo.

# En la mayoría de lenguajes de programación, 1 equivale a 'true' y 0 equivale a 'false'. Por eso esto funciona:

print(True + 1) # Da '2' pq true equivale a 1.
print(False + 1) # Da '1' pq false equivale a 0.

print(True == 1)  # Salida: True
print(False == 0) # Salida: True. Imprime True pq lo que está evaluando es si equivalen, y como sí equivalen la respuesta es True.
# Para que no se confundan.

