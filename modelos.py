class Animal:
    def __init__(self, nombre_animal, caracteristicas, clase):
        self.nombre_animal = nombre_animal
        self.caracteristicas = caracteristicas  # diccionario
        self.clase = clase

    def __str__(self):
        caracteristicas_activas = []

        for nombre_caracteristica, valor in self.caracteristicas.items():
            if str(valor) == "1":
                caracteristicas_activas.append(nombre_caracteristica)

        return f"Animal: {self.nombre_animal} | Clase: {self.clase} | Características: {', '.join(caracteristicas_activas)}"

    def __repr__(self):
        return f"Animal(nombre_animal={self.nombre_animal!r}, clase={self.clase!r})"