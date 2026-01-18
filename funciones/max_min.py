def ejecutar():
    print("=== MÓDULO MÁXIMO Y MÍNIMO ===")
    n = int(input("¿Cuántos números desea ingresar? "))
    numeros = []

    for i in range(n):
        num = int(input(f"Ingrese el número {i + 1}: "))
        numeros.append(num)

    print(f"\nValor máximo: {max(numeros)}")
    print(f"Valor mínimo: {min(numeros)}")
    print(f"Total de valores ingresados: {len(numeros)}")