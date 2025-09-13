# ------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#  Universidad Tecnológica Nacional - Tecnicatura Universitaria en Programación a Distancia
#
#                   Práctico 4: Estructuras repetitivas
#
# Objetivo:
# Implementar ciclos para resolver problemas que requieran repetición de
# acciones.
# Resultados de aprendizaje:
# 1. Diseño y Desarrollo de Algoritmos Eficientes: El estudiante será capaz de diseñar y
# desarrollar algoritmos utilizando estructuras de control repetitivas (FOR, WHILE) para
# resolver problemas matemáticos y de lógica, aplicando
# correctamente operaciones matemáticas y cálculos.
# 2. Escritura Eficaz de Pseudocódigo y Documentación: El estudiante podrá escribir
# pseudocódigo de manera estructurada y clara, utilizando comentarios para explicar el
# funcionamiento de cada parte del algoritmo.
# 3. Interacción con el Usuario y Validación de Datos: El estudiante será capaz de
# diseñar programas que interactúen con el usuario, solicitando datos de entrada y
# proporcionando resultados claros y concisos.

# Actividades

# Ejercicio 1 - Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

print("-- Programa para imprimir por pantalla todos los números desde 0 hasta 100 --", end="\n\n")
print("-------------------------------------------------------------------------------\n")
print("")
for n in range(101): # Bucle que itera desde 0 hasta 100 y lo imprime por pantalla.
    print(n)

print("")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 2 - Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

print("\n-- Programa para determinar la cantidad de dígitos de un número entero --\n")
print("---------------------------------------------------------------------------\n")
print("")
# ---------------------------------------------------------------------------------------------------------------------------
# Programa para contar la cantidad de dígitos sin bucle
#numero = input("Ingrese un número entero: ").strip() # Se solicita el número al usuario y se eliminan espacios en blanco.
#if numero.lstrip('-').isdigit(): # Se valida que el número ingresado sea un entero (positivo o negativo).
#    cantidad_digitos = len(numero.lstrip('-')) # Se cuenta la cantidad de dígitos, excluyendo el signo negativo si existe.
#    print(f"El número {numero} tiene {cantidad_digitos} dígito(s).\n")
#else:
#    print("El número ingresado es inválido. Por favor, ingrese un número entero.\n")   
# ---------------------------------------------------------------------------------------------------------------------------
# Programa para contar la cantidad de dígitos con un bucle
num = int(input("Ingrese un número entero: "))

# Tomamos el valor absoluto (por si el número es negativo)
n = abs(num)

# Caso especial: si el número es 0, tiene 1 dígito
if n == 0:
    cant_digitos = 1
else:
    cant_digitos = 0
    while n > 0:
        n //= 10         # división entera por 10
        cant_digitos += 1
# Se muestra el resultado
print(f"El número {num} tiene {cant_digitos} dígitos.")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 3 - Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

print("\n-- Programa para sumar todos los números enteros entre dos valores --\n")
print("-----------------------------------------------------------------------\n")
print("")
# Se solicitan el valor inicial y el final al usuario
a = int(input("Ingrese el número inicial: ")) 
b = int(input("Ingrese el número final: "))

a += 1 # Se incrementa 'a' en 1 para excluir el valor inicial

suma = 0 # Se inicializa la variable para almacenar la suma

# Bucle que itera desde 'a' hasta 'b-1' y acumula la suma
for x in range(a,b):
    suma += x
# Se muestra el resultado
print(f"La suma de los números entre {a-1} y {b} es: {suma}")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 4 - Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

print("\n-- Programa para sumar números enteros en secuencia hasta ingresar un 0 --\n")
print("----------------------------------------------------------------------------\n")
print("")
# Se solicita el primer número al usuario
i = int(input("Ingrese un numero a sumar: "))
suma = 0 # Se inicializa la variable para almacenar la suma
# Bucle que continúa hasta que el usuario ingrese un 0
while i != 0:   
    suma += i # Se acumula la suma
    # Se solicita el siguiente número al usuario
    i = int(input("Ingrese un numero a sumar: "))
print(f'El total de la suma es: {suma}') # Se muestra el resultado

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 5 - Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. 
# Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

print("\n-- Juego para adivinar un número entre 0 y 9 --\n")
print("----------------------------------------------------\n\n")
print("Tienes que adivinar un número entre 0 y 9. ¡Suerte!\n")

# Se importa el módulo random para generar números aleatorios
import random

intento = 0 # Se inicializa la variable para contar los intentos

numAlea = random.randint(0, 9) # Se genera un número aleatorio entre 0 y 9.

#print(f'El num aleatorio es: {numAlea}') # Línea para pruebas. Muestra el número aleatorio generado.

