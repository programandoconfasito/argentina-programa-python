
numeroUsuario = float(input("Dame un número flotante: "))
numero2Usuario = int(input("Dame un número entero: "))
operacion = input("Declara el tipo de operación con +, -, /, * : ")

def calculadora(numeroA, numeroB, operacion):
    if(operacion == "+"):
        return numeroA + numeroB
    elif(operacion == "-"):
        return numeroA - numeroB
    elif(operacion == "/"):
        return numeroA / numeroB
    elif(operacion == "*"):
        return numeroA * numeroB
    
resultado = calculadora(numeroUsuario, numero2Usuario, operacion)

print(resultado)

#exponenciación

print(2**3) #2*2*2