import gestor as g

def prestar_libro():
    print("----- Aqui estan los Libros disponibles -----")
    libros = g.cargarJson("libros.json")

    if not libros:
        print("No hay libros disponibles.")
        return

    for titulo, detalles in libros.items():
        print(f'- Título: {titulo}, Cantidad: {detalles["cantidad"]}')

    titulo_prestar = input("Ingrese el título del libro que desea prestar: ")

    if titulo_prestar in libros:
        while True:
            cantidad_prestar_str = input(f"Ingrese la cantidad de '{titulo_prestar}' que desea prestar: ")
            try:
                cantidad_prestar = int(cantidad_prestar_str)
                if cantidad_prestar > 0:
                    if cantidad_prestar <= libros[titulo_prestar]["cantidad"]:
                        libros[titulo_prestar]["cantidad"] -= cantidad_prestar
                        g.actualizarJson(libros, "libros.json")
                        print(f"Se han prestado {cantidad_prestar} copias de '{titulo_prestar}'.")
                        break  # Salir del bucle de cantidad
                    else:
                        print("Cantidad de libros insuficiente.")
                else:
                    print("La cantidad a prestar debe ser mayor que 0.")
            except ValueError:
                print("Por favor, ingrese una cantidad válida (número entero).")
    else:
        print(f"El libro '{titulo_prestar}' no está registrado.")


         



    