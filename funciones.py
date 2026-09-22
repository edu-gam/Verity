import json
#registra los items
def registrar_items():
    print(f"Registrar un item:\n")
    codigo = input("Ingrese el codigo del item:")
    titulo = input("Ingrese el titulo:")
    autor = input("Ingrese el autor:")
    categoria = input("Ingrese la categoria:")
    cantidad = int(input("Ingrese la cantidad total:"))
    ubicacion = input("Ingrese la ubicacion:")



#parte de sebas
import json


def listar_items():
    try:
        with open("inventario.json", "r", encoding="utf-8") as archivo:
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
    print("           LISTA DE ÍTEMS")
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
        
#lista los items
def listar_items():
    try:
        with open("inventario.json", "r", encoding="utf-8") as archivo:
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
    print("           LISTA DE ÍTEMS")
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