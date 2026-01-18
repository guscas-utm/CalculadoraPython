def ejecutar():
    print("=== MÓDULO PRODUCTO ===")
    n = int(input("¿Cuántos números desea multiplicar? "))
    producto = 1

    for i in range(n):
        num = float(input(f"Ingrese el número {i + 1}: "))
        producto *= num

    print(f"\nEl producto total es: {producto}")