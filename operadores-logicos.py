#Variables booleanas

print(4<5) # True
print(5<4) # False

# Realizar comparaciones de datos

print( 6 == 6) # True
if((3<4) and (4<5)):
    print("La condición es verdadera")
if((3<4) & (4<5) ):
    print("también funciona así")


x = True
y = False

print(type(x)) #bool

print(x and x) # True

print(x and y) # False

print(x or y) # True

print(y | y) # False

print((3<4) and (6<5)) # False

#Negación

resultado = x and x #True and True

print(resultado)
print(not resultado)