import gestorArchivos as ga
def actualizar_nota():
    print("hola que tal vamos a actualizar la nota ")
    identificacion_actualizar=input("ingrese la identificacion del estudiante que quiere actualizar la nota: ")
    estudiantes=ga.cargarJson("estudiantes.json")
    if not estudiantes:
        print("no hay estudiantes registrados")
        return
    if identificacion_actualizar in estudiantes:
           while True:
            nota_inicial = input("Ingrese la nueva nota del estudiante (0-100): ")
            try:
                nueva_nota = float(nota_inicial)
                if 0 <= nueva_nota <= 100:
                    estudiantes[identificacion_actualizar]['nota_inicial'] = nueva_nota
                    ga.updateJson(estudiantes, "estudiantes.json")
                    print(f"Nota del estudiante con identificación '{identificacion_actualizar}' actualizada a {nueva_nota}.")
                    break 
                else:
                    print("La nota debe estar entre 0 y 100. Intente de nuevo.")
            except ValueError:
                print("La nota ingresada no es válida. Intente de nuevo.")
             

       

