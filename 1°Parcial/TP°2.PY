# 1
anos = int(input("Ingrese la cantidad de años que tiene el computador"))
if (anos <= 2):
    print("El ordenador es nuevo")
else:
    print("El ordenadoor es viejo")

# 2
anos = int(input("Ingrese la cantidad de años que tiene el computador"))
if (anos < 0):
    print("ERROR")
elif (anos <= 2):
    print("El ordenador es nuevo")
else:
    print("El ordenadoor es viejo")

# 3
nombre1 = input("Ingrese el primer nombre")
nombre2 = input("Ingrese el segundo nombre")
if (nombre1[0:1] == nombre2[0:1]):
    print("Hay coincidencia")
else:
    print("No hay coincidencia")

# 4
voto = input(
    "Ingrese al partido que desea votar:A(partido rojo),B(partido verdad),C(partido azul)").lower()
if (voto == "a"):
    print(f"Usted a votado por el partido rojo")
elif (voto == "b"):
    print("Usted a votado por el partido verdad")
elif (voto == "c"):
    print("Usted a votado por el partido azul")
else:
    print("Opción errónea")

# 5
vocal = input("Ingrese una vocal").lower()
if (len(vocal) > 1):
    print("No se puede procesar el dato")
elif (vocal == "a"):
    print("Es vocal")
elif (vocal == "e"):
    print("Es vocal")
elif (vocal == "i"):
    print("Es vocal")
elif (vocal == "o"):
    print("Es vocal")
elif (vocal == "u"):
    print("Es vocal")
else:
    print("No es vocal")

# 6
ano = int(input("Ingrese el año que desee"))
if (ano % 400 == 0):
    print("El año ingresado es bisiesto")
elif (ano % 100 == 0):
    print("El año ingresado no es bisiesto")
elif (ano % 4 == 0):
    print("El año ingresado es bisiesto")
else:
    print("El año ingresado no es bisiesto")

# 7
menor1 = int(input("Ingrese el primer numero"))
menor2 = int(input("Ingrese el segundo numero"))
menor3 = int(input("Ingrese el tercer numero"))
if (menor1 < menor2 and menor1 < menor3):
    print(f"El número menor es {menor1}")
elif (menor2 < menor1 and menor2 < menor3):
    print(f"EL número menos es {menor2}")
else:
    print(f"El número menor es {menor3}")

# 8
user = "Gwenevere"
password = "excalibur"
userIngre = str(input("Ingrese un usuario"))
passIngre = str(input("Ingrese la contraseña"))
if (userIngre == user and passIngre == password):
    print("Usuario y contraseña correctos.Puede ingresar camelot")
else:
    print("accseso denegado")

# 9
nombre = str(input("Ingrese su nombre"))
sexo = str(input("Ingrese el sexo"))
if (nombre.title()[0] > "N" and sexo.lower() == "hombre"):
    print("Pertenece al grupo A")
elif (nombre.title()[0] < "M" and sexo.lower() == "mujer"):
    print("Pertenece al grupo A")
else:
    print("Pertenece al grupo B")

#10
edad=int(input("Ingrese la edad"))
if(edad<4):
    print("la entrada es gratis")
elif(edad>=4 and edad<=18):
    print("La entrada cuesta $500")
else:
    print("La entrada cuesta $1000") 

#11
print("Escriba si o no")
eleccion=str(input("Desea una pizza vegetariana o no?"))
if(eleccion.lower()=="si"):
    print("Elija un ingrediente")
    ingrediente=str(input("Pimiento/Tofu"))
    if(ingrediente.lower()=="pimiento" or ingrediente.lower()=="tofu"):
        print(f"Pizza vegetariana. Ingredientes:Mozzarella,tomate,{ingrediente}")
    else:
        print("Ingrediente erroneo,Pizza vegetariana. Ingredientes:Mozzarella,tomate ")
elif(eleccion.lower()=="no"):
    print("Elija un ingrediente")
    ingrediente=str(input("Peperoni/Jamon/Salmon"))
    if(ingrediente.lower()=="peperoni" or ingrediente.lower()=="jamon" or ingrediente.lower()=="salmon"):
        print(f"Pizza no vegetariana. Ingredientes:Mozzarella,tomate,{ingrediente}")
    else:
        print("Ingrediente erroneo, Pizza no vegetariana. Ingredientes:Mozzarella,tomate")
