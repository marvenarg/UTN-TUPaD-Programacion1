#  Ejercicio 1: Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#  deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

print("-- Programa para verificar si el usuario es mayor de edad --", end="\n\n")
print(end="\n") # Se agrega una línea en blanco para mejorar la legibilidad de la salida.

ANIOS = 18 # Constante que define la mayoría de edad.

edad = int(input("Ingrese su edad: ").strip() or "0") # Se solicita al usuario que ingrese su edad, la linea fué modificada
                                                      # para controlar entradas vacías o nulas, si se ingresa vacío o nulo
                                                      # se asigna 0 como valor por defecto. 

print(end="\n") # Se agrega una línea en blanco para mejorar la legibilidad de la salida.

if edad > ANIOS: # Se verifica si la edad es mayor a 18.
    print("Es mayor de edad.", end="\n\n") # Si es mayor de edad, se muestra el mensaje correspondiente.

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

#  Ejercicio 2: Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#  mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

print("-- Programa para verificar si el usuario aprobó o desaprobó --", end="\n\n")
print(end="\n") # Se agrega una línea en blanco para mejorar la legibilidad de la salida.

NOTA_APROBACION = 6 # Constante que define la nota mínima para aprobar.

nota = float(input("Ingrese su nota: ").strip() or "0") # Se le solicita al usuario su nota.
                                                        # la linea fué modificada para controlar entradas vacías o nulas,
                                                        # si se ingresa vacío o nulo se asigna 0 como valor por defecto.

print(end="\n") # Se agrega una línea en blanco para mejorar la legibilidad de la salida.

if nota >= NOTA_APROBACION: # Se verifica si la nota es mayor o igual a 6.
    print("Aprobado.", end="\n\n") # Si la nota es mayor o igual a 6, se muestra el mensaje Aprobado.
else:
    print("Desaprobado.", end="\n\n") # Si la nota es menor a 6, se muestra el mensaje Desaprobado.

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 3: Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, 
# imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python 
# para evaluar si un número es par o impar.    

# Se agrega un mensaje inicial para el usuario.
print("-- Programa para verificar si el usuario ingresó un número par --", end="\n\n")
print(end="\n") # Se agrega una línea en blanco para mejorar la legibilidad de la salida.      

# Se solicita al usuario ingresar un número par.
numero = float(input("Por favor ingrese un número par:").strip() or "0") # Se solicita que se ingrese un número par.
                                                                         # La linea fué modificada para controlar entradas vacías o nulas, 
                                                                         # si se ingresa vacío o nulo se asigna 0 como valor por defecto. 

print(end="\n") # Se agrega una línea en blanco para mejorar la legibilidad de la salida.

esNumeroPar = (numero % 2 == 0) # Se evalúa si el número es par utilizando el operador módulo (%).

if esNumeroPar:
    print("Ha ingresado un número par.", end="\n\n") # Si el número es par, se muestra el mensaje correspondiente.
else:
    print("Por favor, ingrese un número par.", end= "\n\n") # Si el número no es par, se muestra un mensaje 
                                                            # solicitando que ingrese un número par.

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 4: Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# ●​ Niño/a: menor de 12 años.
# ●​ Adolescente: mayor o igual que 12 años y menor que 18 años.
# ●​ Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# ●​ Adulto/a: mayor o igual que 30 años.    

# Se agrega un mensaje inicial para el usuario.
print("-- Programa que solicite al usuario su edad e imprime por pantalla su categoria --", end="\n\n")
print(end="\n") # Se agrega una línea en blanco para mejorar la legibilidad de la salida.

edad = int(input("Por favor, ingrese su edad:").strip() or "0") # Se solicita al usuario su edad.
                                                                # La linea fué modificada para controlar entradas vacías o nulas,
                                                                # si se ingresa vacío o nulo se asigna 0 como valor por defecto.     

print(end="\n") # Se agrega una línea en blanco para mejorar la legibilidad de la salida.

