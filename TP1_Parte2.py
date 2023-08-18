#1
base=float(input("ingrese base"))
altura=float(input("ingrese altura"))
perimetro=(base*2)+(altura*2)
area=base*altura
#2
cateto1=float(input("ingrese cateto 1"))
cateto2=float(input("ingrese cateto 2"))
hipotenusa=(cateto1*2)+(cateto2*2)
#3
num1=float(input("ingrese numero1"))
num2=float(input("ingrese numero2"))
print(f"suma: {num1+num2} , resta: {num1-num2} , multiplicacion: {num1*num2} , division: {num1/num2}")
#4
gradosF=float(input("ingrese grados f"))
c=(gradosF-32)*5/9
#5
#a)	A = input(nombre, “¿Cuál es tu canción favorita?”)
nombre='paulo'
a=input(f"{nombre} ¿cual es tu cancion favorita?")
#b)	precio = input(“Precio: “)
total = precio + (precio * 0.1)
b=float(input('precio: '))
#c)	edad = int(input(“Edad: “))
print(tu edad es, edad)
print=(f'tu edad es: {edad} ')
#d) edad =int(input('Edad:'))
print('veamos si tu edad es 18..',edad=18)
print(f'veamos si tu edad es 18..{edad==18}')
#6
var1= float (input("ingrese un número"))
var2=float (input("ingrese un número"))
var3=float (input("ingrese un número"))
var4=(var1+var2+var3)/3
print(var4)
#7
min=1000
horas=int(min/60)
print(f"Horas: {horas}, minutos: {min%60}")
#8
var1=float(input("Ingrese su primer venta"))
var2=float(input("Ingrese su segunda venta"))
var3=float(input("Ingrese su tercer venta"))
var4=0.1
var5= (var1+var2+var3)*var4
var6= var1+var2+var3+var5
print(f"El total de comisiones que recibirá por las tres ventas es de: {var5}")
print(f"El sueldo mensual total que va recibir es de: {var6}")
#9
var1=float(input("Ingrese el total de su compra"))
var2= 0.15
var3=var1*var2
var4=var1-var3
print(f"El total que debera pagar es de: {var4}")
#10
nota1=float(input("Ingrese su primer nota"))
nota2=float(input("Ingrese su segunda nota"))
nota3=float(input("Ingrese su tercer nota"))
nota4=float(input("Ingrese la nota del trabajo final"))
nota5=float(input("Ingrese la nota del trabajo final"))
nota_parciales=(nota1+nota2+nota3)*0.55
nota_examen_final=nota4*0.3
nota_trabajo_final=nota5*0.15
nota_final_algoritmos=(nota_trabajo_final+nota_parciales+nota_examen_final)/3
print(f"La nota final de Algoritmo es: {nota_final_algoritmos}")
#11
num1=int(input("Ingrese un número"))
num2=int(input("Ingrese un número"))
distancia=abs(num1-num2)
print(distancia)
#12
num1=int(input("Ingrese un número"))
raiz=num1**(1/2)
caudra2=num1**(1/3)
print(f"La raíz cúbica de {num1} es: {caudra2} y la raíz del mismo número es: {raiz}")
#13
num1=str(23)
print(num1[::-1])#usando esetea fórmula se escriben todos los caracteres de adelante hacia atras
#14
var1=int(input("Ingrese el valor de A"))
var2=int(input("Ingrese el valor de B"))
aux=var1
var1=var2
print(f"El valor de A es {var1} y el valor de B es {aux}")
#15
horaSalida=float(input('indique hora de salida'))
minutosSalida=float(input('indique minuto de salida'))
segundosSalida=float(input('indique segundos de salida'))
tsegundos=float(input('indique los segundos totales que se demoro para llegar'))
horaLlegada=tsegundos//3600
minutosLlegada=(tsegundos%3600)//60
segundosLlegada=tsegundos%60
print(f'el ciclista llego a las {horaLlegada+horaSalida} hs, {minutosLlegada+minutosSalida} min y {segundosLlegada+segundosSalida} seg')
#16
nombre=input("Ingrese su nombre")
apellido= input("Ingrese su apellido")
print(f"La inincial de su nombre es {nombre[0:1]} y la de su apellido es {apellido[0:1]}")
#17
usuario=input("Ingrese su nombre")
print(f"Ahora estas en la matrix, [{usuario}]")
#18
total=float(input("Ingrese el gasto toal de la cena"))
total_a_pagar=total+(total*0.062)+(total*0.1)
print(f"El monto final a pagar es {total_a_pagar}")
#19
dia=input("Ingrese el día de su nacimiento")
mes=input("Ingrese el mes de su nacimiento")
año=input("Ingrese el año de su nacimiento")
print(f"Su fecha de nacimiento es {dia}/{mes}/{año}")
#20
dia=str(input("Ingrese el día de su nacimiento"))
mes=str(input("Ingrese el mes de su nacimiento"))
año=str(input("Ingrese el año de su nacimiento"))
fecha=(dia+mes+año).upper()
print(fecha)
#21
consumo=float(input("Ingrese la cantidada de kilómetros x 1L gasta la moto"))
tanque=float(input("Ingrese la capacidad de litros que ingresan en el tanque de combustible"))
kilometros=float(input("Ingrese la cantidad de kilómetros que desea recorrrer"))
cantidad_de_consumo=(tanque*consumo)
cantidad_de_consumo=int(kilometros/cantidad_de_consumo)+1
print(f"Para recorrer {kilometros} kilomtros va a nececsitar {cantidad_de_consumo} tanque/s de combustible")

