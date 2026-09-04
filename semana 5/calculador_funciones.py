print("Bienvenido a su calculadora")
resultado = 0
continuar = 0


def fun_enter():
    num1 = int(input("Ingrese el valor del primer numero de la operacion: "))
    num2 = int(input("Ingrese el valor del segundo numero de la operacion: "))
    operacion = input("Ingrese la operacion(+,-,*,/): ")
    return num1, num2, operacion



def fun_addition(num1, num2):
    resultado = num1 + num2
    print("El resultado de la suma es:", resultado)
    

def fun_subtraction(num1, num2):
    resultado = num1 - num2
    print("El resultado de la resta es: ", resultado)
    

def fun_multiplication(num1, num2):
    resultado = num1 * num2
    print("El resultado de la multiplicacion es: ", resultado)
    

def fun_division(num1, num2):
    resultado = num1 / num2
    print("El resultado de la division es: ", resultado)
    

while continuar != "No" and continuar != "no" and continuar != "n":
    num1, num2, operacion = fun_enter()
    if operacion != "+" and operacion != "-"  and operacion != "/" and operacion != "*" :
     print("Operacion Incorrecta")
    elif operacion == "+" :
     fun_addition(num1, num2)
    elif operacion == "-" :
     fun_subtraction(num1, num2)
    elif operacion == "*" :
     fun_multiplication(num1, num2)
    elif operacion == "/" and num2 != 0 :
     fun_division(num1, num2)
    else :
       print("No se puede dividir por cero.")
    continuar = str(input("Desea continuar con usando la calculadora?: "))
