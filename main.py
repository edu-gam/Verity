#equipo verity

#cambio en el main
import json
from funciones import *


while True:
    print("=========================================")
    print("   BIBLIOSTOCK - BIBLIOTECA HORIZONTE")
    print("=========================================")
    print("1. Registrar ítem")
    print("2. Listar ítems")
    print("3. Buscar ítem")
    print("4. Registrar préstamo")
    print("5. Registrar devolución")
    print("6. Salir")
    print("==========================================")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_items()

    elif opcion == "2":
        listar_items()

    elif opcion == "3":
        print("Buscar ítem")

    elif opcion == "4":
        print("Registrar préstamo")

    elif opcion == "5":
        print("Registrar devolución")

    elif opcion == "6":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida")