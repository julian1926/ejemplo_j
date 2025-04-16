import gestorTarea as gt

def añadir_tarea():
    nombre = input("Ingrese el nombre de la tarea: ")
    responsable = input("Ingrese quién es el responsable de la tarea: ")
    while True:
        estado = input(f"Ingrese el estado de {nombre}, (pendiente, en progreso, completada): ").lower()
        if estado in ["pendiente", "en progreso", "completada"]:
            break
        else:
            print("El estado de la tarea que ingresó es incorrecto.")

    tarea = {"nombre": nombre, "responsable": responsable, "estado": estado}
    tareas = gt.cargarJson("tareas.json")  # Corregido: el nombre del archivo debe ser coherente
    tareas[tarea["nombre"]] = tarea
    gt.actualizarJson(tareas, "tareas.json")  # Corregido: el nombre del archivo debe ser coherente
    print("Proceso exitoso")

añadir_tarea()


