# ------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Universidad Tecnológica Nacional - Tecnicatura Universitaria en Programación a Distancia
#  
#                    Práctico 7: Estructuras de datos complejas
#
# Objetivo:
# Dominar el uso de estructuras de datos complejas en Python para almacenar, 
# organizar y manipular datos de manera eficiente, aplicando buenas prácticas y 
# optimizando el rendimiento de las aplicaciones.
#
# Resultados de aprendizaje:
# 1. Comprensión y aplicación de iterables: listas, tuplas y sets.
# 2. Introducción a estructuras de datos complejas: diccionarios.
#

# Actividades
# Ejercicio 1:
#  Dado el diccionario precios_frutas
#    precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#  Añadir las siguientes frutas con sus respectivos precios:
#    ● Naranja = 1200
#    ● Manzana = 1500
#    ● Pera = 2300

# Título del ejercicio
titulo ="Ejercicio 1 - Listado de precios de frutas"
print(f"\n{titulo}\n")
print("-" * len(titulo))
print("\n")

# Diccionario inicial
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450
}

# Agregar nuevas frutas con sus precios
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Mostrar el resultado final
print("\nPrecios de frutas actualizados:\n")
print(precios_frutas)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 2:
# Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

# Título del ejercicio
titulo ="Ejercicio 2 - Listado de precios de frutas que permiten actualizarse"
print(f"\n{titulo}\n")
print("-" * len(titulo))
print("\n")

# Diccionario existente
precios_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1500,
    'Pera': 2300
}

# Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Mostrar el resultado actualizado
print("\nPrecios de frutas actualizados:\n")
print(precios_frutas)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 3:
# Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

# Título del ejercicio
titulo ="Ejercicio 3 - Listado de de frutas sin precios"
print(f"\n{titulo}\n")
print("-" * len(titulo))
print("\n")

# Diccionario actual
precios_frutas = {
    'Banana': 1330,
    'Ananá': 2500,
    'Melón': 2800,
    'Uva': 1450,
    'Naranja': 1200,
    'Manzana': 1700,
    'Pera': 2300
}

# Crear una lista solo con las frutas (las claves del diccionario)
frutas = list(precios_frutas.keys())

# Mostrar la lista resultante
print("\nLista de frutas:\n")
print(frutas)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 4:
# Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.
# Ejemplo:
#
#    contactos = {"Juan": "123456", "Ana": "987654"}
#    # Consultar: "Juan" -> muestra "123456"
#

# Título del ejercicio
titulo ="Ejercicio 4 - Agenda telefónica"
print(f"\n{titulo}\n")
print("-" * len(titulo))
print("\n")

# Crear el diccionario vacío
contactos = {}

# Cargar 5 contactos
print("=== Carga de contactos ===")
for i in range(5):
    nombre = input(f"\nIngrese el nombre del contacto {i+1}: ").strip().capitalize() # Se solicita el nombre del contacto
    telefono = input(f"Ingrese el número telefónico de {nombre}: ").strip() # Se solicita el número telefónico
    
    if nombre != "" and telefono != "":
        contactos[nombre] = telefono
    else:
        print("\nNombre o número inválido. Intente nuevamente.") # Si dato es inválido se avisa al usuario
        i -= 1  # Repite la iteración

# Consultar contacto
print("\n=== Consulta de contactos ===")
consulta = input("Ingrese el nombre del contacto que desea buscar: ").strip().capitalize()

if consulta in contactos:
    print(f"\nEl número de {consulta} es: {contactos[consulta]}\n") # Si el contacto existe se muestra el número asociado
else:
    print(f"\nNo se encontró el contacto '{consulta}' en la agenda.\n") # Si el contacto no existe se informa al usuario

# Mostrar todos los contactos cargados (opcional)
print("\nContactos guardados:")
for nombre, telefono in contactos.items():
    print(f"- {nombre}: {telefono}")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------    
# Ejercicio 5:
# Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.
# Ejemplo:
#            
#   #Entrada -> "hola mundo hola"
# 
#   #Salida:
#   Palabras_únicas: {'hola', 'mundo'} 
#   Recuento: {'hola': 2, 'mundo': 1}   

# Título del ejercicio
titulo ="Ejercicio 5 - Análisis de la frase ingresada"
print(f"\n{titulo}\n")
print("-" * len(titulo))
print("\n")

# Solicitar la frase al usuario
frase = input("Ingrese una frase: ").strip().lower()

# Separar las palabras
palabras = frase.split()

# Obtener las palabras únicas (sin repetir)
palabras_unicas = set(palabras)

# Crear un diccionario con el recuento de palabras
recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

# Mostrar resultados
print("\nPalabras únicas:", palabras_unicas)
print("Recuento:", recuento)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 6:
# Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.
# Ejemplo:
# 
#  alumnos = {
#      "Sofía": (10, 9, 8),
#      "Luis": (6, 7, 7)
#  }
#

# Título del ejercicio
titulo ="Ejercicio 6 - Promedios de alumnos"
print(f"\n{titulo}\n")
print("-" * len(titulo))
print("\n")

# Diccionario para almacenar los alumnos y sus notas
alumnos = {}

# Cargar datos de los 3 alumnos
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ").strip().capitalize()
    notas = []

    # Ingresar las 3 notas del alumno
    for j in range(3):
        while True:
            nota = input(f"Ingrese la nota {j+1} de {nombre}: ").strip()
            if nota.replace('.', '', 1).isdigit():  # Permite enteros o decimales
                notas.append(float(nota))
                break
            else:
                print("\nIngrese un número válido.")

    # Guardar las notas como tupla en el diccionario
    alumnos[nombre] = tuple(notas)

# Mostrar el promedio de cada alumno
print("\n=== Promedio de cada alumno ===")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: promedio = {promedio:.2f}")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 7:
# Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
#

