lista = {}
opc = 0
while opc != 4 :
    print("--- Lista de compras ---")
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Eliminar productos")
    print("4. Salir")
    opc = int(input("Elige una opcion: "))
    if opc == 1 :
         producto = input("Ingrese el nombre del producto a agregar: ")
         valor = int(input("Ingrese el valor del producto agregado: "))
         lista[producto] = valor
    elif opc == 2:
        if len(lista) == 0 :
            print("La lista esta vacia.")
        else:
            print("Lista de mercado:")
            for producto, valor in lista.items():
                print(f"-{producto}: {valor}")
            print("la lista tiene", len(lista),"productos")
    elif opc == 3:
        producto = input("Ingrese el nombre del producto que desea eliminar: ")
        if producto in lista :
            lista.pop(producto)
            print("Producto eliminado correctamente.")
        elif producto not in lista:
            print("El producto ingresado no existe en la lista.")
    else:
        print("opcion no valido.")