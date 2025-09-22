# ------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#  Universidad Tecnológica Nacional - Tecnicatura Universitaria en Programación a Distancia
#
#                   Práctico 5: Listas
#
# Objetivo:
# Desarrollar la comprensión y la capacidad de manipular listas en Python mediante la aplicación
# de conceptos fundamentales como la indexación, la modificación de elementos, el uso de
# métodos integrados y el manejo de listas anidadas.
# 
# 1. Reconocer y aplicar correctamente la indexación y el slicing para acceder a elementos
# individuales o subconjuntos dentro de una lista.
# 2. Utilizar los métodos básicos de listas para crear, modificar y gestionar estructuras de
# datos simples.
# 3. Modificar listas mediante la actualización de valores y el manejo de listas anidadas,
# comprendiendo cómo acceder a datos en estructuras más complejas.
#
# Actividades
# NOTA: Siempre que se pida mostrar una lista o sus elementos, utilizar estructuras repetitivas.
#

# Ejercicio 1:
# 
# Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.

# Lista con las notas de 10 estudiantes
nota_estudiantes = [7, 8.5, 6, 9, 5.5, 10, 4, 8, 7.5, 6.5]  
print("Lista completa de notas:") # Muestra la lista completa
for nota in nota_estudiantes:
    nro_estudiante = nota_estudiantes.index(nota)    
    print(f"Estudiante {nro_estudiante + 1}: {nota} \n", end="" )
# Calcular y mostrar el promedio       
promedio = sum(nota_estudiantes) / len(nota_estudiantes)
print(f"\n\nPromedio: {promedio}")
# Se calcula la nota más alta y la más baja
nota_mas_alta = max(nota_estudiantes) 
nota_mas_baja = min(nota_estudiantes)
print(f"\nNota más alta: {nota_mas_alta}") # Se muestra la nota más alta   
print(f"\nNota más baja: {nota_mas_baja}") # Se muestra la nota más baja
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 2: 
# Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

print("Ingrese 5 productos:\n")

# Lista de los 5 productos
productos = []

for i in range(5):
    producto = input(f"Producto {i+1}: ").strip()
    productos.append(producto)

ordenados = sorted(productos)
print("\nLista de productos ordenada alfabéticamente:")
for i, p in enumerate(ordenados, start=1):
    print(f"  {i}. {p}")
    
# Se solicita al usuario el producto a aliminar    
prod_a_eliminar = input("Ingrese el nombre del producto que desea eliminar:").strip()

# Normalizamos todo a minúsculas para la comparación
coincidencia = None
for p in productos:
    if p.lower() == prod_a_eliminar.lower():
        coincidencia = p
        break
# Si el producto existe se elimina, si no se informa que no existe.
if coincidencia:
    productos.remove(coincidencia)
    print(f"\nProducto eliminado: {coincidencia}.")
else:
    print(f"\nEl producto '{prod_a_eliminar}' no se encontró en la lista.")    
    
    
    
# Se muestra la lista actualizada
print("\nLista de productos actualizada:")
for i, p in enumerate(productos, start=1):
    print(f"  {i}. {p}")  

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 3: Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.

# Se importa la librería random para la generación de números aleatorios
import random

# Se crean las listas para pares e impares
lst_par = []
lst_impar = []
# Se generan 100 números aleatorios entre 1 y 100 sin repetición
numeros = random.sample(range(1, 101), 100)
# Se muestra la lista generada
print("Lista de 100 números aleatorios:")
for i in numeros:
    indice = numeros.index(i)
    print(f"{indice +1}: {i}\n", end="")
# Separador   
print("\n\n")

# Separamos los números en pares e impares 
for i in numeros:   
    if i%2 == 0:
        lst_par.append(i)
    else:
        lst_impar.append(i)
# Se muestran las listas y la cantidad de números en cada una
print("Lista de números pares:") 
for i in lst_par:
    print(f"{i}\n", end="")
print(f"\nCantidad de números pares: {len(lst_par)}\n\n")

print("Lista de números impares:")
for i in lst_impar:
    print(f"{i}\n", end="")
print(f"\nCantidad de números impares: {len(lst_impar)}\n\n")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 4: Dada una lista con valores repetidos:
#
#  datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
#
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.

# Lista con valores repetidos
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

# Se crea una nueva lista para elementos sin duplicados
lst_sin_repetidos = []

# Se recorre la lista original y se agregan los elementos no repetidos a la nueva lista
for i in datos:
    if i not in lst_sin_repetidos:
        lst_sin_repetidos.append(i)
# Se muestra la lista sin elementos repetidos        
print("Lista sin elementos repetidos: \n") 
for i in lst_sin_repetidos:       
    print(f"{i},\n", end="")
# Se agrega un salto de línea al final para mejor presentación        
print("\n")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 5: Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.
#

# Lista de estudiantes
lst_estudiantes = []

