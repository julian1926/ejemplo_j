import gestorArchivos as ga
print ("vamos a ingresar un estudiante")


def agregar_estudiantes():
    nombre=input("ingrese el nombre del estudiante: ")
    identificacion=input("ingrese la identificacion: ")
    while True:
        nota_inicial = input("ingrese la nota del estudiante: ")
        try:
            nota_inicial = float(nota_inicial) 
            if 0 < nota_inicial < 100:
                break
            else:
                print("la nota tiene que ser de 0 a 100. Intente de nuevo.")
        except ValueError:
            print("la nota ingresada no es valida. Intente de nuevo.")

    estudiante={"nombre": nombre, "identificacion":identificacion, "nota_inicial":nota_inicial}
    estudiantes=ga.cargarJson("estudiantes.json")
    estudiantes[estudiante["identificacion"]]=estudiante
    ga.updateJson(estudiantes,"estudiantes.json")
    print("proceso exitoso")



