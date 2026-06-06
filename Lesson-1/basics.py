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
# Que a diferencia de otros lenguajes que usan llaves {} para definir los bloques de codigo python usa indentacion.
# Personalmente, eso me parece una cagada, pero es lo que hay.
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
# Por último el standard para nombrar cosas en python es el snake_case, o sea así:
# mi_variable en vez de miVariable.
# Ahora sí podemos iniciar con la primera clase.



# ╔══════════════════════════════════════════════════════════════╗
# ║                      TIPOS DE DATOS                          ║
# ╚══════════════════════════════════════════════════════════════╝

entero = 1            # int — Números enteros, incluye negativos.
entero_negativo = -1
decimal = 1.1         # float — Números con decimales (punto flotante).
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
# es esto que es súper poco intuitivo al inicio, pero tiene sentido conforme uno va entendiendo como sirven las
# cosas por debajo.

# En la mayoría de lenguajes de programación, 1 equivale a 'true' y 0 equivale a 'false'. Por eso esto funciona:

print(True + 1) # Da '2' pq true equivale a 1.
print(False + 1) # Da '1' pq false equivale a 0.

print(True == 1)  # Salida: True
print(False == 0) # Salida: True. Imprime True pq lo que está evaluando es si equivalen, y como sí equivalen la respuesta es True.
# Para que no se confundan.



# ╔══════════════════════════════════════════════════════════════╗
# ║                          OPERADORES                          ║
# ╚══════════════════════════════════════════════════════════════╝

# Ya vimos la suma (+) y hasta multiplicamos un string. Ahora veamos
# todos los operadores que uno termina usando el 99% del tiempo.

# --- Aritméticos ---

