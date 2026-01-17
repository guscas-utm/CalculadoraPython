def ejecutar():
    print("=== MÓDULO DIVISIÓN ===")
    a = float(input("Ingrese el numerador: "))
    b = float(input("Ingrese el denominador: "))

    if b == 0:
        print("\nError: no se puede dividir entre cero.")
    else:
        print(f"\nEl resultado de la división es: {a / b}")
