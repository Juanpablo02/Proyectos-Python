from cmath import sqrt
import math

# Menu de opciones

opcion=1

print("Bienvenido a Empanas el Mocho")
print("*********************")
print("0. Salir")
print("1. Encontrar multiplo de 2")
print("2. Encontrar raiz cuadrada")
print("3. Sumar +100")
print("4. Elevar a la 2")

while(opcion != 0):
    opcion = int(input("Digita una opcion: "))
    if(opcion == 1):
        num = int(input("Digite un Numero entero: "))
        if(num % 2 == 0):
            print("El numero digitado es multiplo de 2")
        else:
            print("El numero digitado no es multiplo de 2")
    elif(opcion == 2):
        num = int(input("Digite un numero para saber su raiz cuadrada: "))
        print(math.sqrt(num))
    elif(opcion == 3):
        num = int(input("Digite un numero para sumar 100: "))
        print(num + 100)
    elif(opcion == 4):
        num = int(input("Digite un numero para elevar a la 2: "))
        print(pow(num,2))
    elif(opcion == 0):
        break
    else:
        print("Digite una opcion valida")
else:
    print("Para ahi")