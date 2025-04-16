import gestor as g
def buscarLibro():
    print("vamos a buscar un libro")
    print("vacio")
    libro_buscar=input("ingrese el titulo del libro que desea buscar: ")
    libros=g.cargarJson("libros.json")
    if not libros:
        print("lista de libros vacia")
        return
    if libro_buscar in libros:
        datos_libro=libros[libro_buscar]
        print("----datos del libro-----")
        print(f'Título: {libro_buscar}, Autor: {datos_libro.get("autor", "Desconocido")}, Cantidad: {datos_libro.get("cantidad", "N/A")}, Categoría: {datos_libro.get("categoria", "Sin categoría")} ')
    else:
        print(f"no se encontro ningun libro con el titulo {libro_buscar}")





    

