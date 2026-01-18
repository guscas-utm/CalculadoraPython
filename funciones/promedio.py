def ejecutar():
    print("=== MÓDULO PROMEDIO ===")
    suma = 0
    contador = 0

    while True:
        num = float(input("Ingrese un número (-1 para terminar): "))
        if num == -1:
            break
        suma += num
        contador += 1

    if contador > 0:
        print(f"\nEl promedio es: {suma / contador}")
    else:
        print("\nNo se ingresaron números para calcular el promedio.")
