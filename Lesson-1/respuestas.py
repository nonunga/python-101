#Aquí están las respuestas de los ejercicios si las necesitan.
#Solo usar si fracasan terriblemente, pero preferible no verlas a no ser que sea para revisar.

#Ejercicio 1:

# CODIGO:
# print(type(entero))
# print(type(entero_negativo))
# print(type(decimal))
# print(type(texto))
# print(type(booleano))
# print(type(nulo))

# SALIDA/OUTPUT:
# <class 'int'>
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'bool'>
# <class 'NoneType'>


#Ejercicio 2:

# CODIGO:
# print(4567 % 2 == 0)

# SALIDA/OUTPUT:
# False
# (da False, o sea que el resto de dividir 4567 entre 2 NO es 0,
#  entonces 4567 es impar)


#Ejercicio 3:

# CODIGO:
# numero1 = int(input("Escribí un número: "))
# numero2 = int(input("Escribí otro número: "))
# print(numero1 + numero2)

# SALIDA/OUTPUT (suponiendo que el usuario escribe 2 y luego 3):
# Escribí un número: 2
# Escribí otro número: 3
# 5
#
# Ojo: el int() de cada input es lo importante. Si lo dejan sin convertir,
# "2" + "3" daría "23" (texto pegado) en vez de 5.


#Ejercicio 4:

# CODIGO:
# edad = int(input("¿Cuántos años tenés? "))
# if edad >= 18:
#     print("Puede entrar")
# else:
#     print("No puede entrar")

# SALIDA/OUTPUT (suponiendo que el usuario escribe 20):
# ¿Cuántos años tenés? 20
# Puede entrar
#
# Y si escribe 15:
# ¿Cuántos años tenés? 15
# No puede entrar