arregloM=[]
numCorrer=int(input('cuantos lugares quieres correr: '))
for i in range(1,6):
    mensaje=input(f'ingrese el mensaje al ofical{i}: ')
    arregloM.append(mensaje)

print(arregloM)
abecedario='abcdefghijklmnopqrstuvwxyz'
arregloPalabras=[]
for p in arregloM:
    msj_enc = ''
    for letra in p:
        if letra in abecedario:
            ind=abecedario.find(letra)
            ind = (ind+numCorrer)%26
            msj_enc += abecedario[ind]
        else:
            msj_enc+=letra
    arregloPalabras.append(msj_enc)
print(arregloPalabras)

#punto2

"""Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el
0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene.
Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total."""
contPares = 0
contimPares = 0
contParesNum = 0
contimParesNum = 0
while True:
    print("")
    num = int(input("ingrese un num, ingrese 0 para terminar: "))
    if num == 0:
        break
    longitud = str(num)
    for p in longitud:
        for j in p:
            if int(j) > 0:
                if int(j) % 2 == 0:
                    contPares += 1
                    contParesNum += 1
                else:
                    contimPares += 1
                    contimParesNum += 1
            print(j, end=" ")
    print(f'el numero tiene {contParesNum} numeros pares y {contimParesNum} numeros impares')
    contimParesNum=0
    contParesNum=0    
print("terminado")
print(f"en total hay {contPares} numeros pares y {contimPares} impares")