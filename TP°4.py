#1
x=0
while x <=30:
    x+=1
    if (x==4 or x==6 or x==10):
        print(f"El valor de {x} se saltó")
    else:
        if x==15:
            break
        else:
            print(x)
print(f"Se rempió la ejecución cuando x valía: {x}")

#2
while True:
    word=input("Ingrese una palabra").upper()
    print(word)
    if word =='':
        break  

#3
total=0
while True:
    word=input("")
    if word=="":
        break
    operation, account=word.split()
    account=int(account)
    if operation.lower()=="d":
        total+=account
    elif operation.lower()=="r":
        total -= account
print(f"EL total es {total}")

#4
cousin_number=0
while True:
    account=0
    number=int(input("Ingrese un número"))
    if number == 0:
        break
    elif(number<0):
        print("El número ingresado no es primo")
    else:
        for i in range(number+1):
            if (number%(i+1) == 0):
                account+=1
        if (account==2):
            cousin_number+=1
print(f"La cantidad de números primos ingresados es de {cousin_number}")

#5
first_year=int(input("Ingrese el primer año"))
seccond_year=int(input("Ingrese el segundo año"))
for i in range(first_year,seccond_year+1):
    if (i%4==0 and i%100!=0) or i%400==0:
        print(i)

#6
for i in range(1,21):
    if (i%2!=0):
        continue
    print(i)

#7
list=[]
for i in range(101):
    list.append(i)
number=int(input("Ingrese el n°  que desee buscar"))
for j in list:
    if list[j]==number:
        print(f"Se encontro el n° {number} en la posición {j}")
        break

#8
while True:
    print("Ingrese una de las opciones del menú: 1 2 3")
    number=int(input("Ingrese la opción que desee"))
    if (number==1):
        print("Sorpresa 1")
    elif(number==2):
        print("Sorpresa 2")
    elif(number==3):
        print("Sorpresa 3")
    elif(number==0):
        break
    else:
        print("Hace las cosas bien")
