book_contact = []
opc = 0
def cargar_contactos():
    try:
        with open("contactos.txt", "r") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea != "":
                    partes = linea.split(";")
                    contacto = {
                        "name": partes[0],
                        "email": partes[1],
                        "number": partes[2]
                    }
                    book_contact.append(contacto)
    except FileNotFoundError:
        # Si el archivo no existe, no hacemos nada (la lista queda vacía)
        pass

def view_menu():
    print("--- Menu ---")
    print("1. Agregar un contacto.")
    print("2. Ver contactos.")
    print("3. Eliminar un contacto.")
    print("4. Buscar un contacto.")
    print("5. Salir.")

def addition_contact():
    name = input("Ingrese el nombre del contacto que desea ingresar: ")
    email = input("Ingrese el email del contacto: ")
    number = input("Ingrese el numero del contacto: ")
    contact = {
        "name": name,
        "email": email,
        "number": number
    }
    book_contact.append(contact)
    guardar_contactos()
    return contact

def view_contact():
    if len(book_contact) == 0 :
            print("La lista esta vacia.")
    else:
        print("Lista de contactos:")
        for contact in book_contact:
            print("Nombre:", contact["name"])
            print("Email:", contact["email"])
            print("Numero:", contact["number"])
        print("la lista tiene", len(book_contact),"contactos")

def delete_contact():
    name = input("Ingrese el nombre del contacto que desea eliminar: ")
    encontrado = False
    for contact in book_contact :
        if contact["name"] == name :
            encontrado = True
            if encontrado == True :
                book_contact.remove(contact)
                print("Contacto eliminado exitosamente.")
    guardar_contactos()
    if encontrado == False :
        print("No exite un contacto con ese nombre o no esta en la lista de contactos.")

def guardar_contactos():
    with open("contactos.txt", "w") as archivo:
        for contacto in book_contact:
            linea = contacto["name"] + ";" + contacto["email"] + ";" + contacto["number"] + "\n"
            archivo.write(linea)

def search_contact():
    name = input("Ingrese el nombre del contacto a buscar: ")
    encontrado = False
    for contact in book_contact :
        if contact["name"] == name :
            encontrado = True
            if encontrado == True :
                print("Nombre:", contact["name"])
                print("Email:", contact["email"])
                print("Numero:", contact["number"])
    if encontrado == False :
        print("No existe el contacto.")

cargar_contactos()

while opc != 5 :
    view_menu()
    opc = int(input("Ingrese el numero de la opcion elegida: "))
    if opc == 1 :
        addition_contact()
    elif opc == 2 :
        view_contact()
    elif opc == 3 :
        delete_contact()
    elif opc == 4 :
        search_contact()
    elif opc == 5 :
        break
    else :
        print("Opcion invalida.")