print("Hola, mundo")

numero1 = 6
numero2 = 11

sumar = numero1 + numero2

print(sumar)

def sumar(numeroA, numeroB):
    return numeroA + numeroB

resultado = sumar(numero1, numero2)
print(f'El resultado es: {resultado}')

#Comentario

x = 12 # Integer 
print(x)

y = 13.5 #float ---> flotando
print(y)

#Veamos el tipo de dato de las variables x e y

print(type(x))
print(type(y))

booleano = True

if(booleano):
    print("La concha de tu madre")
print(booleano)
print(type(booleano))