if edad < 0:
    print("La edad ingresada no es válida. Por favor, ingrese una edad correcta.", end="\n\n") # Si la edad es negativa, se muestra este mensaje.
elif edad < 12:
    print("Usted pertenece a la categoria de Niño/a. ", end="\n\n") # Si la edad es menor a 12, se muestra este mensaje.
elif edad >= 12 and edad < 18:
    print("Usted pertenece a la categoria de Adolescente. ", end="\n\n") # Si la edad es mayor o igual a 12 y menor a 18, se muestra este mensaje.
elif edad >= 18 and edad < 30:
    print("Usted pertenece a la categoria de Adulto/a joven. ", end="\n\n") # Si la edad es mayor o igual a 18 y menor a 30, se muestra este mensaje.
else:
    if edad >= 30:
        print("Usted pertenece a la categoria de Adulto/a. ", end="\n\n") # Si la edad es mayor o igual a 30, se muestra este mensaje.

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 5: Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
# de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
# como una lista o un string.

# Se agrega un mensaje inicial para el usuario.
print("-- Programa para verificar si el usuario es mayor de edad --", end="\n\n")

passwd = input("Ingrese una contraseña de entre 8 y 14 caracteres: ") # Se solicita al usuario que ingrese una contraseña de entre 8 y 14 caracteres.

print(end="\n") # Se agrega una línea en blanco para mejorar la legibilidad de la salida.                                                                          
                                                                                                 
longpwd = len(passwd) # Se obtiene la longitud de la contraseña ingresada.

if longpwd >= 8 and longpwd <= 14: # Se verifica si la longitud está entre 8 y 14 caracteres (inclusive).
    print("Ha ingresado una contraseña correcta", end="\n\n") # Si la longitud es adecuada, se muestra un mensaje indicando que es correcta.
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres", end="\n\n") # Si la longitud no es adecuada, se muestra el mensaje solicitando una contraseña correcta.   

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 6: El paquete statistics de python contiene funciones que permiten tomar una lista de números
# y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el siguiente:
#
#   from statistics import mode, median, mean
#   mi_lista = [1,2,5,5,3]
#   mean(mi_lista)
#
# En la documentación oficial se puede encontrar más información sobre este paquete:
# https://docs.python.org/es/3.8/library/statistics.html.
# La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se
# pueden utilizar para predecir la forma de una distribución normal a partir del siguiente criterio:
# ●​ Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la
# mediana es mayor que la moda.
# ●​ Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez,
# la mediana es menor que la moda.
# ●​ Sin sesgo: cuando la media, la mediana y la moda son iguales.
# Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista
# numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
# hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
# Definir la lista numeros_aleatorios de la siguiente forma:
#
#   import random
#   numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
#
# Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de
# forma aleatoria.

# Se importan las librerias necesarias
import random
from statistics import mode, median, mean

# Se crea una lista con números numeros aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Obtenemos la moda, mediana y la media
moda = mode(numeros_aleatorios) 
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Se muestran los resultados obtenidos
print(f"Moda: {moda}, Mediana: {mediana}, Media: {media:.2f}", end="\n\n")

# Se evalua si hay sesgo positivo, negativo o no hay sesgo    
if (media > mediana) and (mediana > moda):
    print("Sesgo positivo o a la derecha", end="\n\n")
elif (media < mediana) and (mediana < moda):
    print("Sesgo negativo o a la izquierda", end="\n\n")    
elif ( media == mediana) and (mediana == moda):
    print("Sin sesgo", end="\n\n")    
else:
    print("No se puede determinar el sesgo", end="\n\n") # En el caso que no se cumpla ninguna de las condiciones anteriores se notifica.

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 7:  Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

frase = input("Por favor ingrese una frase o palabra: ").strip() # Se solicita al usuario que ingrese una frase o palabra y 
                                                                 #  se eliminan los espacios en blanco al inicio y al final.

print(end="\n") # Se agrega una línea en blanco para mejorar la legibilidad de la salida.

