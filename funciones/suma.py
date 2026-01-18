def ejecutar():
    print("=== MÓDULO SUMA ===")
    n = int(input("¿Cuántos números desea sumar? "))
    total = 0

    for i in range(n):
        num = float(input(f"Ingrese el número {i + 1}: "))
        total += num

    print(f"\nLa suma total es: {total}")