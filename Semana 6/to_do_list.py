to_do_list = []
opc = 0

def upload_list() :
    try :
        with open("to_do_list.txt", "r") as archivo:
            for linea in archivo :
                linea = linea.strip()
                if linea != "" :
                    partes = linea.split(";")
                    task = {
                        "Name" : partes[0],
                        "State" : partes[1],
                    }      
                    to_do_list.append(task)
    except FileNotFoundError: 
        pass

def view_menu():
    print("--- Menu ---")
    print("1. Add a task.")
    print("2. view to do list.")
    print("3. Delete a task.")
    print("4. change state a task.")
    print("5. Leave.")

def adittion_task():
    name = input("Enter the task name: ")
    state = input("Enter the task status: ")
    task = {
        "Name" : name,
        "State" : state, 
    }
    to_do_list.append(task)
    save_to_do_list()

def view_to_do_list() :
    if len(to_do_list) == 0:
        print("The to do list is empty.")
    else :
        print("To do List:" )
        for task in to_do_list :
            print("Name: ", task["Name"])
            print("State: ", task["State"])
        print("The to do list have",len(to_do_list),"taks.")

def delete_task() :
    name = input("Enter a task name what need delete: ")
    found = False
    for task in to_do_list :
        if task["Name"] == name :
            found = True
            if found == True :
                to_do_list.remove(task)
            print("Task delete sucessful.")
            save_to_do_list()
    if found == False :
        print("Dont exist that Task.")

def change_state() :
    name = input("Enter a task name what need chage state: ")
    found = False
    for task in to_do_list :
        if task["Name"] == name :
            found = True
            if found == True :
                task["State"] = input("Enter a new state: ")
                print("The change sucessful.")
                save_to_do_list()
    if found == False :
        print("Dont exit that Task.")

def save_to_do_list() :
    with open ("to_do_list.txt", "w") as archivo :
        for task in to_do_list :
            linea = task["Name"] + ";" + task["State"] + "\n"
            archivo.write(linea) 

upload_list()

while opc != 5:
    view_menu()
    opc = int(input("Enter a option number: "))
    if opc == 1 :
        adittion_task()
    elif opc == 2 :
        view_to_do_list()
    elif opc == 3 :
        delete_task()
    elif opc == 4 :
        change_state()
    elif opc == 5 :
        break
    else :
        print("Invalid Option.")