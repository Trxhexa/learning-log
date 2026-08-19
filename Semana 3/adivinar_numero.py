import random
num_random = random.randint(0,100) 
print("Bienvenido al juego de adivina el numero, el numero a adivinar esta en el rango de 0 - 100 contando a ambos.")
num_resp = 0
cont_int = 0
while num_resp != num_random :
    num_resp = int(input("Ingrese su intento: "))
    cont_int = cont_int + 1 
    if num_resp > num_random :
        print("El numero ingresado es mayor que el numero a adivinar.")
    elif num_resp < num_random :
        print("El numero ingresado es menor que el numero a adivinar.")
print("Lo lograste en", cont_int,"intentos.")