#1
word=input("Ingrese una palabra")
if len(word) == 4:
    word+="!"
else:
    word+="?"
print(word)
#2
import random
words_list=["salmon","pescado","carne","adios","ascendente","hola"]
indice=random.randint(0,len(words_list)-1)
word=words_list[indice]
intentos=0
letter_list=[]
aux=word
print(word)
while intentos<6:
    letter=input("Ingrese una letra")
    if letter in word:
        print("la letra se encuentra en la palabra")
        letter_list+=letter
        for i in word:
            for j in letter_list:
                if i == j:
                    word=word.replace(i,"")
        if len(word)==0:
            print("Adivinaste la palabra")
            break
    else:
        print("la letra no se encuentra en la palabra")
        intentos+=1
if intentos==6:
    print("Te quedaste sin intentos")
print(f"La palabra es {aux}")

#3
word=input("Ingrese una frase")
words=word.split()
print(f"Hay {len(words)} palabras")
for i in words:
    print(i, end="-")

#4
salary=int(input("Ingrese el sueldo base por mes: "))
hours=int(input("Cuantas horas trabajó el domingo? "))
porcent=0
while True:
    assistence=input("Asistió todo el mes? SI/NO ")
    if assistence.lower()=="si":
        if hours>=3 and hours<=5:
            porcent=salary*0.03
            print(f"El salario del empleado es de: ${salary+porcent}")
            break
        elif hours>=6 and hours<=10:
            procent=salary*0.10
            print(f"El salario del empleado es de: ${salary+porcent}")
            break
        else:
            print(f"El salario del empleado es de: ${salary+porcent}")
            break
    elif assistence.lower()=="no":
        if hours>=3 and hours<=10:
            porcent=salary*0.02
            print(f"El salario del empleado es de: ${salary+porcent}")
            break
        else:
            print(f"El salario del empleado es de: ${salary+porcent}")
            break
    else:
        print("Opcion no valida")
#5
number1=int(input("Ingrese el primer numero"))
number2=int(input("Ingrese el segundo numero"))
if number1 == number2:
    print(f"Multiplicacion= {number1*number2}")
elif number1>number2:
    print(f"Resta= {number1-number2}")
else:
    print(f"Suma= {number1+number2}")
#6
while True:
    name=input("Ingrese el nombre. (Si desea terminar el programa ingrese enter vacio)")
    if name =="" or name ==" ":
        print("Gracias por confiar en nosotros")
        break
    age=int(input("Ingrese la edad"))
    antiquity=int(input("Ingrese la antigüedad"))
    if age>=60 and antiquity<25:
        print(f"{name} pertenece a una jubilación por edad")
    elif age<60 and antiquity>=25:
        print(f"{name} pertenece a una jubilación por antigüedad joven")
    elif age>60 and antiquity>=25:
        print(f"{name} pertenece a una jubilación por antigüedad joven")

#7
print(" PROGRAME DE UTILIDAD (ingrese enter si desea terminar)")
while True:
    name=input("Ingrese el nombre del empleado ")
    if name=="" or name==" ":
        print("Muhcas gracias por elegirnos")
        break
    age=int(input("Ingrese la antigüedad del empleado (en años) "))
    salary=int(input("Ingrese el salario mensual que recibe "))
    if age <1:
        utility=salary*0.05
        print(f"La utilidad a recibir es de {utility}")
    elif age >=1 and age <2:
        utility=salary*0.07
        print(f"La utilidad a recibir es de {utility}")
    elif age >=2 and age<5:
        utility=salary*0.1
        print(f"La utilidad a recibir es de {utility}")
    elif age >=5 and age <10:
        utility=salary*0.15
        print(f"La utilidad a recibir es de {utility}")
    elif age >=5:
        utility=salary*0.2
        print(f"La utilidad a recibir es de {utility}")
    else:
        print("Dato no valido")