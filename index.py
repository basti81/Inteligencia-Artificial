suma = 0
cont = 0
nMax = 0
nMin = 0

while(1):
    x = int(input("ingresa numero: "))
    if(x==""):
        break
    if (cont == 0):
        nMax = x
        nMin = x
    if(x < nMin):
        nMin = x
    elif(x > nMax):
        nMax = x 
    suma = suma + x
    cont =cont+1
    print("Media", suma/cont)
    print("Numero Max ", nMax)
    print("Numero Min ", nMin)

    