# Se solicita al usuario ingresar los nombres de 8 estudiantes.
print("Por favor, ingrese los nombres de 8 estudiantes presentes en clase: ")
# Se cargan los nombres en la lista
for e in range(1,9):
    lst_estudiantes.append(input(f"Estudiante N° {e}: ").strip())

# Se muestra la lista de estudiantes ingresados
print("\n\nLista de estudiantes ingresados: \n")
    
for i in lst_estudiantes:
   print(f"{i}\n", end="")
   
print("\n")

#opcion = input("¿Desea agregar un nuevo estudiante (A) o eliminar uno existente (E)? Ingrese A o E: ").strip().upper()  

opcion = 'A' # Inicializo la variable para entrar al bucle.

# bucle para agregar o eliminar estudiantes dependiendo de la opción elegida.
while opcion in ['A', 'E', 'S']:
    opcion = input("\n¿Desea agregar un nuevo estudiante (A), eliminar uno existente (E) o Salir (S)? Ingrese A, E o S: ").strip().upper() 
    if opcion == 'A':
        estudiante = input("\nPor favor, ingrese el nombre del estudiante a agregar: ").strip()
        if estudiante not in lst_estudiantes:
            lst_estudiantes.append(estudiante)
            # Se muestra la lista actualizada.
            print("\nLista final actualizada de estudiantes: \n")
            for i in lst_estudiantes:
                print(f"{i}\n", end="")
        else:
            print(f"\nEl nombre del estudiante: {estudiante} ya existe, pruebe ingresarlo junto con su segundo nombre...")            
    elif opcion == 'E':
        estudiante = input("\nPor favor, ingrese el nombre del estudiante a eliminar: ").strip()
        if estudiante in lst_estudiantes:
            lst_estudiantes.remove(estudiante)
            # Se muestra la lista actualizada.
            print("\nLista final actualizada de estudiantes: \n")
            for i in lst_estudiantes:
                print(f"{i}\n", end="")
        else:
            print(f"\nEl nombre del estudiante: {estudiante} no existe, por favor compruebelo y vuelva a intentarlo.")            
    else:
        #print("\nSaliendo del programa...\n\n")
        break

# Se muestra la lista final actualizada.
print("\nLista final actualizada de estudiantes: \n")
for i in lst_estudiantes:
    print(f"{i}\n", end="")
# Se muestra un mensaje de salida.    
print("\nSaliendo del programa...\n\n")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 6: Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
# último pasa a ser el primero).
#

# Lista de números
lst_nros = [4, 5, 6, 7, 8, 9, 10]

# Se rota la lista
ultimo = lst_nros[-1]

# Se obtiene el resto de la lista sin el último elemento 
resto = lst_nros[:-1]

# Se crea la lista rotada
lst_rotada = [ultimo] + resto

# Se muestra la lista original y la lista rotada.
print("\nLista de números original: \n")
for n in lst_nros:
    print(f"{lst_nros.index(n)+1}: {n}\n", end="")


print("\nLista de números rotada: \n")
for n in lst_rotada:
    print(f"{lst_rotada.index(n)+1}: {n}\n", end="")

# Saltos de linea para mejorar la visualización.  
print("\n\n")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 7: Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.
#

# Matriz de temperaturas mínimas y máximas de una semana
matriz_temps = [[4,12],[6,16],[8,14],[2,8],[7,15],[5,12],[12,21]]

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Se muestran las temperaturas de la semana
print("Temperaturas mínimas y máximas de la semana (Mínima-Máxima):\n")
# Se obtiene la cantidad de filas y columnas de la matriz
cant_filas = len(matriz_temps)  
cant_columnas = len(matriz_temps[0])
# Inicializo las variables para el cálculo de promedios y la mayor amplitud térmica.
suma_minimas = 0
suma_maximas = 0
mayor_amplitud = -1
dia_mayor_amplitud = ""

# Se recorren las filas de la matriz para mostrar las temperaturas de la semana.
for fila in range(cant_filas):
    print(f"{dias_semana[fila]}: {matriz_temps[fila][0]}-{matriz_temps[fila][1]} °C")

# Se muestran las temperaturas mínimas y se calcula el promedio de las mismas.
print("\n\nTemperaturas mínimas: \n")
for fila in range(cant_filas):
    print(f"{dias_semana[fila]}: {matriz_temps[fila][0]} °C")
    suma_minimas += matriz_temps[fila][0] 

# Se muestra el promedio de temperaturas mínimas.
print(f"\nEl promedio de temperaturas mínimas es de: {round(suma_minimas/cant_filas,2)} °C.\n")    

# Se muestran las temperaturas máximas y se calcula el promedio de las mismas.
print("\nTemperaturas máximas: \n")
for fila in range(cant_filas):
    print(f"{dias_semana[fila]}: {matriz_temps[fila][1]} °C")
    suma_maximas += matriz_temps[fila][1]
# Se muestra el promedio de temperaturas máximas.
print(f"\nEl promedio de temperaturas máximas es de: {round(suma_maximas/cant_filas,2)} °C.\n")

