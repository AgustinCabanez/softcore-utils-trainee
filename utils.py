def menu():
    while True:
        print ("Proyecto calculadora ")
        print("selecione la operacion que desea realizar: ")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")
        opc = int(input("Ingrese la opcion: "))
        if opc == 1:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            resultado = num1 + num2
            print("El resultado de la suma es: ", resultado)
            
        elif opc == 2:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            resultado = num1 - num2
            print("El resultado de la resta es: ", resultado)
            
        elif opc == 3:      
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            resultado = num1 * num2
            print("El resultado de la multiplicacion es: ", resultado)
            
        elif opc == 4:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            if num2 == 0:
                print("No se puede dividir por cero")
            else:
                resultado = num1 / num2
                print("El resultado de la division es: ", resultado)
        elif opc == 5:
            print("Gracias por usar la calculadora")
            break
        else:
            print("Opcion no valida")
if __name__ == "__main__":
    menu()