# Se verifica si la última letra es una vocal (mayúscula o minúscula).
if frase[-1].lower() in "aeiou":
    print(frase + "!", end="\n\n") # Si termina con vocal, se añade un signo de exclamación al final.
else:
    print(frase, end="\n\n") # Si no termina con vocal, se deja tal cual y se imprime.

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 8:  Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1.​ Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2.​ Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3.​ Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.    

# Se agrega un mensaje inicial para el usuario.
print("-- Programa para transformar el nombre ingresado de acuerdo a la opción seleccionada --", end="\n\n")
print(end="\n") # Se agrega una línea en blanco para mejorar la legibilidad de la salida.

nombre = input("Por favor, ingrese su nombre: ").strip() # Se solicita al usuario que ingrese su nombre y se eliminan los espacios del principio y final.
print(end="\n\n") # Se agrega una línea en blanco para mejorar la legibilidad de la salida.

if (nombre.strip() != "") and not(nombre.isdigit()): # Se verifica que el nombre no esté vacío o nulo.

    # Se lista las opciones disponibles para el usuario.
    print("Lista de opciones: ",end="\n\n")
    print("1: Para imprimir su nombre en mayúsculas.", end="\n\n")
    print("2: Para imprimir su nombre en minúsculas.", end="\n\n")
    print("3: Para imprimir su nombre con la primer letra en mayúscula.", end="\n\n")
    print(end="\n") # Se agrega una línea en blanco para mejorar la legibilidad de la salida.

    opcion = input("Ingrese una opción: ")
    print(end="\n") # Se agrega una línea en blanco para mejorar la legibilidad de la salida.

    # Se evalúa la opción seleccionada por el usuario y se muestra el nombre transformado según la opción.
    if opcion == "1":
        print(f"Su nombre en mayúsculas es: {nombre.upper()}", end="\n\n")
    elif opcion == "2":
        print(f"Su nombre en minúsculas es: {nombre.lower()}", end="\n\n")
    elif opcion == "3":
        print(f"Su nombre con la primer letra en mayúscula es: {nombre.title()}", end="\n\n")
    else:
        print("Opción inválida. Por favor, seleccione una opción válida (1, 2 o 3).", end="\n\n")   
else:   
    if nombre.isdigit():
        print("Se ingresó un número en lugar de un nombre. Por favor, intente nuevamente.", end="\n\n\n")
    else:
        print("No se ingresó ningún nombre. Por favor, intente nuevamente.", end="\n\n\n")      

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 9: Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
# ●​ Menor que 3: "Muy leve" (imperceptible).
# ●​ Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# ●​ Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
# ●​ Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
# ●​ Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# ●​ Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

# Se muestra un mensaje con la descripción del programa
print("-- Programa para imprimir la clasificación según la magnitud del terremoto --", end="\n\n")
print(end="\n") # Linea para mejorar la claridad del mensaje

magnitud = input("Por favor, ingrese la magnitud del terremoto (1,2,3,4,5,6 o 7): ")
print(end="\n\n") # Linea para mejorar la claridad del mensaje

if magnitud.isdigit(): # Se verifica que el valor ingresado sea un número

    # Se evalúa la magnitud ingresada y se imprime la clasificación correspondiente
    if int(magnitud) < 3:
        print("Categoria: Muy leve (imperceptible)", end="\n\n")
    elif (int(magnitud) >= 3) and (int(magnitud) < 4):
        print("Categoria: Leve (ligeramente perceptible)", end="\n\n")
    elif (int(magnitud) >= 4) and (int(magnitud) < 5):
        print("Categoria: Moderado (sentido por personas, pero generalmente no causa daños)", end="\n\n")
    elif (int(magnitud) >= 5) and (int(magnitud) < 6):
        print("Categoria: Fuerte (puede causar daños en estructuras débiles)", end="\n\n")
    elif (int(magnitud) >= 6) and (int(magnitud) < 7):
        print("Categoria: Muy Fuerte (puede causar daños significativos)", end="\n\n")
    elif int(magnitud) >= 7:
        print("Categoria: Extremo (puede causar graves daños a gran escala)", end="\n\n") 

