from funciones import (
    cargar_csv,
    escribir_csv,
    menu,
    obtener_mapa_clases,
    listar_por_clase,
    listar_por_caracteristica,
    agregar_animal,
    mostrar_todos,
    crear_objetos_animales
)


def main():
    archivo_clases = "clases.csv"
    archivo_zoo = "zoo.csv"

    clases = cargar_csv(archivo_clases)
    animales = cargar_csv(archivo_zoo)

    mapa_clases = obtener_mapa_clases(clases)

    objetos_animales = crear_objetos_animales(animales, mapa_clases)

    while True:
        opcion = menu()

        if opcion == "1":
            listar_por_clase(animales, mapa_clases)

        elif opcion == "2":
            listar_por_caracteristica(animales)

        elif opcion == "3":
            agregar_animal(animales, mapa_clases)

        elif opcion == "4":
            mostrar_todos(animales, mapa_clases)

        elif opcion == "5":
            if animales:
                encabezados = list(animales[0].keys())
                escribir_csv(archivo_zoo, animales, encabezados)
            print("Cambios guardados. Saliendo del programa...")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()