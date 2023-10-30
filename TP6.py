#1
list_numbers=[]
while True:
    num1=int(input("Ingrese un número"))
    if num1==0:
        break
    else:
        list_numbers.append(num1)
print(list_numbers)

#2
list_numbers=[]
while True:
    num1=int(input("Ingrese un número"))
    if num1==0:
        break
    else:
        list_numbers.append(num1)
print(list_numbers)
num2=int(input("Ingrese el número que desee eliminar de la lista"))
list_numbers.remove(num2)
print(list_numbers)

#3
list_numbers=[]
while True:
    num1=int(input("Ingrese un número"))
    if num1==0:
        break
    else:
        list_numbers.append(num1)
print(list_numbers)
num2=int(input("Ingrese el número que desee eliminar de la lista"))
list_numbers.remove(num2)
print(list_numbers)
counter=0
for i in list_numbers:
    counter+=i
print(f"La sumatoria de todos los números ingresdados es {counter}")

#4
list_numbers=[]
while True:
    num1=int(input("Ingrese un número"))
    if num1==0:
        break
    else:
        list_numbers.append(num1)
print(list_numbers)
num2=int(input("Ingrese el número que desee eliminar de la lista"))
list_numbers.remove(num2)
print(list_numbers)
counter=0
for i in list_numbers:
    counter+=i
print(f"La sumatoria de todos los números ingresdados es {counter}")
num2=int(input("Ingrese un número para formar una nueva lista"))
new_list=[]
for i in list_numbers:
    if i<num2:
        new_list.append(i)
new_list.append(num2)
for i in new_list:
    print(i,end=" ")

#5
list_numbers=[]
while True:
    num1=int(input("Ingrese un número"))
    if num1==0:
        break
    else:
        list_numbers.append(num1)
print(list_numbers)
#Creamos una lista y una tupla nueva, un contador para cada n°.
listanueva=[]
tupla=()
for i in list_numbers:
    cont=0  #Volvemos a resetear el contador en 0 para volver a contar cada iteración antes de entrar en e segundo bucle
    for k in list_numbers:   #Iteramos cada elemento para compararlo y contar la canridad de repeticiones
        if i ==k:
            cont+=1
            tupla=(i,cont)   #Se nos va a guardar el n° "i" q seria con el que lo estamos comparando y el contador de cuantas veces se repite
    listanueva.append(tupla)     #Agregamos la tupla a la lista 
listaset=set(listanueva)     #Seteamos la lista para no ver los elementos repetidos y de esta forma quda un solo contador de cada n°
print(listaset)

#6.	Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar ‘x’. A continuación, solicitar que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar ‘x’.



listanombresPrimaria=[]
listanombresSecundaria=[]
while True:
    nombresp=input('ingrese nombres de primaria, para finalizar ingrese X:\n')
    if nombresp!='x':
        listanombresPrimaria.append(nombresp)
    if nombresp=='x':
        break
while True:
    nombress=input('ingrese nombres de secundaria, para finalizar ingrese X:\n')
    if nombress!='x':
        listanombresSecundaria.append(nombress)
    if nombress=='x':
        break
#a.	Informar los nombres de todos los alumnos de nivel primario y de los de nivel secundario, sin repeticiones.    
todoslosnombres=listanombresPrimaria+listanombresSecundaria
nombressinrepetir=set(todoslosnombres)
print(nombressinrepetir)

#b.	Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.
nombresrepetidos=[]
nombresnorepetidos=[]
for i in listanombresPrimaria:
    for k in listanombresSecundaria:
        if i==k:
            nombresrepetidos.append(i)
        #c.	Informar qué nombres de nivel primario no se repiten en los de nivel secundario.
        if i not in listanombresSecundaria:
            nombresnorepetidos.append(i)
nombresrepetidos=set(nombresrepetidos)
nombresnorepetidos=set(nombresnorepetidos)
print(nombresrepetidos)
print(nombresnorepetidos)
#7.	Escribir un programa que procese strings ingresados por el usuario. La lectura finaliza cuando se hayan procesado 50 strings. Al finalizar, informar la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados. Ejemplo:
#‘r’:5
#‘%’:3
#‘a’:8
#‘9’:1

listastr=[]
contt=0
while True:
    string=input('ingrese una string: \n')
    listastr.append(string)
    contt+=1
    if contt==50:
        break
listanuevastr=[]
tuplastr=()
for i in listastr:
    cont=0
    for k in listastr:
        if i ==k:
            cont+=1
            tuplastr=(i,cont)
    listanuevastr.append(tuplastr)   

listaset=set(listanuevastr)            
print(listaset)

#8 trabajo de los equipos de futbol
def res(matriz, num):
    contvic = 0
    contderr = 0
    contemp = 0
    conpuntos = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i != j:
                if i == num:
                    if matriz[i][j] < matriz[j][i]:
                        contderr += 1
                    elif matriz[i][j] > matriz[j][i]:
                        contvic += 1
                        conpuntos += 3
                    else:
                        conpuntos += 1
                        contemp += 1
    listaestadisticas = [contvic, contderr, contemp, conpuntos]
    return listaestadisticas