else:
    print("Eleccion errone")

#12
anoActual=int(input("Ingrese el año actual"))
anoCualquiera=int(input("Ingrese cualquier año"))
if(anoActual>anoCualquiera):
    print(f"Han pasado {abs(anoActual-anoCualquiera)}")
elif(anoActual<anoCualquiera):
    print(f"Faltan {abs(anoActual-anoCualquiera)} años")
else:
    print("Estamos en ese año")

#13
num1=int(input("Ingrese un numero"))
num2=int(input("Ingrese otro numero"))
if(num1<=0 or num2<=0):
    print("Valores negativos o nulo")
else:
    if(num1>num2):
        if(num1%num2==0):
            print("El numero mayor es multiplo del menor")
        else:
            print("El nuemero mayor no es multiplo del menor")
    else:
        if(num2%num1==0):
            print("El mayor es multiplo del menor")
        else:
            print("El mayor no es multiplo del menor")

#14
a=float(input("Ingrese el valor de A"))
b=float(input("Ingrese el valor de B"))
x=-b/a
print(f"El valor de x en la ecuación {a}x + {b} = 0 es de {x}")

#15
forma=str(input("Ingrese T o t si desea calcular el área de un triángulo ó ingrese C o c si desea calcular el área de un círculo")).lower()
if (forma=="t"):
    base=float(input("Ingrese la base del triángulo"))
    altura=float(input("Ingrese la altura del triángulo"))
    area=(base*altura)/2
    print(f"El área del triágulo es {area}")
elif(forma=="c"):
    radio=float(input("Ingrese el radio del círculo"))
    area1=3.14*(radio**2)
    print(f"El área del círculo es {area1}")
else:
    print("dato incorrecto")

#16
a=float(input("Ingrese el valor de A"))
b=float(input("Ingrese el valor de B"))
decision=input("Ingrese la operación que desea realizar: 1_Suma 2_Multiplicación 3_Resta 4_Divison")
if(decision==1):
    print(f"La suma de los valores {a} y {b} es {a+b}")
elif(decision==2):
        print(f"La multiplicacion de los valores {a} y {b} es {a*b}")
elif(decision==3):
        print(f"La resta de los valores {a} y {b} es {a-b}")
elif(decision==4):
        print(f"La división de los valores {a} y {b} es {a/b}")
else:
    print("El dato que ingreso no corresponde a niguna operación matemática")

#17
dia=str(input("Ingrese el día de la semana que desee")).lower()
if(dia=="lunes"):
    print("LUNES es solo una palabra,tú decides el significado")
elif(dia=="viernes"):
    print("Hoy es vierne y tu cuerpo lo sabe")
elif(dia=="sabado" or dia=="domingo" or dia=="sábado"):
    print("El fin de semana es para salir no para quedarse en casa")
else:
    print("El tiempo que se disfruta es el verdadero tiempo vivido")

#18
horas=int(input("Ingrese la cantidad de horas que trabajo en el mes"))
paga=int(input("Ingrese el salario que recibe por hora trabajada"))
if(horas>48):
    extra=(horas-48)*(paga*1.1)
    salario=extra+(48*paga)
    print(f"El salario total a recibir es de ${salario}")
else:
    print(f"El salario total a recibir es de ${horas*paga}")

#19
cantidad=int(input("Ingrese la cantidad de lápices que desea comprar"))
if(cantidad>=1000):
    descuento=(cantidad*60)*0.07
    print(f"El total a pagar por la cantidad de {cantidad} lápices es de ${(cantidad*60)-descuento}")
else:
    print(f"EL total a pagar por la cantidad de {cantidad} lápices es de ${cantidad*60}")

#20
nota1=int(input("Ingrese la primer nota"))
nota2=int(input("Ingrese la segunda nota"))
nota3=int(input("Ingrese la tercer nota"))
nota4=int(input("Ingrese la cuarta nota"))
promedio=int((nota1+nota2+nota3+nota4)/4)
if (promedio>=6):
    print("Usted ha aprobado el curso")
else:
    print("Usted ha desaprobado el curso")