# Se calcula la mayor amplitud térmica y el día en que ocurrió.
for fila in range(cant_filas):
    temp_min = matriz_temps[fila][0]
    temp_max = matriz_temps[fila][1]
    amplitud = temp_max - temp_min
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = dias_semana[fila]
# Se muestra la mayor amplitud térmica y el día en que ocurrió.
print(f"\nLa mayor amplitud térmica fue de {mayor_amplitud} °C y ocurrió el día {dia_mayor_amplitud}. \n")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 8: Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.
#

# Listas de estudiantes, materias y matriz de notas
lst_estudiantes = ["Ana", "Luis", "Marta", "Carlos", "Sofía"]
lst_materias = ["Matemática", "Física","Química"]
matriz_notas = [[7,6,4],[9,6,7],[5,7,6],[4,8,9],[9,7,8]]

# Cantidad de filas y columnas de la matriz
cant_filas = len(matriz_notas)
cant_colum = len(matriz_notas[0])

# Muestra las notas de los estudiantes
print(f"\nNotas de los estudiantes:\n")
for fila in range(cant_filas):        
    print(f"{lst_estudiantes[fila]}: {matriz_notas[fila][0]} {matriz_notas[fila][1]} {matriz_notas[fila][2]}")


# Promedio por estudiante
print("\n\nPromedio por estudiante:")
for fila in range(cant_filas):
    suma = 0
    for colum in range(cant_colum):
        suma += matriz_notas[fila][colum]
    promedio = suma / cant_colum
    print(f"\nEl promedio de {lst_estudiantes[fila]} es: {round(promedio,2)}")

# Promedio por materia
print("\n\nPromedio por materia:")
for colum in range(cant_colum):
    suma = 0
    for fila in range(cant_filas):
        suma += matriz_notas[fila][colum]
    promedio = suma / cant_filas
    print(f"\nEl promedio de {lst_materias[colum]} es: {round(promedio,2)}")
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 9: Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.
#

# Inicializa el tablero con guiones
tablero = [["-" for _ in range(3)] for _ in range(3)]

# Función para mostrar el tablero
def mostrar_tablero():
    for fila in tablero:
        print(" | ".join(fila))
    print()
# Se muestra un mensaje de bienvenida
print("Bienvenidos al juego Ta-Te-Ti!\n")
mostrar_tablero()

# bucle para controlar los turnos de los jugadores (X y O)
for turno in range(9):  # Máximo 9 jugadas
    jugador = "X" if turno % 2 == 0 else "O"
    print(f"Turno del jugador {jugador}")
    # Se solicita una posición hasta que sea válida
    while True:
        fila = int(input("Ingrese la fila (0-2): "))
        col = int(input("Ingrese la columna (0-2): "))
        
        # Valida que esté dentro del rango
        if fila not in [0,1,2] or col not in [0,1,2]:
            print("Posición inválida. Debe ser entre 0 y 2. Intente de nuevo.")
            continue
        
        # Verifica si la casilla está libre
        if tablero[fila][col] == "-":
            tablero[fila][col] = jugador
            break
        else:
            print("Casilla ocupada, intente de nuevo.")
    
    print("\n") # Salto de línea para mejor visualización
    
    # Se muestra el tablero actualizado
    mostrar_tablero()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 10: Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.
#

# Matriz 4x7 de ventas [producto][día]
ventas = [
    [10, 12, 8, 15, 20, 18, 25],   # Producto 1
    [5, 8, 12, 10, 15, 14, 16],    # Producto 2
    [20, 22, 25, 18, 24, 20, 30],  # Producto 3
    [7, 9, 11, 10, 13, 12, 14]     # Producto 4
]

# Listas de productos y días
productos = ["Producto 1", "Producto 2", "Producto 3", "Producto 4"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Se obtiene la cantidad de productos y días
cant_productos = len(ventas)  # 4
cant_dias = len(ventas[0])    # 7

# Se muestra el total vendido por cada producto
print("\nTotal vendido por cada producto:\n")
totales_productos = []
for i in range(cant_productos):
    total_prod = sum(ventas[i])
    totales_productos.append(total_prod)
    print(f"{productos[i]}: {total_prod}")

# Se muestra el día con mayores ventas totales
print("\nVentas totales por día:\n")
totales_dias = []
for j in range(cant_dias):
    total_dia = sum(ventas[i][j] for i in range(cant_productos))
    totales_dias.append(total_dia)
    print(f"{dias[j]}: {total_dia}")

mayor_ventas_dia = max(totales_dias)
dia_mayor = dias[totales_dias.index(mayor_ventas_dia)]
print(f"\nEl día con mayores ventas totales fue el {dia_mayor} con {mayor_ventas_dia} ventas.")

# Se muestra el producto más vendido en la semana
mayor_producto = max(totales_productos)
producto_mayor = productos[totales_productos.index(mayor_producto)]
print(f"\nEl producto más vendido en la semana fue el {producto_mayor} con {mayor_producto} ventas.\n\n")

# ------------------------------------------------------------------------------------------------------------------------------------------------------------