def dif(matriz, num):
    sum = 0
    golesrecibidos = 0
    cont = 0
    for i in matriz[num]:
        sum += i
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                if i != j:
                    if cont == 3:
                        break
                    if i == num:
                        golesrecibidos += matriz[j][i]

                        cont += 1
    res = sum - golesrecibidos

    return f"equipo{num+1} la diferencia es : {res} "


matriz = [[0, 4, 2, 1], [5, 0, 3, 2], [0, 2, 0, 1], [1, 0, 2, 0]]

estadisticasequipo1 = res(matriz, 0)
print(
    f"Equipo 1: Victorias={estadisticasequipo1[0]}, Derrotas={estadisticasequipo1[1]}, Empates={estadisticasequipo1[2]}, puntosTotales= {estadisticasequipo1[3]}"
)
dif1 = dif(matriz, 0)
print(dif1)


estadisticasequipo2 = res(matriz, 1)
print(
    f"Equipo 2: Victorias={estadisticasequipo2[0]}, Derrotas={estadisticasequipo2[1]}, Empates={estadisticasequipo2[2]},  puntosTotales= {estadisticasequipo2[3]}"
)
dif2 = dif(matriz, 1)
print(dif2)

estadisticasequipo3 = res(matriz, 2)
print(
    f"Equipo 3: Victorias={estadisticasequipo3[0]}, Derrotas={estadisticasequipo3[1]}, Empates={estadisticasequipo3[2]}, puntosTotales= {estadisticasequipo3[3]}"
)
dif3 = dif(matriz, 2)
print(dif3)

estadisticasequipo4 = res(matriz, 3)
print(
    f"Equipo 4: Victorias={estadisticasequipo4[0]}, Derrotas={estadisticasequipo4[1]}, Empates={estadisticasequipo4[2]}, puntosTotales= {estadisticasequipo4[3]}"
)
dif4 = dif(matriz, 3)
print(dif4)
#9
import random

# Función para crear un tablero con cartas aleatorias
def crear_tablero(filas, columnas):
    numeros = list(range(1, filas * columnas // 2 + 1))
    cartas = numeros + numeros
    random.shuffle(cartas)
    tablero = [[0] * columnas for _ in range(filas)]

    for fila in range(filas):
        for columna in range(columnas):
            tablero[fila][columna] = cartas.pop()

    return tablero

# Función para imprimir el tablero con cartas boca abajo
def imprimir_tablero(tablero, filas, columnas):
    for fila in range(filas):
        for columna in range(columnas):
            if tablero[fila][columna] == 0:
                print("?", end="\t")
            else:
                print("X", end="\t")
        print()

# Función para jugar al Memotest
def jugar_memotest(tablero, filas, columnas):
    parejas_encontradas = 0
    while parejas_encontradas < filas * columnas // 2:
        imprimir_tablero(tablero, filas, columnas)
        fila1 = int(input("Ingresa la fila de la primera carta: ")) - 1
        columna1 = int(input("Ingresa la columna de la primera carta: ") - 1)
        fila2 = int(input("Ingresa la fila de la segunda carta: ")) - 1
        columna2 = int(input("Ingresa la columna de la segunda carta: ") - 1)

        if (
            0 <= fila1 < filas
            and 0 <= columna1 < columnas
            and 0 <= fila2 < filas
            and 0 <= columna2 < columnas
            and (fila1, columna1) != (fila2, columna2)
            and tablero[fila1][columna1] == tablero[fila2][columna2]
        ):
            print("¡Encontraste una pareja!")
            tablero[fila1][columna1] = 0
            tablero[fila2][columna2] = 0
            parejas_encontradas += 1
        else:
            print("No es una pareja válida. Inténtalo de nuevo.")

    print("¡Has encontrado todas las parejas!")

# Tamaño del tablero
filas = 4
columnas = 4

# Crear y jugar el Memotest
tablero = crear_tablero(filas, columnas)
jugar_memotest(tablero, filas, columnas)
#10

def obtener_diagonales(matriz):
    # Obtener la longitud de la matriz (dimensión)
    n = len(matriz)
    
    # Inicializar listas para almacenar las diagonales
    diagonal_principal = []
    diagonal_inversa = []
    
    # Recorrer la matriz para obtener las diagonales
    for i in range(n):
        diagonal_principal.append(matriz[i][i])  # Elementos de la diagonal principal
        diagonal_inversa.append(matriz[i][n - 1 - i])  # Elementos de la diagonal inversa
    
    return diagonal_principal, diagonal_inversa

# Ejemplo de una matriz cuadrada
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

diagonal_principal, diagonal_inversa = obtener_diagonales(matriz)

print("Diagonal Principal:", diagonal_principal)
print("Diagonal Inversa:", diagonal_inversa)
#11

dicc={'Euro':'€',
    'Dolar':'$',
    'Yen':'¥'}

question=input('que divisa desea ver? \n')

if question in dicc:
    print(f'si esta, el simbolo es: {dicc[question]}')
else:
    print('no se encuentra la divisa')    

#12

dic={}
nombre=input('ingrese nombre: ')
dic['nombre']=nombre
edad=input('ingrese edad: ')
dic['edad']=edad
direccion=input('ingrese direccion: ')
dic['direccion']=direccion
telefono=input('ingrese telefono: ')
dic['telefono']=telefono
print(dic)