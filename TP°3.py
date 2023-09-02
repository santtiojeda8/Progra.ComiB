#1
word=input("Ingrese una palabra")
for i in range(10):
    print(word)

#2
age=int(input("Ingrese su edad"))
for i in range(age) :
    print(i+1)

#3

num=int(input("Ingrese un número"))
for i in range(1,num+1):
    if (i%2 != 0):
        print(f"{i},",end="")

#4
num=int(input("Ingrese el númwro que desee"))
i=num
while (i>=0):
    print(i,end="")
    i-=1
    if (i >= 0 ):
        print(",",end="")

#5
cashtoinvest=int(input("Ingrese la cantidad a invertir"))
annualinterest=float(input("Ingrese el interés anual"))
years=int(input("Ingrese la canatidad de años a invertir"))
annualinterest=annualinterest/100
for i in range(years):
    cashtoinvest+=(cashtoinvest*annualinterest)
    print(f"capital obtenido {cashtoinvest}")

#6
num=int(input("Ingrese un numero"))
for i in range(1,num+1):
    print("")
    for j in range(1,i+1):
        print("*",end="")

#7
for i in range(1,10):
    print(f"Tabla del {i}")
    for j in range(1,10):
        print(i*j)

#8
num=int(input("Ingrese un número entero"))

#9
password=input("Ingrese su nueva contraseña")
validation_password=""
while (validation_password != password):
    validation_password=input("Ingrese nuevamente su contraseña")
print("Contraseña nueva lamacenada correctamente")

#10
number=int(input("Ingrese nu número entero para saber si es primo o no"))
account=0
sss=0
for i in range(number+1):
    if (number%(i+1) == sss):
        account+=1

if ((account==2)):
    print("El número ingresado es primo")
else:
    print("El número ingresado no es primo")

#11
word= input("Inrgese una palabra")
word= word[::-1]
for i in word:
    print(i,end=" ")

#12
word=input("Ingrese una frase o palabra")
letter=input("Ingrese la letra que deseea buscar dentro de la frase anterior")
account=0
for i in word:
    if (letter == i):
        account+=1

print(f"La letra {letter} aparece en la frase {account} veces")

#13
word=input("Ingrese una palabra")
print("Para salir del programa debe ingresar salir")
while(word.lower() != "salir") :
    print(word)
    word=input("Ingrese una palabra")
print("Salió del programa")

#14

