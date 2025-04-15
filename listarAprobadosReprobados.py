import gestorArchivos as ga
print("hola")

def listar_aprobados_reprobados():
    estudiantes = ga.cargarJson("estudiantes.json")
    aprobados = []
    reprobados = []

    if not estudiantes:
        print("No hay estudiantes registrados.")
        return

    for identificacion, datos in estudiantes.items():
        try:
            nota = float(datos['nota_inicial'])
            if nota >= 60:
                aprobados.append(datos['nombre'])
            else:
                reprobados.append(datos['nombre'])
        except (ValueError, KeyError) as e:
            print(f"Advertencia: No se pudo procesar la nota del estudiante con ID {identificacion}. Error: {e}")

    print("\n--- Estudiantes Aprobados (Nota >= 60) ---")
    if aprobados:
        for nombre in aprobados:
            print(f"- {nombre}")
    else:
        print("No hay estudiantes aprobados.")

    print("\n--- Estudiantes Reprobados (Nota < 60) ---")
    if reprobados:
        for nombre in reprobados:
            print(f"- {nombre}")
    else:
        print("No hay estudiantes reprobados.")