# Bucle que continúa hasta que el usuario adivine el número
while True:
    if intento == 0:
        numUsr = int(input("Ingrese un número entre 0 y 9: \n").strip()) # Se solicita el número al usuario y se eliminan espacios en blanco.
    elif numAlea == numUsr:
        break # Si el número ingresado por el usuario es igual al número aleatorio, se sale del bucle.
    else: # si no hay coincidencia, se le pide que ingrese otro número.  
        numUsr = int(input("Vuelva a intentarlo, ingrese un número entre 0 y 9: \n").strip())

    intento += 1 # Se incrementa el contador de intentos.
    
# Se muestra el mensaje de felicitación con el número de intentos.
print("")
print(f"¡Felicidades! ¡Has adivinado el número {numAlea} en el intento: {intento} !\n")   
print("-----------------------------------------------------------------------------\n\n")   

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 6 - Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

print("\n-- Programa para imprimir por pantalla todos los números pares entre 0 y 100 en orden decreciente --\n")
print("------------------------------------------------------------------------------------------------------\n")
print("")
for i in range(100, -1, -1): # Bucle que itera desde 100 hasta 0 en orden decreciente (con pasos de -1)
    if i % 2 == 0: # Se verifica si el número es par
        print(i) # Si es par, se imprime el número

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 7 - Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.        

print("\n-- Programa para sumar todos los números entre 0 y un número entero positivo --\n")
print("---------------------------------------------------------------------------------\n")
print("")
suma = 0 # Se inicializa la variable para almacenar la suma.
numUsr = int(input("Ingrese un número entero positivo: ").strip()) # Se solicita el número al usuario y se eliminan espacios en blanco.
print("\n")

#Bucle que continúa hasta que el usuario ingrese un número positivo
while True:
    if numUsr < 0:
        numUsr = int(input("El número ingresado no es positivo. Por favor, ingrese un número entero positivo: ").strip())
        print("\n")
    #Ciclo for para sumar los números desde 0 hasta el número ingresado por el usuario.     
    for i in range(numUsr+1): 
        print(f'El número a sumar es: {i}') # Línea para pruebas. Muestra el valor que se está sumando.    
        suma += i
    if numUsr >= 0:
        break

#Por último se muestra el siguiente mensaje con el valor total de la suma
print("\n")
print(f"La suma total de los números comprendidos entre 0 y {numUsr} es: {suma}")
   
# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 8 - Escribe un programa que permita al usuario ingresar 100 números enteros. 
# Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. 
# (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

#Se inicializan las variables.
numFinal = 100  #Indicar la cantidad de números requeridos.
numPar = 0
numImp = 0
numPos = 0
numNeg = 0

#Se muestra un mensaje sobre el programa.
print("\n-- Programa para indicar los números pares, impares, negativos y positivos --\n")
print("-------------------------------------------------------------------------------\n")
print("") 
print(f"Se deben ingresar {numFinal} números \n")
print("")

#Se comprueba si el número es par, impar, negativo o positivo.
for i in range(numFinal):
    numUsr = int(input(f"Ingrese el N° {i+1}: ")) 
    
    if numUsr % 2 == 0:
        numPar += 1
    else:
        numImp += 1

    if numUsr > 0:
        numPos += 1
    else:
        numNeg += 1            

#Se muestra un mensaje indicando las cantidades totales de cada uno
print("")
print(f"La cantidad total de números pares es: {numPar} \n") 
print("")
print(f"La cantidad total de números impares es: {numImp} \n")
print("")
print(f"La cantidad de números negativos es: {numNeg} \n")
print("")
print(f"La cantidad de números positivos es: {numPos} \n")        

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 9 - Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. 
# (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

#Se inicializan las variables
numFinal = 100
media = 0

#Se muestra un mensaje sobre el programa
print("\n-- Programa para calcular la media de los valores ingresados --\n")
print("-----------------------------------------------------------------\n")
print("")
print(f"Se deben ingresar {numFinal} números enteros \n")
print("")

#Se calcula la media la media de los valores ingresados
for i in range(numFinal):
    valUsr = int(input(f"Ingrese el valor N° {i+1}: "))
    media += valUsr

#Se calcula la media dividiendo la suma total por la cantidad de números ingresados
media = media / numFinal

#Se muestra un mensaje con la media
print("")
print(f"La media es: {media} \n")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 10 - Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. 
# Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

#Se inicializan las variables
inv = 0

#Se muestra un mensaje sobre el programa y luego se solicita ingresar un número
print("\n-- Programa para invertir el orden de los dígitos del número ingresado --\n")
print("-----------------------------------------------------------------------------\n")
print("")

num = int(input("Ingrese un número entero: ").strip()) # Se solicita el número al usuario y se eliminan espacios en blanco.
print("")

#Se elimina el signo negativo en el caso de ser necesario y se invierten los dígitos.
nAux = abs(num)

while nAux > 0:
    resto = nAux % 10
    inv = inv * 10 + resto
    nAux //= 10

#Si era negativo se le vuelve a asignar el signo
if num < 0:
    inv = -inv

#Se muestra un mensaje con el resultado
print("")
print(f"El número {num} invirtiendo sus dígitos es: {inv} \n")
print("")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------