else:
    print("No se ingresó un número, vuelva a intentarlo", end="\n\n") # Se informa que el valor ingresado no es un número   

# ------------------------------------------------------------------------------------------------------------------------------------------------------------

# Ejercicio 10: Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
# 
#  |-------------------------------------------|----------------------------|--------------------------|
#  |             Periodo del año               |       Estación en el       |      Estación en el      | 
#  |                                           |      hemisferio norte      |      hemisferio sur      | 
#  |-------------------------------------------|----------------------------|--------------------------|                                          
#  | Desde el 21 de diciembre hasta el 20 de   |         Invierno           |          Verano          |       
#  | marzo (incluidos)                         |                            |                          | 
#  |-------------------------------------------|----------------------------|--------------------------|
#  | Desde el 21 de marzo hasta el 20 de junio |         Primavera          |           Otoño          |
#  | (incluidos)                               |                            |                          | 
#  |-------------------------------------------|----------------------------|--------------------------|
#  | Desde el 21 de junio hasta el 20 de       |           Verano           |          Invierno        | 
#  | septiembre (incluidos)                    |                            |                          |
#  |-------------------------------------------|----------------------------|--------------------------|
#  | Desde el 21 de septiembre hasta el 20 de  |            Otoño           |          Primavera       | 
#  | diciembre (incluidos)                     |                            |                          |
#  |-------------------------------------------|----------------------------|--------------------------| 
#
# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. 
# El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.  

# Se muestra un mensaje con la descripción del programa
print("-- Programa para determinar la estación del año --\n")

# Se solicita la información al usuario
hemisferio = input("Ingrese el hemisferio en el que se encuentra N para Norte y S para Sur (N/S): ").strip().upper()
print(end="\n\n") # Se agrega una línea en blanco para mejorar la legibilidad de la salida.
mes = input("Ingrese el mes (ejemplo: marzo): ").strip().lower()
print(end="\n\n") # Se agrega una línea en blanco para mejorar la legibilidad de la salida.
dia = int(input("Ingrese el día del mes (1-31): "))
print(end="\n\n") # Se agrega una línea en blanco para mejorar la legibilidad de la salida.

# Convertimos los meses a números para simplificar
meses = {
    "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5, "junio": 6,
    "julio": 7, "agosto": 8, "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
}

if mes not in meses:
    print("Mes inválido. Intente nuevamente.") # Validamos el mes ingresado
else:
    mes_num = meses[mes]

    # Determinamos la estación en base a las fechas
    if (mes_num == 12 and dia >= 21) or (mes_num in (1, 2)) or (mes_num == 3 and dia <= 20):
        estacion_norte = "Invierno"
        estacion_sur = "Verano"
    elif (mes_num == 3 and dia >= 21) or (mes_num in (4, 5)) or (mes_num == 6 and dia <= 20):
        estacion_norte = "Primavera"
        estacion_sur = "Otoño"
    elif (mes_num == 6 and dia >= 21) or (mes_num in (7, 8)) or (mes_num == 9 and dia <= 20):
        estacion_norte = "Verano"
        estacion_sur = "Invierno"
    elif (mes_num == 9 and dia >= 21) or (mes_num in (10, 11)) or (mes_num == 12 and dia <= 20):
        estacion_norte = "Otoño"
        estacion_sur = "Primavera"
    else:
        estacion_norte = estacion_sur = "Desconocido"

    # Mostrar resultado según hemisferio elegido
    if hemisferio == "N":
        print(f"En el hemisferio norte, la estación es: {estacion_norte}\n")
    elif hemisferio == "S":
        print(f"En el hemisferio sur, la estación es: {estacion_sur}\n")
    else:
        print("Hemisferio inválido. Debe ingresar N para Norte o S para Sur.\n")
