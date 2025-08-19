# Ejercicio 1:  Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
#
print("-- Programa para imprimir 'Hola Mundo!' --", end="\n\n")
print("Hola mundo!")


# Ejercicio 2: Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
# el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
# por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f...) para
# realizar la impresión por pantalla. 

print("-- Programa para saludar al usuario --", end="\n\n")
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")


# Ejercicio 3: Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
# imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
# “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
# años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f...) para realizar
# la impresión por pantalla.

print("-- Programa para mostrar los datos personales ingresados --", end="\n\n")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar_residencia = input("Ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}.")


# Ejercicio 4:  Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.
import math

print("-- Programa para calcular el área y perímetro de un círculo en base al radio ingresado --", end="\n\n")
radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")      


# Ejercicio 5: Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

print("-- Programa para mostrar en horas, minutos y segundos un valor ingresado en segundos --", end="\n\n")
#segundos = int(input("Ingrese la cantidad de segundos: "))      
segundos = int(input("Ingrese la cantidad de segundos: ").strip() or 0) #Linea modificada para controlar entradas vacías o nulas
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60
print(f"{segundos} segundos equivalen a {horas} horas, {minutos} minutos y {segundos_restantes} segundos.")


# Ejercicio 6: Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
# multiplicar de dicho número.

print("-- Programa para mostrar la tabla de multiplicar de dicho del número ingresado --", end="\n\n")
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")      


# Ejercicio 7: Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

print("-- Programa para mostrar las operaciones con dos números enteros distintos de 0 --", end="\n\n")   
num1 = int(input("Ingrese un número entero distinto de 0: "))
num2 = int(input("Ingrese nuevamente un número entero distinto de 0: "))
if num1 != 0 and num2 != 0:
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    if num2 != 0:  # Evitar división por cero
        division = num1 / num2
        print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division:.2f}")
    else:
        print(f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: No se puede dividir por cero.")       


# Ejercicio 8:  Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo:
#       
#  IMC = peso en kg / (altura en m)²
#  

print("-- Cálculo de IMC --\n")
# En el caso de que el usuario ingrese la altura y el peso con comas en lugar de puntos, se reemplaza por puntos.
altura = float((input("Ingrese su altura en metros: ").strip().replace(',', '.') or '0'))
peso   = float((input("Ingrese su peso en kilogramos: ").strip().replace(',', '.') or '0'))
if altura <= 0 or peso <= 0:
    print("Altura y peso deben ser mayores que 0. No se puede calcular el IMC.")
else:
    imc = peso / (altura ** 2)
    print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")


# Ejercicio 9:  Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#
# Temperatura en Fahrenheit = (Temperatura en Celsius * 9/5) + 32
#
print("-- Programa para convertir una temperatura Celsius a Fahrenheit --", end="\n\n")
temperatura_celsius = float((input("Ingrese la temperatura en grados Celsius: ").strip().replace(',', '.') or '0'))
temperatura_fahrenheit = (temperatura_celsius * 9/5) + 32
print(f"La temperatura en grados Fahrenheit es: {temperatura_fahrenheit:.2f}")      


# Ejercicio 10: Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
print("-- Programa para calcular el promedio de 3 números. --", end="\n\n")
num1 = float((input("Ingrese el primer número: ").strip().replace(',', '.') or '0'))
num2 = float((input("Ingrese el segundo número: ").strip().replace(',', '.') or '0'))
num3 = float((input("Ingrese el tercer número: ").strip().replace(',', '.') or '0'))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los números ingresados es: {promedio:.2f}")  