def rectangulo_area():
    print("Vamos a calcular el área del rectángulo")
    try:
        longitud = float(input("Ingrese la longitud del rectángulo: "))
        ancho = float(input("Ingrese el ancho del rectángulo: "))
        area = longitud * ancho
        print(f"El área del rectángulo es {area}")
    except ValueError:
        print("Error: Por favor, ingrese números válidos para la longitud y el ancho.")

def rectangulo_perimetro():
    print("Vamos a calcular el perímetro del rectángulo")
    try:
        longitud = float(input("Ingrese la longitud del rectángulo: "))
        ancho = float(input("Ingrese el ancho del rectángulo: "))
        perimetro = 2 * (ancho + longitud)
        print(f'El perímetro del rectángulo es {perimetro}')
    except ValueError:
        print("Error: Por favor, ingrese números válidos para la longitud y el ancho.")

print("----- Bienvenido al menú -----")

while True:
    print("Seleccione una figura:")
    print("1. Rectángulo")
    print("2. Salir")  # Agregamos la opción de salir
    opcion = input("Ingrese la opción que desea realizar: ")

    if opcion == '1':
        rectangulo_area()
        rectangulo_perimetro()
    elif opcion == '2':
        print("¡Gracias por usar la calculadora!")
        break  # Sale del bucle while
    else:
        print("Opción incorrecta. Por favor, ingrese 1 o 2.")