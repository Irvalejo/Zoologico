import csv
from modelos import Animal


def cargar_csv(ruta_archivo):
    datos = []
    with open(ruta_archivo, mode="r", encoding="utf-8-sig", newline="") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            datos.append(dict(fila))
    return datos


def escribir_csv(ruta_archivo, datos, encabezados):

    with open(ruta_archivo, mode="w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=encabezados)
        escritor.writeheader()
        escritor.writerows(datos)


def menu():
    print("\n----- ZOOLÓGICO -----")
    print("1. Listar animales por clase")
    print("2. Listar animales por característica")
    print("3. Agregar nuevo animal")
    print("4. Mostrar todos los animales")
    print("5. Salir")
    opcion = input("Selecciona una opción: ")
    return opcion


def obtener_mapa_clases(lista_clases):
    mapa = {}
    for fila in lista_clases:
        mapa[fila["Clase_id"]] = fila["Clase_tipo"]
    return mapa


def crear_objetos_animales(lista_animales, mapa_clases):
    animales_obj = []
    for fila in lista_animales:
        clase_id = fila["clase"]
        clase_nombre = mapa_clases.get(clase_id, f"Clase {clase_id}")

        caracteristicas = {}
        for clave, valor in fila.items():
            if clave not in ["nombre_animal", "clase"]:
                caracteristicas[clave] = valor

        animal = Animal(fila["nombre_animal"], caracteristicas, clase_nombre)
        animales_obj.append(animal)

    return animales_obj


def listar_por_clase(lista_animales, mapa_clases):
    print("\nClases disponibles:")
    for clase_id, clase_nombre in mapa_clases.items():
        print(f"{clase_id}. {clase_nombre}")

    clase_buscada = input("Ingresa el número de la clase: ").strip()

    if clase_buscada not in mapa_clases:
        print("Clase no válida.")
        return

    print(f"\nAnimales de la clase {mapa_clases[clase_buscada]}:")
    encontrados = False

    for animal in lista_animales:
        if animal["clase"] == clase_buscada:
            print(f"- {animal['nombre_animal']}")
            encontrados = True

    if not encontrados:
        print("No se encontraron animales de esa clase.")


def obtener_caracteristicas_disponibles(lista_animales):
    if not lista_animales:
        return []
    return [col for col in lista_animales[0].keys() if col not in ["nombre_animal", "clase"]]


def listar_por_caracteristica(lista_animales):
    caracteristicas = obtener_caracteristicas_disponibles(lista_animales)

    print("\nCaracterísticas disponibles:")
    for i, c in enumerate(caracteristicas, start=1):
        print(f"{i}. {c}")

    try:
        opcion = int(input("Selecciona el número de la característica: "))
        if opcion < 1 or opcion > len(caracteristicas):
            print("Opción inválida.")
            return
    except ValueError:
        print("Debes ingresar un número.")
        return

    caracteristica_buscada = caracteristicas[opcion - 1]

    print(f"\nAnimales con la característica '{caracteristica_buscada}':")
    encontrados = False

    for animal in lista_animales:
        if animal[caracteristica_buscada] == "1":
            print(f"- {animal['nombre_animal']}")
            encontrados = True

    if not encontrados:
        print("No se encontraron animales con esa característica.")


def agregar_animal(lista_animales, mapa_clases):
    print("\n----- AGREGAR NUEVO ANIMAL -----")
    nombre = input("Nombre del animal: ").strip()

    if not nombre:
        print("El nombre no puede estar vacío.")
        return

    print("\nClases disponibles:")
    for clase_id, clase_nombre in mapa_clases.items():
        print(f"{clase_id}. {clase_nombre}")

    clase = input("Selecciona el número de la clase: ").strip()

    if clase not in mapa_clases:
        print("Clase inválida.")
        return

    caracteristicas = obtener_caracteristicas_disponibles(lista_animales)

    nuevo_animal = {"nombre_animal": nombre}

    print("\nResponde con 1 = sí, 0 = no")
    for c in caracteristicas:
        while True:
            valor = input(f"{c}: ").strip()
            if valor in ["0", "1"]:
                nuevo_animal[c] = valor
                break
            print("Entrada inválida. Usa 1 o 0.")

    nuevo_animal["clase"] = clase
    lista_animales.append(nuevo_animal)

    print(f"\nAnimal '{nombre}' agregado correctamente.")


def mostrar_todos(lista_animales, mapa_clases):
    print("\n----- LISTADO COMPLETO -----")
    for animal in lista_animales:
        clase_nombre = mapa_clases.get(animal["clase"], "Desconocida")
        print(f"- {animal['nombre_animal']} ({clase_nombre})")