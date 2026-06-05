
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

entero = 1            # int — Numeros enteros, incluye negativos.
entero_negativo = -1
decimal = 1.1         # float — Numeros decimales. Para mayor exactitud matematica.
texto = "Hello World" # str — Cadena de letras, para texto.
booleano = True       # bool — Verdadero o falso, se llama booleano por la matematica booleana (1 y 0)
nulo = None           # None — nulo tal cual, se usa mucho para validar condiciones e.g: si x no es nulo entonces....algo pasa.

# =============================================================
# Como saber el tipo de una variable? con la función type()
# python te devuelve el tipo de cualquier variable o valor.
#
#   type(variable) o type("valor")
#
# Pista para resolver el ejercicio: Esta función devuelve el tipo, pero no lo imprime.
#
# Ejercicio: imprime el tipo de cada variable que definimos arriba.
# =============================================================


