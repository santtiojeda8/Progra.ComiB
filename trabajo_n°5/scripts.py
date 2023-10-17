#1
import funciones
dni_number=int(input("Ingrese su N° de DNI"))
print(funciones.digits(dni_number))

#2
import funciones
phrase=input("Ingrese una frase de mas de 2 palabras")
print(funciones.last_word(phrase))

#3 
import funciones
while True:
    name=input("Ingrese su nombre completo (formato: nombre apelido ó, formato: nombre1,nombre2,apellido) ")
    complete_name=name.split(",")
    if name=="":
        break
    elif len(complete_name)==1:
        while True:
            dni_number=int(input("Ingrese su número de DNI"))
            if funciones.digits(dni_number)==True:
                break
            else:
                print("DNI no válido")
        last_name=name.split()
        last_name=last_name[1]
        partner_id=last_name.title()
        partner_id+=funciones.cant_digits(last_name)
        partner_id+=funciones.first_digits(dni_number)
        print(f"Su ID de socio es {partner_id}")
    elif len(complete_name)==3:
        while True:
            dni_number=int(input("Ingrese su número de DNI"))
            if funciones.digits(dni_number)==True:
                break
            else:
                print("DNI no válido")
        complete_name=complete_name[2]
        partner_id=complete_name.title()
        partner_id+=funciones.cant_digits(complete_name)
        partner_id+=funciones.first_digits(dni_number)
        print(f"Su ID de socio es {partner_id}")

#4
import funciones
num1=int(input("Ingrese un número"))
num2=int(input("Ingrese un número"))
if num1%num2==0 or num2%num1==0:
    print("Uno de los números ingresados es múltiplo del otro")
if funciones.multi(num1,num2)==True:
    print("El primer n° es múltiplo del segundo")
elif funciones.multi(num1,num2)==False:
    print("El primer n° no es múltiplo del segundo")

#5
import funciones
days=int(input("Ingrese la cantidad de días"))
if days==1:
    max_temp=int(input("Ingrese la temperatura máxima"))
    min_temp=int(input("Ingrese la temperatura mínima"))
    print(f"La temperatura media es ",(funciones.temperature(max_temp,min_temp)))
elif days>1:
    for i in range(days):
        max_temp=int(input("Ingrese la temperatura máxima"))
        min_temp=int(input("Ingrese la temperatura mínima"))
        print(f"La temperatura media es ",(funciones.temperature(max_temp,min_temp)))

#6
import funciones
phrase=input("Ingrese una frase o una palabra")
print(funciones.space(phrase))

#7
import funciones
number_ls=[]
end=int(input("Ingrese la cantidad de números que desea ingresar"))
for i in range(end):
    number=int(input("Ingrese number"))
    number_ls.append(number)
print(number_ls)
print(funciones.max_and_min(number_ls))

#8
import funciones
import math 
num=math.pi
radio=int(input("Ingrese el radio de una circunferencia "))
print("El area de la circunferencia es ",(funciones.area(num,radio)))

#9 
import funciones
attempt=0
while True:
    user=input("Ingrese el nombre de ususario")
    password=input("Ingrese la contraseña")
    print(funciones.login(user,password,attempt))
    attempt=funciones.login(user,password,attempt)
    if funciones.login(user,password,attempt)=="Verdadero":
        break
    elif attempt==3:
        break

#10
import funciones
print("Los descuentos a las compras dependen del monto de la prenda")
garment={}
discount={"1":0.10, "2":0.15, "3":0.2}
j=0
while True:
    j+=1
    garment[j]=int(input("Ingrese el valore de la prenda (ingrese 0 cuando desee terminar)"))
    if garment[j]==0:
        break
print("Cada producto con descuentos aplicados le queda en ",funciones.total(garment,discount))

#11
import funciones
list_of_number=[]
while True:
    num=int(input("Ingrese un número entero (Ingrese 0 para salir)"))
    if num==0:
        break
    list_of_number.append(num)
print(list_of_number)
print("El doble de los números ingresado es ",funciones.first(list_of_number))  

#12
import funciones
phrase=input("Ingrese una frase de mas de dos palabras")
phrase=phrase.split()
print(funciones.diccio(phrase))

#13
import funciones
num1=float(input("Ingrese el primer numero del vector"))
num2=float(input("Ingrese el segundo numero"))
print("El módulo del vector es  ",funciones.mod(num1,num2))

#14
import funciones
num=int(input("Ingrese un número entero para saber si es primo o no "))
print("Si el número es primo nos devolvera True, y si no lo es nos devolvera False")
print(funciones.primo(num))

#15
import funciones
num1=0
while True:
    num=int(input("Ingrese un número entero"))
    if num ==0:
        break
    print(f"El factorial de {num} es ",funciones.factorial(num))
    num1+=1
print("La cantidad de numeros ingresados es ",funciones.counter(num1))

#16
import funciones
num=int(input("Ingrese un número entero"))
num1=input("Ingrese un solo dígito para saber cuantas veces aparece en el número")
print("La cantidad de ocurrencias enciontradas es ",funciones.frequency(num,num1))

#17
import funciones
max=0
while True:
    num=int(input("Ingrese números primos"))
    if funciones.primo(num)==False:
        break
    print("EL numero ingresado contiene ",funciones.sum_digits(num)," digitos")
    num1=int(input(f"Ingrese un número para saber cuantas veces aparece en {num}"))
    print(num1," aparece ",funciones.frequency(num,num1)," veces")
    if num>max:
        max=num
print("El factorial del numero max ingresado es ",funciones.factorial_1(max))