print(10 + 3)   # suma            -> 13
print(10 - 3)   # resta           -> 7
print(10 * 3)   # multiplicación  -> 30
print(10 / 3)   # división        -> 3.3333333333333335
print(10 // 3)  # división entera -> 3   (bota los decimales, NO redondea)
print(10 % 3)   # módulo (resto)  -> 1   (lo que sobra de la división)
print(10 ** 3)  # potencia        -> 1000 (10 elevado a la 3)

# Dos cosas a las que hay que ponerle ojo:
#
# 1. La división normal (/) SIEMPRE devuelve float, aunque la cuenta
#    sea exacta:
print(10 / 2)   # -> 5.0  (fíjese en el .0, ya es float, no 5)
#
# 2. El módulo (%) devuelve el RESTO de la división. Suena inútil pero
#    es de lo más usado. Por ejemplo, para saber si un número es par
#    se revisa si el resto de dividirlo entre 2 es 0.
print(8 % 2)    # -> 0  (8 es par, no sobra nada)
print(7 % 2)    # -> 1  (7 es impar, sobra 1)

# =============================================================
# Dato curioso / advertencia sobre los float:
# los decimales NO son perfectamente exactos en la máquina.
# El ejemplo clásico:
print(0.1 + 0.2)   # uno esperaría 0.3, pero da -> 0.30000000000000004
# Es por cómo la compu guarda los decimales en binario por debajo.
# No se compliquen con esto ahorita, solo sépanlo para que no los
# agarre desprevenidos cuando aparezca.
# =============================================================

# --- De comparación ---

# Estos los van a usar muchísimo apenas lleguemos a los condicionales.

print(5 == 5)   # ¿son iguales? (equals)                        -> True
print(5 != 5)   # ¿son distintos? (not)                         -> False
print(5 > 3)    # ¿mayor que?  (greater than)                   -> True
print(5 < 3)    # ¿menor que? (less than)                       -> False
print(5 >= 5)   # ¿mayor o igual que? (equals or greater than)  -> True
print(5 <= 4)   # ¿menor o igual que? (equals or less than)     -> False

# OJO, error clásico de principiante:
#   un solo  =   es para ASIGNAR un valor a una variable.
#   doble    ==  es para COMPARAR si dos cosas son iguales.
#
#   edad = 18      # le asigno 18 a la variable
#   edad == 18     # pregunto si edad es igual a 18 (da True o False)
#
# Confundir = con == es de los errores más comunes al inicio.

# --- Lógicos ---

# En PSeInt usaban Y, O, NO. En python es lo mismo pero en inglés:
#   Y  -> and
#   O  -> or
#   NO -> not

print(True and True)    # -> True   (se cumplen las DOS)
print(True and False)   # -> False  (con que una falle, ya da False)
print(True or False)    # -> True   (con que UNA se cumpla, da True)
print(not True)         # -> False  (not invierte: lo verdadero lo vuelve falso)

# Esto cobra sentido cuando uno combina comparaciones, por ejemplo:
edad = 20
print(edad >= 18 and edad < 65)   # -> True (es mayor de edad Y menor de 65)

# =============================================================
# Ejercicio 2: usando el operador módulo (%) y el de comparación (==),
# imprima el resultado de revisar si el número 4567 es par.

# Si imprime True es par, si imprime False es impar.
# =============================================================









# ╔══════════════════════════════════════════════════════════════╗
# ║                     LEER DATOS: input()                      ║
# ╚══════════════════════════════════════════════════════════════╝

# Hasta ahora solo hemos IMPRIMIDO cosas con print(). Pero un programa
# de verdad muchas veces necesita PEDIRLE datos al usuario.
# Para eso está input().

nombre = input("¿Cómo te llamás? ")

# Muestra el texto y se queda esperando a que el usuario escriba algo y dé enter.
# Lo que el usuario escribe queda guardado en la variable.

print("Hola " + nombre)



# =============================================================
# El detalle MÁS importante de input():
#
#   input() SIEMPRE devuelve un string. SIEMPRE.
#   Aunque la persona escriba un número.
# =============================================================

edad = input("¿Cuántos años tenés? ")   # si escriben 25, edad NO es 25,
                                          # es el string "25"
print(type(edad))   # -> <class 'str'>

# Entonces si uno trata de hacer matemática con eso, truena o se porta raro:

# print(edad + 1)   # TypeError: puede concatenar str con str, no con int

# Aquí es donde sirve lo que vimos de conversión de tipos. Hay que
# convertir el string a número ANTES de usarlo:

edad = int(input("¿Cuántos años tenés? "))   # lo convierto a entero de una vez
print("El año que viene vas a tener", edad + 1)

# Léalo de adentro hacia afuera: primero corre input(), eso devuelve un
# string, y ese string se lo pasamos a int() para que lo convierta a entero.

# =============================================================
# Ejercicio 3: pídale al usuario DOS números con input(), conviértalos
# a int, y imprima la suma.
# (ojo: si NO los convierte, se le van a "sumar" como texto y
#  "2" + "3" da "23" en vez de 5)
# =============================================================









# ╔══════════════════════════════════════════════════════════════╗
# ║               CONDICIONALES: if / elif / else                ║
# ╚══════════════════════════════════════════════════════════════╝

# Esto es lo que en PSeInt era Si / Si no / FinSi. Es la forma de que el
# programa TOME DECISIONES: "si pasa tal cosa haz esto, si no haz otra".

# La estructura es:
#
#   if condicion:
#       # esto corre SOLO si la condición es True
#   elif otra_condicion:
#       # esto corre si la primera fue False y esta es True
#   else:
#       # esto corre si ninguna de las anteriores se cumplió
#
# Acuérdense de lo de la indentación del inicio: lo que va "dentro" del if
# va indentado. Y ojo a los dos puntos ( : ) al final de cada línea.

if edad >= 18:
    print("Sos mayor de edad")
else:
    print("Sos menor de edad")

# La condición (edad >= 18) es exactamente uno de esos operadores de
# comparación que vimos arriba: devuelve True o False, y el if actúa
# según eso.

# Cuando hay más de dos caminos posibles, se usa elif (viene de "else if"):

nota = 75

if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
else:
    print("Reprobado")

# Python revisa las condiciones de arriba hacia abajo y se queda con la
# PRIMERA que se cumpla. Por eso 75 imprime "C" y ya ni revisa el resto.

# =============================================================
# Ejercicio 4 (junta todo lo de hoy):
# Haga un programita que:
#   1. Le pida la edad al usuario con input()
#   2. La convierta a entero
#   3. Imprima "Puede entrar" si tiene 18 o más, y "No puede entrar"
#      si es menor.

# Comente todo el codigo anterior para que no se le haga enredos ni le tire errores.
# para hacer eso rapido haga 'ctrl + a' y luego 'ctrl + /'
# =============================================================









# ╔══════════════════════════════════════════════════════════════╗
# ║                    Y ESO ES TODO POR HOY                     ║
# ╚══════════════════════════════════════════════════════════════╝
#
# Con esto ya tienen lo básico para escribir programas que reciben datos,
# hacen cuentas y toman decisiones. No es poca cosa.
#
# Para el #2 quedan pendientes:
#   - los "loops" (repetir cosas, lo que en PSeInt eran Mientras y Para)
#   - las listas (guardar varios valores en una sola variable)
#   - las funciones (empaquetar código para reutilizarlo)
#
# Practiquen los ejercicios, rompan el código a propósito y lean los
# errores que tira. Así es como se aprende de verdad.