import gestor as g
print("hola que tal")

def mostrar_libros():
    libros = g.cargarJson("libros.json")
    if not libros:
        print("Lista de libros vacía.")
        return
    print("----- Lista de libros -----")
    for titulo, datos in libros.items():
        print(f'Título: {titulo}, Autor: {datos.get("autor", "Desconocido")}, Cantidad: {datos.get("cantidad", "N/A")}, Categoría: {datos.get("categoria", "Sin categoría")} ')




    


        


