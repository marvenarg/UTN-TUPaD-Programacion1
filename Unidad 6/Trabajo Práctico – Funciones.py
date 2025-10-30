# ------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Universidad Tecnológica Nacional - Tecnicatura Universitaria en Programación a Distancia
#  
#                    Práctico 6: Funciones en Python
#
# Objetivo:
# Comprender y aplicar el uso de funciones en la programación, desarrollando algoritmos que implementen modularidad, 
# reutilización de código y una organización estructurada para resolver problemas.
#
# Resultados de aprendizaje:
# 
# Fundamentos de las Funciones: A través de explicaciones teóricas y ejercicios prácticos, el estudiante desarrollará 
# habilidades para definir, llamar y reutilizar funciones en Python.
#
# Modularidad y Reutilización: El estudiante será capaz de descomponer problemas complejos en pequeñas unidades funcionales, 
# mejorando la claridad, mantenimiento y reutilización del código.
#
# Resolución de Problemas con Funciones: El estudiante aplicará funciones para resolver problemas computacionales que 
# involucren cálculos matemáticos, manipulación de datos y flujos de control más complejos.
#
# Buenas Prácticas: El estudiante aprenderá a estructurar el código usando funciones y a documentar adecuadamente cada una para 
# facilitar su comprensión.
#
# Actividades:
#

# Ejercicio 1:
# Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

# Función que imprime "Hola Mundo!"
def imprimir_hola_mundo():
    print("Hola Mundo!")    

# Llamada a la función desde el programa principal
imprimir_hola_mundo()    

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 2: 
# Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

# Función que devuelve un saludo personalizado
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Solicitar el nombre al usuario
nombre_usuario = input("Ingrese su nombre: ").strip()   
# Llamada a la función y mostrar el saludo
print(saludar_usuario(nombre_usuario))

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 3:
# Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima:
# “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con 
# los valores ingresados.

# Función que imprime la información personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Solicitar los datos al usuario
nombre = input("Ingrese su nombre: ").strip()
apellido = input("Ingrese su apellido: ").strip
edad = input("Ingrese su edad: ").strip()
residencia = input("Ingrese su lugar de residencia: ").strip()  

# Llamada a la función con los valores ingresados
informacion_personal(nombre, apellido, edad, residencia) 

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 4:
# Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

# Librería matemática para usar constantes y funciones matemáticas
import math

# Función que calcula el área del círculo
def calcular_area_circulo(radio):
    return math.pi * radio ** 2 

# Función que calcula el perímetro del círculo
def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio  

# Solicitar el radio al usuario
radio = float(input("Ingrese el radio del círculo: "))

# Llamada a las funciones y mostrar los resultados
area = calcular_area_circulo(radio) # Llamada a la función
perimetro = calcular_perimetro_circulo(radio) # Llamada a la otra función
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")  

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 5:
# Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# Función que convierte segundos a horas
def segundos_a_horas(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    return horas, minutos, segundos_restantes

# Solicitar al usuario los segundos
seg = input("Ingrese la cantidad de segundos: ").strip()

# Validar que sea un número válido
if seg.isdigit():
    seg = int(seg)
    h, m, s = segundos_a_horas(seg) # Llamada a la función
    print(f"{seg} segundos equivalen a {h} hora(s), {m} minuto(s) y {s} segundo(s).") # Mostrar el resultado
else:
    print("Debe ingresar un número válido de segundos.")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 6:
# Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

# Función que muestra la tabla de multiplicar
def tabla_multiplicar(numero):
    print(f"\nTabla de multiplicar del {numero}:")
    print("-" * 30)
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
    print("-" * 30)

# Solicitar número al usuario
num = input("Ingrese un número para ver la tabla de multiplicar del mismo: ").strip()

# Validar que sea un número entero
if num.isdigit() or (num.startswith('-') and num[1:].isdigit()):
    num = int(num)
    tabla_multiplicar(num) # Llamada a la función
else:
    print("Debe ingresar un número válido.")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 7:
# Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla
# con el resultado de la suma, resta, multiplicación y división.

# Función que realiza las operaciones básicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "Indefinida (no se puede dividir por cero)"
    return (suma, resta, multiplicacion, division)

# Solicitar los números al usuario
a = input("Ingrese el primer número: ").strip()
b = input("Ingrese el segundo número: ").strip()

# Validar que ambos sean números válidos
if (a.replace('.', '', 1).isdigit() or (a.startswith('-') and a[1:].replace('.', '', 1).isdigit())) and \
   (b.replace('.', '', 1).isdigit() or (b.startswith('-') and b[1:].replace('.', '', 1).isdigit())):
    
    a = float(a)
    b = float(b)
    
    resultados = operaciones_basicas(a, b) # Llamada a la función
    # Mostrar los resultados
    print("\nResultados de las operaciones básicas:")
    print("--------------------------------------")
    print(f"Suma: {resultados[0]}")
    print(f"Resta: {resultados[1]}")
    print(f"Multiplicación: {resultados[2]}")
    print(f"División: {resultados[3]}")
else:
    print("\nError: Debe ingresar números válidos.")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 8:
# Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

# Función que calcula el índice de masa corporal (IMC)
def calcular_imc(peso, altura):
    """Calcula el índice de masa corporal (IMC)."""
    imc = peso / (altura ** 2)
    return imc

# Solicitar datos al usuario
peso = input("Ingrese su peso en kilogramos: ").strip()
altura = input("Ingrese su altura en metros: ").strip()

# Validar que sean números positivos
if (peso.replace('.', '', 1).isdigit() and altura.replace('.', '', 1).isdigit()
    and float(peso) > 0 and float(altura) > 0):

    peso = float(peso)
    altura = float(altura)
    imc = calcular_imc(peso, altura) # Llamada a la función
    # Mostrar el resultado
    print(f"\nSu índice de masa corporal (IMC) es: {imc:.2f}")

else:
    print("\nError: Debe ingresar valores numéricos válidos y mayores que cero.")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 9:
# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función. 

# Función que convierte Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    """Convierte grados Celsius a Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Solicitar la temperatura al usuario
temp_celsius = input("Ingrese la temperatura en grados Celsius: ").strip()

# Validar que sea un número
if temp_celsius.replace('.', '', 1).replace('-', '', 1).isdigit():
    temp_celsius = float(temp_celsius)
    temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)
    print(f"\n{temp_celsius:.2f} °C equivalen a {temp_fahrenheit:.2f} °F.") # Mostrar el resultado
else:
    print("\nError: Debe ingresar un número válido (por ejemplo, -5 o 23.4).")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 10:
# Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.

# Función que calcula el promedio de tres números
def calcular_promedio(a, b, c):
    """Devuelve el promedio de tres números."""
    promedio = (a + b + c) / 3
    return promedio

# Solicitar los tres números al usuario
n1 = input("Ingrese el primer número: ").strip()
n2 = input("Ingrese el segundo número: ").strip()
n3 = input("Ingrese el tercer número: ").strip()

# Validar que los tres sean números
if (n1.replace('.', '', 1).replace('-', '', 1).isdigit() and
    n2.replace('.', '', 1).replace('-', '', 1).isdigit() and
    n3.replace('.', '', 1).replace('-', '', 1).isdigit()):

    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)
    # Se llama a la función para calcular el promedio
    promedio = calcular_promedio(n1, n2, n3)
    print(f"\nEl promedio de los tres números es: {promedio:.2f}") # Mostrar el resultado

else:
    print("\nError: Debe ingresar solo números válidos.")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------    