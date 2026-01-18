def ejecutar():
    print("=== MÓDULO TABLAS DE MULTIPLICAR ===")
    n = int(input("Ingrese el número de la tabla que desea ver: "))
    print("")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

