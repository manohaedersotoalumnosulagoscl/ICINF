lista = []

while True:
    print("\nMenu de opciones:")
    print("1. Ingresar un elemento a la lista")
    print("2. Modificar un elemento de la lista según el índice")
    print("3. Eliminar un elemento de la lista según el índice")
    print("4. Eliminar el último elemento de la lista")
    print("5. Buscar un elemento de la lista según el dato (devuelve el índice)")
    print("6. Mostrar todos los elementos de la lista")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        lista.append(input("Ingrese el elemento a añadir: "))
    elif opcion == "2":
        indice = int(input("Ingrese el índice del elemento a modificar: "))
        if 0 <= indice < len(lista):
            lista[indice] = input("Ingrese el nuevo valor: ")
        else:
            print("Índice fuera de rango.")
    elif opcion == "3":
        indice = int(input("Ingrese el índice del elemento a eliminar: "))
        if 0 <= indice < len(lista):
            del lista[indice]
        else:
            print("Índice fuera de rango.")
    elif opcion == "4":
        if len(lista) > 0:
            lista.pop()
        else:
            print("La lista está vacía.")
    elif opcion == "5":
        elemento = input("Ingrese el elemento a buscar: ")
        encontrado = False
        for i, item in enumerate(lista):
            if item == elemento:
                print(f"Elemento '{elemento}' encontrado en el índice {i}.")
                encontrado = True
                break
        if not encontrado:
            print("Elemento no encontrado en la lista.")
    elif opcion == "6":
        if len(lista) > 0:
            print("Elementos en la lista:")
            for i, elemento in enumerate(lista):
                print(f"{i}: {elemento}")
        else:
            print("La lista está vacía.")
    elif opcion == "7":
        print("Vuelva pronto")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
