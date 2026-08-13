print("Bienvenido a su calculadora")
num1 =int(input("Ingrese el primer numero de la operacion:"))
num2 = int(input("Ingrese el segundo numero de la operacion:"))
operacion = input("Ingrese la operacion(+,-,*,/):")
resultado = 0
if operacion != "+" and operacion != "-"  and operacion != "/" and operacion != "*" :
     print("Operacion Incorrecta")
elif operacion == "+" :
    resultado = num1 + num2
    print("El resultado de el calculo es:", resultado)
elif operacion == "-":
    resultado = num1 - num2
    print("El resultado de el calculo es:", resultado)
elif operacion == "*":
    resultado = num1 * num2
    print("El resultado de el calculo es:", resultado)
elif operacion == "/" and num2 != 0 :
    resultado = num1 / num2 
    print("El resultado de el calculo es:", resultado)
else :
    print("No se puede dividir por cero")