lista = {}
def fun_menu() :
    print("--- Lista de compras ---")
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Eliminar productos")
    print("4. Salir")

def fun_add_produc() :
    producto = input("Ingrese el nombre del producto a agregar: ")
    valor = int(input("Ingrese el valor del producto agregado: "))
    lista[producto] = valor

def fun_view_list():
    if len(lista) == 0 :
        print("La lista esta vacia.")
    else:
        print("Lista de mercado:")
        for producto, valor in lista.items():
            print(f"-{producto}: {valor}")
        print("la lista tiene", len(lista),"productos")
            

def fun_erase_produc():
    producto = input("Ingrese el nombre del producto que desea eliminar: ")
    if producto in lista :
        lista.pop(producto)
        print("Producto eliminado correctamente.")
    elif producto not in lista:
        print("El producto ingresado no existe en la lista.")

opc = 0

while opc != 4 :
    fun_menu()
    opc = int(input("Elija una opcion: "))
    if opc == 1 :
        fun_add_produc()
    elif opc == 2 :
        fun_view_list()   
    elif opc == 3 :
        fun_erase_produc()
    elif opc == 4 :
        break
    else :
        print("opcion invalida.")