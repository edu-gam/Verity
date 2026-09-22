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


inventario = cargar_inventario()

def cargar_inventario():
    try:
        with open("inventario.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []


def guardar_inventario(inventario):
    with open("inventario.json", "w") as archivo:
        json.dump(inventario, archivo, indent=4)


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


inventario = cargar_inventario()

#registra los items

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

    print("Ítem registrado exitosamente.")
    print(item)



#parte de sebas
#lista los items
def listar_items(inventario):
    try:
        with open("archivo.json", "r", encoding="utf-8") as archivo:
            inventario = json.load(archivo)
    except FileNotFoundError:
        print("\nNo existe el archivo de inventario.")
        return
    except json.JSONDecodeError:
        print("\nEl archivo de inventario está vacío o tiene un formato incorrecto.")
        return

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

def buscar_item(inventario):
    busqueda = input("Ingrese el código o título del ítem: ")

    for item in inventario:
        if item["codigo"] == busqueda or item["titulo"].lower() == busqueda.lower():
            print("Ítem encontrado:")
            print("Código:", item["codigo"])
            print("Título:", item["titulo"])
            print("Autor:", item["autor"])
            print("Categoría:", item["categoria"])
            print("Cantidad disponible:", item["cantidad_disponible"])
            print("Ubicación:", item["ubicacion"])
            return

    print("No se encontró ningún ítem.")