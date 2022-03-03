contador = 1
sumatoria = 0

while(contador <= 5):
    num = int(input("Porfvaor digite un numero: "))
    if(num < 0):
        sumatoria+=1
    contador+=1
    
print(f'La cantidad de negativos es: {sumatoria}')
    