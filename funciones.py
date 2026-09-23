import json


def cargar_inventario():
    try:
        with open("inventario.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []


def guardar_inventario(inventario):
    with open("inventario.json", "w") as archivo:
        json.dump(inventario, archivo, indent=4)


# Registra los items
def registrar_item(inventario):
    codigo = input("Ingrese el código del ítem: ")
    titulo = input("Ingrese el título: ")
    autor = input("Ingrese el autor: ")
    categoria = input("Ingrese la categoría: ")
    cantidad = int(input("Ingrese la cantidad total: "))
    ubicacion = input("Ingrese la ubicación: ")

    item = {
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "cantidad_total": cantidad,
        "cantidad_disponible": cantidad,
        "ubicacion": ubicacion
    }

    inventario.append(item)
    guardar_inventario(inventario)

    print("Ítem registrado exitosamente.")


# Lista los items
def listar_items(inventario):

    if not inventario:
        print("\nNo hay ítems registrados en el inventario.")
        return

    print("\n==========================================")
    print("             LISTA DE ÍTEMS")
    print("==========================================")

    for item in inventario:
        print(f"Código: {item['codigo']}")
        print(f"Título: {item['titulo']}")
        print(f"Autor: {item['autor']}")
        print(f"Categoría: {item['categoria']}")
        print(f"Cantidad total: {item['cantidad_total']}")
        print(f"Cantidad disponible: {item['cantidad_disponible']}")
        print(f"Ubicación: {item['ubicacion']}")
        print("------------------------------------------")


# Busca los items
def buscar_item(inventario):
    busqueda = input("Ingrese el código o título del ítem: ")

    for item in inventario:
        if item["codigo"] == busqueda or item["titulo"].lower() == busqueda.lower():
            print("\nÍtem encontrado:")
            print("Código:", item["codigo"])
            print("Título:", item["titulo"])
            print("Autor:", item["autor"])
            print("Categoría:", item["categoria"])
            print("Cantidad disponible:", item["cantidad_disponible"])
            print("Ubicación:", item["ubicacion"])
            return

    print("No se encontró ningún ítem.")


# Carga el inventario al iniciar
inventario = cargar_inventario()

def cargar_prestamos():
    try:
        with open("prestamos.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

inventario = cargar_inventario()
prestamos = cargar_prestamos()  

from datetime import datetime


def manejar_json(archivo, datos=None):
    if datos is None:
        try:
            with open(archivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)


def registrar_prestamo(inventario, prestamos):
    busqueda = input("Código o título del ítem a prestar: ").strip().lower()

    # Buscar el ítem en el inventario
    item = next(
        (
            i
            for i in inventario
            if i["codigo"].lower() == busqueda
            or i["titulo"].lower() == busqueda
        ),
        None,
    )

    if not item:
        print("Error: Ítem no encontrado.")
        return

    if item.get("cantidad_disponible", 0) <= 0:
        print(f"Error: No hay copias disponibles de '{item['titulo']}'.")
        return

    usuario = input("Nombre del usuario: ").strip()
    if not usuario:
        print("Error: El nombre del usuario no puede estar vacío.")
        return

    # Actualizar la cantidad en el inventario
    item["cantidad_disponible"] -= 1

    # Registrar el préstamo
    prestamo = {
        "codigo_item": item["codigo"],
        "titulo_item": item["titulo"],
        "usuario": usuario,
        "fecha_prestamo": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "estado": "Activo",
    }

    prestamos.append(prestamo)

    # Persistir los cambios en los archivos JSON
    manejar_json("inventario.json", inventario)
    manejar_json("prestamos.json", prestamos)

    print(
        f"Préstamo del libro '{item['titulo']}' registrado con éxito a {usuario}."
    )


def registrar_devolucion(inventario, prestamos):
    busqueda = (
        input("Nombre del usuario o código del ítem a devolver: ")
        .strip()
        .lower()
    )

    prestamo = next(
        (
            p
            for p in prestamos
            if (
                p["usuario"].lower() == busqueda
                or p["codigo_item"].lower() == busqueda
            )
            and p["estado"] == "Activo"
        ),
        None,
    )

    if not prestamo:
        print("Error: No se encontró ningún préstamo activo con ese criterio.")
        return

    # Marcar el préstamo como devuelto
    prestamo["estado"] = "Devuelto"
    prestamo["fecha_devolucion"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Restaurar la disponibilidad en el inventario
    for item in inventario:
        if item["codigo"] == prestamo["codigo_item"]:
            item["cantidad_disponible"] += 1
            break

    # Persistir los cambios en los archivos JSON
    manejar_json("inventario.json", inventario)
    manejar_json("prestamos.json", prestamos)

    print(
        f"Devolución del ítem '{prestamo['titulo_item']}' procesada con éxito."
    )