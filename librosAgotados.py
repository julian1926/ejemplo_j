
import gestor as g
print("triple f")
print("que bueno")
print("lalalalala")

def mostrar_libros_agotados():
    libros = g.cargarJson("libros.json")  # Corregido: la extensión debe ser .json
    agotados = []
    proximos_agotarse = []

    if not libros:
        print("Lista de libros vacía.")
        return

    for titulo, datos in libros.items():
        try:
            cantidad = int(datos['cantidad'])
            if cantidad <= 0:
                agotados.append(titulo)  # Corregido: agregar el título, no los datos completos
            elif 0 < cantidad <= 3:
                proximos_agotarse.append(titulo)  # Corregido: agregar el título
            # La rama 'else' con 'return' era incorrecta, la eliminé
        except (ValueError, KeyError) as e:
            print(f"Advertencia: No se pudo procesar la cantidad del libro '{titulo}'. Error: {e}")

    print("\n--- Libros Agotados ---")
    if agotados:
        for titulo in agotados:
            print(f"- {titulo}")
    else:
        print("No hay libros agotados.")

    print("\n--- Libros Próximos A Agotarse ---")
    if proximos_agotarse:
        for titulo in proximos_agotarse:
            print(f"- {titulo}")
    else:
        print("No hay libros próximos a agotarse.")

