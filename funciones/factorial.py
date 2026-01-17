def ejecutar():
    print("=== MÓDULO FACTORIAL ===")
    n = int(input("Ingrese un número entero positivo: "))

    if n < 0:
        print("\nEl factorial no está definido para números negativos.")
        return

    resultado = 1
    for i in range(1, n + 1):
        resultado *= i

    print(f"\nEl factorial de {n} es: {resultado}")
