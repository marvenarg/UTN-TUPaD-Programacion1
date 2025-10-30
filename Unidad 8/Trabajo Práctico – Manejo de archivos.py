# ------------------------------------------------------------------------------------------------------------------------------------------------------------
#  Universidad Tecnológica Nacional - Tecnicatura Universitaria en Programación a Distancia
#  
#                    Práctico 8: Manejo de Archivos
#
#
# Objetivo:
#
# Comprender y aplicar el uso de archivos de texto en Python, desarrollando un pequeño programa 
# que lea, procese y almacene información sobre productos de manera persistente. Se busca que 
# el estudiante manipule datos a través de estructuras como listas y diccionarios, integrando 
# lectura, escritura y buenas prácticas con archivos.
#
# Resultados de aprendizaje:
#
# Lectura y escritura de archivos:
# El estudiante desarrollará la habilidad de leer y escribir información en archivos de
# texto mediante ejemplos prácticos, reconociendo los modos 'r', 'w' y 'a'.
#
# Manejo de estructuras de datos: Será capaz de convertir líneas de texto en listas y
# diccionarios, y manipular esta información en memoria de forma eficiente.
#
# Persistencia y reutilización de datos: Entenderá el concepto de persistencia de
# datos y será capaz de actualizar archivos sin borrar la información previa, reutilizando
# y modificando registros.
#
# Buenas prácticas al trabajar con archivos: Aplicará el uso de with open() para el
# manejo correcto de archivos y validará situaciones comunes como evitar sobrescritura
# accidental o errores de apertura.
#
# Actividades:
#
# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado
# productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad
#
# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
# formato:
#
#    Producto: Lapicera | Precio: $120.5 | Cantidad: 30
#
# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.
#
# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
# una lista llamada productos, donde cada elemento sea un diccionario con claves:
# nombre, precio, cantidad.
#
# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.
#
# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista.
#
# Consejo final:
#
# Antes de empezar, analizá cada problema y pensá cómo dividirlo en partes:
# 
#  ● Leer archivo
#  ● Procesar datos
#  ● Mostrar o actualizar información
#  ● Guardar los cambios
#
# Al terminar, probá tu programa varias veces:
#
#  ● ¿Se puede agregar más de un producto?
#  ● ¿Se guarda todo correctamente?
#  ● ¿Se muestra bien el resultado?
#
#  
# 

# Se importan las librerías necesarias
import os
from pathlib import Path

# Definición de la ruta del archivo
archivo = Path("productos.txt")

# Se definen las funciones necesarias

# ----------------- utilidades -----------------
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def pausar():
    input("\nPresione ENTER para volver al menú...")


def normalizar_nombre(s: str) -> str:
    return " ".join(s.strip().split())

# Consigna 4
def leer_archivo(ruta: Path) -> list[dict]:
    productos = []
    if not ruta.exists():
        return productos
    with ruta.open("r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            partes = [p.strip() for p in linea.split(",")]
            if len(partes) != 3:
                continue
            nombre, precio_s, cant_s = partes
            try:
                precio = float(precio_s)
                cantidad = int(cant_s)
            except ValueError:
                continue
            productos.append({"nombre": normalizar_nombre(nombre),
                              "precio": precio,
                              "cantidad": cantidad})
    return productos


def mostrar(productos: list[dict]) -> None:
    limpiar_pantalla()
    print("=== LISTADO DE PRODUCTOS ===\n")
    if not productos:
        print("(No hay productos cargados)\n")
    else:
        for p in productos:
            print(f"Producto: {p['nombre']} | Precio: ${p['precio']:.2f} | Cantidad: {p['cantidad']}")
    pausar()


def pedir_producto() -> dict | None:
    nombre = normalizar_nombre(input("Nombre (vacío para cancelar): "))
    if not nombre:
        return None
    while True:
        ps = input("Precio: ").strip().replace(",", ".")
        try:
            precio = float(ps)
            if precio < 0:
                raise ValueError
            break
        except ValueError:
            print("  → Precio inválido.")
    while True:
        cs = input("Cantidad: ").strip()
        if cs.isdigit():
            cantidad = int(cs)
            break
        print("  → Cantidad inválida. Ingresá un número entero.")
    return {"nombre": nombre, "precio": precio, "cantidad": cantidad}


def guardar_sobrescribiendo(ruta: Path, productos: list[dict]) -> None:
    with ruta.open("w", encoding="utf-8") as f:
        for p in productos:
            f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")


def append_en_archivo(ruta: Path, p: dict) -> None:
    with ruta.open("a", encoding="utf-8") as f:
        f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")


# ---------- crear archivo inicial si no existe ---------- 

# Consigna 1
if not archivo.exists():
    iniciales = [
        "Lapicera,120.5,30",
        "Cuaderno,950,15",
        "Regla,300,50",
    ]
    archivo.write_text("\n".join(iniciales) + "\n", encoding="utf-8")

productos = leer_archivo(archivo) # Consigna 2 y 4

# ----------------- menú principal -----------------
while True:
    limpiar_pantalla()
    print("".ljust(56, "-"))
    print("   MENÚ - GESTIÓN DE PRODUCTOS")
    print("".ljust(56, "-"))
    print(" 1) Mostrar productos") # Consigna 2
    print(" 2) Agregar producto") # Consigna 3
    print(" 3) Buscar producto por nombre") # Consigna 5
    print(" 4) Guardar") # Consigna 6
    print(" 5) Salir")
    print("".ljust(56, "-"))
    op = input("Opción: ").strip()

    if op == "1": # Consigna 2
        mostrar(productos)

    elif op == "2": # Consigna 3
        limpiar_pantalla()
        print("=== AGREGAR PRODUCTO ===\n")
        nuevo = pedir_producto()
        if nuevo:
            productos.append(nuevo)
            append_en_archivo(archivo, nuevo)
            print(f"\n✓ Producto '{nuevo['nombre']}' agregado correctamente.")
        else:
            print("\nOperación cancelada.")
        pausar()

    elif op == "3": # Consigna 5
        limpiar_pantalla()
        print("=== BUSCAR PRODUCTO ===\n")
        nombre = input("Ingrese el nombre del producto: ").strip().lower()
        encontrado = None
        for p in productos:
            if p["nombre"].lower() == nombre:
                encontrado = p
                break
        if encontrado:
            print(f"\n→ Producto: {encontrado['nombre']} | Precio: ${encontrado['precio']:.2f} | Cantidad: {encontrado['cantidad']}")
        else:
            print("\nNo se encontró ese producto.")
        pausar()

    elif op == "4": # Consigna 6
        guardar_sobrescribiendo(archivo, productos)
        print("\n✓ Archivo actualizado con los productos actuales.")
        pausar()

    elif op == "5": 
        conf = input("\n¿Guardar antes de salir? (s/n): ").strip().lower()
        if conf == "s":
            guardar_sobrescribiendo(archivo, productos)
            print("✓ Cambios guardados.")
        print("\nSaliendo...")
        break

    else:
        print("\nOpción inválida.")
        pausar()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------


