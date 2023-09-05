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
number = int(input("ingrese un numero: "))
for i in range(1, number + 1, 2):
    for j in range(i, 0, -2):
        print(j, end="")
    print("")

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
number1=int(input("Ingrese el primer números par"))
number2=int(input("Ingrese el sesgundonúmeros par"))
if (number1%2 == 0):
    print(f"El número {number1} es par")
if (number2%2 == 0):
    print(f"El número {number2} es par")

#15
number=int(input("Ingrese un número mayor a 0"))
print(f"El número {number} es divisible por: ",end="")
for i in range(number+1):
    if (number%(i+1) == 0):
        print(i+1,end=" ")

#16
number=int(input('ingrese cantidad de numeros a ingresar: '))
list_of_number=[]
contNeg=0
for i in range(1,number+1):
    num=int(input(f'ingrese numero {i}:'  ))
    list_of_number.append(num)
print(list_of_number)    
for n in list_of_number:
    if n<0:
        contNeg+=1    
print(f'en total hay {contNeg} numeros negativos')

#17
vowels=set() #set no permite elementos repetidos
sentence=input('ingrese frase: ')
for v in sentence:
    if v=='a' or v=='e' or v=='i' or v=='o' or v=='u':
        vowels.add(v)
print(f'las vocales en la oracion son {vowels}')        

#18
quantity=int(input("Ingrese la cantidad de veces a repetir la secuencia fibonacci"))
fibonacci=[]
a=0
b=1
for i in range(quantity):
    fibonacci.append(a)
    a,b=b,a+b
print(fibonacci)

#19
money_box=int(input("Ingrese la cantidad de dinero que desea ahorrar en la alcancía"))
total_money=0
actually_money=0
while money_box>total_money:
    actually_money=int(input("Cuanto dinero desea ingresar a la alcancía?"))
    if (actually_money<0):
        print("La cantidad de dinero ingresada es incorrecta, vuelva a ingresar")
    else:
        total_money+=actually_money
    print(f"LLeva ahorrado {total_money}")
print(f"El dinero total ahorrado es de ${total_money}")

#20
number=int(input("Ingrese un número entero"))
account=0
print("Escriba 0 cuando desee salir del programa")
while number!=0:
    account+=number
    number=int(input("Ingrese un número entero"))
print(f"La suma de todos los número ingresados es {account}")

#21
number=int(input("Ingrese un número entero"))
bigger=0
print("Escriba 0 cuando desee salir del programa")
while number!=0:
    if number>bigger:
        bigger=number
    number=int(input("Ingrese un número entero"))
print(f"El número entero mas grande  es {bigger}")

#22
number=int(input("Ingrese un número entero"))
account=0
even_numbers=0
print("Para salir del programa debe ingresar -1")
while number!= -1:
    account+=number
    if number%2 == 0:
        even_numbers+=1
    number=int(input("Ingrese un número entero"))
print(f"La suma de todods los números ingresados es {account} y dentro de los números ingresados hay {even_numbers} números pares")

#23
ammount=int(input("Ingrese el monto de la compra"))
total_ammount=0
print("Escriba 0 cuando desee salir del programa")
while ammount!=0:
    total_ammount+=ammount
    ammount=int(input("Ingrese el monto de la compra"))
print(f"El monto total de la compra es {total_ammount}")

#24
ammount=int(input("Ingrese el monto de la compra"))
total_ammount=0
print("Escriba 0 cuando desee salir del programa")
while ammount!=0:
    if ammount<0:
        print("El monto ingresado es negativo")
    else:
        total_ammount+=ammount
    ammount=int(input("Ingrese el monto de la compra"))
if total_ammount>1000:
    total_ammount=total_ammount*0.9
print(f"El monto total a pagar es de ${total_ammount}")

#25
number=int(input("Ingrese un número para saber su factorial"))
account=1
for i in range(1,number+1):
    account=account*i
print(f"El númeroi factorial de {number} es {account}")