# Título del ejercicio
titulo ="Ejercicio 7 - Análisis de estudiantes aprobados en parciales"
print(f"\n{titulo}\n")
print("-" * len(titulo))
print("\n")

# Sets de números representando alumnos aprobados
parcial1 = {1, 2, 3, 5, 7}
parcial2 = {3, 4, 5, 8}

# 1. Estudiantes que aprobaron ambos parciales
ambos = parcial1 & parcial2 # intersección
print("\nAprobados en ambos parciales:", ambos)

# 2. Estudiantes que aprobaron solo uno de los dos
solo_uno = parcial1 ^ parcial2 # diferencia simétrica
print("\nAprobados solo en uno de los dos parciales:", solo_uno)

# 3. Estudiantes que aprobaron al menos un parcial (sin repetir)
al_menos_uno = parcial1 | parcial2 # unión
print("\nAprobados en al menos un parcial:", al_menos_uno)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 8:
# Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
#  • Consultar el stock de un producto ingresado.
#  • Agregar unidades al stock si el producto ya existe.
#  • Agregar un nuevo producto si no existe.
#

# Título del ejercicio
titulo ="Ejercicio 8 - Sistema de control de stock"
print(f"\n{titulo}\n")
print("-" * len(titulo))
print("\n")


# Diccionario inicial con productos y su stock (en minúsculas)
stock_productos = {
    "martillos": 10,
    "destornilladores": 5,
    "tornillos": 300,
    "clavos": 500,
    "arandelas": 200
}

# Mostrar el estado inicial del stock
print("\nEstado actual del stock:")
for prod, cant in stock_productos.items():
    print(f" - {prod.capitalize()}: {cant} unidades")
print("\n")

# Solicitar al usuario el producto a consultar
producto = input("\nIngrese el nombre del producto: ").strip().lower()

# Verificar si el producto existe
if producto in stock_productos:
    print(f"\nEl producto '{producto}' tiene {stock_productos[producto]} unidades en stock.")
    
    # Permitir agregar unidades al stock existente
    agregar = input("¿Desea agregar unidades al stock? (s/n): ").strip().lower()
    if agregar == "s":
        cantidad = input("Ingrese la cantidad a agregar: ").strip()
        if cantidad.isdigit():
            stock_productos[producto] += int(cantidad)
            print(f"\nStock actualizado de '{producto}': {stock_productos[producto]} unidades.")
        else:
            print("\nError: Debe ingresar un número válido.")
    else:
        print("\nNo se realizaron cambios en el stock.")
else:
    # Si el producto no existe, permitir agregarlo
    print(f"\nEl producto '{producto}' no existe en el inventario.")
    agregar_nuevo = input("¿Desea agregarlo al stock? (s/n): ").strip().lower()
    if agregar_nuevo == "s":
        cantidad = input("Ingrese la cantidad inicial: ").strip()
        if cantidad.isdigit():
            stock_productos[producto] = int(cantidad)
            print(f"\nProducto '{producto}' agregado con {cantidad} unidades.")
        else:
            print("\nError: Debe ingresar un número válido.")
    else:
        print("\nNo se agregó ningún producto nuevo.")

# Mostrar el estado final del stock
print("\nEstado actual del stock:")
for prod, cant in stock_productos.items():
    print(f" - {prod.capitalize()}: {cant} unidades")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejrecicio 9:
# Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
# Ejemplo:
#
#   agenda = {
#       ("lunes", "10:00"): "Reunión",
#       ("martes", "15:00"): "Clase de inglés"
#   }
#
# Permití consultar qué actividad hay en cierto día y hora.

# Título del ejercicio
titulo ="Ejercicio 9 - Agenda semanal"
print(f"\n{titulo}\n")
print("-" * len(titulo))
print("\n")

# Diccionario base
agenda = {
    ("lunes", "10:00"): "Reunión de trabajo",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "18:00"): "Gimnasio"
}

# Mostrar agenda inicial
print("\nAgenda actual:")
for clave, evento in agenda.items():
    dia, hora = clave
    print(f" - {dia.capitalize()} {hora}: {evento}")

# Consulta
print("\n=== Consultar actividad ===")
dia_consulta = input("Ingrese el día: ").strip().lower() # Solicitar día al usuario
hora_consulta = input("Ingrese la hora (formato HH:MM): ").strip() # Solicitar hora al usuario

clave_consulta = (dia_consulta, hora_consulta) # Crear la tupla clave para la consulta

if clave_consulta in agenda:
    print(f"\nEl {dia_consulta} a las {hora_consulta} tenés: {agenda[clave_consulta]}") # Si hay actividad registrada se muestra al usuario
else:
    print(f"\nNo hay actividades registradas el {dia_consulta} a las {hora_consulta}.") # Si no hay actividad registrada se informa al usuario

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ejercicio 10:
# Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
#  • Las capitales sean las claves.
#  • Los países sean los valores.
# 
# Ejemplo:
#   
#   original = {"Argentina": "Buenos Aires", "Chile": "Santiago"} 
#   invertido = {"Buenos Aires": "Argentina", "Santiago": "Chile"}
#  

# Título del ejercicio
titulo ="Ejercicio 10 - Invertir un diccionario de países y capitales"
print(f"\n{titulo}\n")
print("-" * len(titulo))
print("\n")

# Diccionario original
paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción"
}

# Invertir el diccionario
invertido = {}

for pais, capital in paises.items():
    invertido[capital] = pais

# Mostrar ambos diccionarios
print("\nDiccionario original (País → Capital):\n")
print(f"{paises}\n\n")

print("\nDiccionario invertido (Capital → País):\n")
print(f"{invertido}\n")

# --------------------------------------------------------------------------------------------------------------------------------------------------------------