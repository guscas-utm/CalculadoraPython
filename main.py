# Importación de módulos
from funciones import suma
from funciones import producto
from funciones import division
from funciones import factorial
from funciones import tablas
from funciones import potencias
from funciones import promedio
from funciones import max_min

def mostrar_menu():
    print("\n==============================")
    print("  BIENVENIDO AL PROGRAMA")
    print("==============================")
    print("Seleccione una opción:")
    print("1. Suma de n números")
    print("2. Producto de n números")
    print("3. División entre 2 números")
    print("4. Factorial de un número")
    print("5. Tabla de multiplicar")
    print("6. Cuadrado y cubo de un número")
    print("7. Promedio de números")
    print("8. Máximo, mínimo y total de valores")
    print("9. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            suma.ejecutar()
        elif opcion == "2":
            producto.ejecutar()
        elif opcion == "3":
            division.ejecutar()
        elif opcion == "4":
            factorial.ejecutar()
        elif opcion == "5":
            tablas.ejecutar()
        elif opcion == "6":
            potencias.ejecutar()
        elif opcion == "7":
            promedio.ejecutar()
        elif opcion == "8":
            max_min.ejecutar()
        elif opcion == "9":
            print("Gracias por usar el programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

main()
