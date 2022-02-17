# Esto es un comentario de linea

'''
Comentario de bloque
'''

# Salida por consola

print("Que chimba sog")

# Variables o entradas

nombre = 'Juan'
edad = 34
estatura = 1.65
hinchaDeVerde = True

print(nombre, edad, estatura, hinchaDeVerde, "Sihabueno")

print(f'Buenos dias {nombre}, tu edad es {edad}, mides aproximadamente {estatura} y eres hincha del Nacional {hinchaDeVerde}')

# Recibiendo variables desde la consola

numero1 = int(input('Digita un numero entero:'))
numero2 = int(input('Digita otro numeor entero:'))

resultado = numero1 + numero2

print(f'El resultado es {resultado}')

# Decision logica

if(numero1 > numero2):
    print(f'El primer numero ({numero1}) es mayor que el segundo ({numero2})')
else:
    print(f'El segundo numero ({numero2}) es mayor que el primer ({numero1})')

