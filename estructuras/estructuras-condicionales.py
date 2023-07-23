'''edad = int(input("Ingese su edad: "))

if(edad < 18):
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")

numero1 = int(input("Ingresa un número mayor a 0 para realizar una división del mismo: "))

if(numero1 <= 0):
    print("El numero ingresa no es valido para dividir, vuelva a ingresarlo")
    numero1 = int(input("Ingresa un número mayor a 0 para realizar una división del mismo: "))

numero2 = int(input("Ingresa el número que quieres dividir el anterior:"))

if(numero2 <= 0):
    print("El numero ingresa no es valido para dividir, vuelva a ingresarlo: ")
    numero2 = int(input("Ingresa un número mayor a 0 para realizar una división del mismo"))




def division(numero1, numero2):
    return numero1 / numero2

resultado = division(numero1, numero2)

print(float(resultado))

'''
#problemas 3 
#pida usuario ent y muestre si es par o impar

numero1user = int(input("Ingresa un número: "))


if(numero1user % 2 == 0) :
    print("El número es par")
else: 
    print("El número es impar")


#Solicitar al usuario que ingrese dos números y mostraer cuál de los dos es menor, considerar si son iguales

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número"))

if(numero1 > numero2):
    print(f'El numero {numero1} es mayor que {numero2}')
elif(numero1 < numero2):
    print(f"EL número {numero2} es mayor que el {numero1}")
else:
    print("Los números ingresados son iguales")


