# 1.Escribir una función que reciba un número positivo n y devuelva la cantidad de dígitos que tiene.

def digits(n):
    if n<10:
        return 1
    else:
        return 1+digits(n//10)

num=123
print(digits(num))


# 2.	Escribir una función que reciba 2 enteros n y b y devuelva True si n es potencia de b.


def potencia(a,b):
    if a==1:
        return True
    elif a<b:
        return False
    else:
        return potencia(a/b,b)

a=7
b=2
print(potencia(a,b))



# 3.	Escribir una funcion recursiva que reciba como parámetros dos strings a y b, y devuelva una lista con las posiciones en donde se encuentra b dentro de a.
def posiciones(a, b, start=0, positions=None):
    if positions is None:
        positions = []

    if start >= len(a):
        return positions

    index = a.find(b, start)

    if index != -1:
        positions.append(index)
        return posiciones(a, b, index + 1, positions)
    else:
        return positions


a = "un tete a tete con Tete"
b = "te"
result = posiciones(a, b)
print(result)
# 4 4.	Escribir dos funciones mutualmente recursivas par(n) e impar(n) que determinen la paridad del numero natural dado, conociendo solo que:
# 1 es impar.
# Si un número es impar, su antecesor es par; y viceversa.

def par(n):
    if n == 0:
        return True  
    else:
        return impar(n - 1)

def impar(n):
    if n == 0:
        return False  
    else:
        return par(n - 1)


numero = 5
if impar(numero):
    print(f"{numero} es impar.")
else:
    print(f"{numero} es par.")



#5.	Escribir una función recursiva que encuentre el mayor elemento de una lista.


def encontrar_mayor_elemento(lista):
    # Caso base: Si la lista está vacía, no hay ningún elemento para comparar.
    if not lista:
        return None

    # Caso base: Si la lista tiene solo un elemento, ese es el mayor.
    if len(lista) == 1:
        return lista[0]

    # Encontrar el mayor elemento entre el primero y el resto de la lista.
    primer_elemento = lista[0]
    resto_de_la_lista = lista[1:]
    mayor_del_resto = encontrar_mayor_elemento(resto_de_la_lista)

    # Comparar el mayor del resto con el primer elemento y devolver el máximo.
    return primer_elemento if primer_elemento > mayor_del_resto else mayor_del_resto


lista = [5, 8, 2, 10, 15, 3]
mayor = encontrar_mayor_elemento(lista)
print(f"El mayor elemento de la lista es: {mayor}")
#6.	Escribir una función recursiva para replicar los elementos de una lista una cantidad n de veces. Por ejemplo, replicar ([1, 3, 3, 7], 2) = ([1, 1, 3, 3, 3, 3, 7, 7])
def replicar_lista(lista, n):
    # Caso base: Si la lista está vacía o n es 0, no se replica nada.
    if not lista or n == 0:
        return []

    # Caso base: Si n es 1, la lista se deja sin cambios.
    if n == 1:
        return lista

    # Obtenemos el primer elemento de la lista y replicamos el resto de la lista n-1 veces.
    primer_elemento = lista[0]
    resto_de_la_lista_replicada = replicar_lista(lista, n - 1)

    # Concatenamos el primer elemento con el resto replicado.
    return [primer_elemento] + resto_de_la_lista_replicada


lista = [1, 3, 3, 7]
n = 2
lista_replicada = replicar_lista(lista, n)
print(lista_replicada)
#7.	Implemente un algoritmo, usando una función recursiva, que resuelva la siguientesumatoria:
#K(n, p) = p + 2 ∗ p + 3 ∗ p + 4 ∗ p + … + n ∗ p
#● El programa debe pedir al usuario que ingrese un número n, y un número d,
#● Luego debe calcular el valor de K(n, p) usando una función recursiva,
#● Debe imprimir el resultado de K(n, p)
def calcular_sumatoria(n, p):
    if n == 1:
        return p
    else:
        return n * p + calcular_sumatoria(n - 1, p)

def main():
    try:
        n = int(input("Ingrese el valor de n: "))
        p = int(input("Ingrese el valor de p: "))
        
        resultado = calcular_sumatoria(n, p)
        
        print(f"El resultado de K({n}, {p}) es: {resultado}")
    except ValueError:
        print("Por favor, ingrese números enteros válidos.")

if __name__ == "__main":
    main()
#8.	El triángulo de Pascal es un arreglo triangular de números que se define de la siguiente manera: Las filas se enumeran desde n = 0, de arriba hacia abajo. Los valores de cada fila se enumeran desde k = 0 (de izquierda a derecha). Los valores que se encuentran en los bordes del triángulo son todos unos. Cualquier otro valor se calcula sumando los dos valores contiguos de la fila de arriba. Escribí la función recursiva pascal(n, k) que calcula el valor que se encuentra en la fila n y la columna k.
def pascal(n, k):
    if k == 0 or k == n:
        return 1  # Los valores en los bordes siempre son 1.
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)


fila = 5
columna = 2
valor = pascal(fila, columna)
print(f"El valor en la fila {fila} y la columna {columna} es: {valor}")
#9.	Escribí una función recursiva combinaciones(lista, k) que reciba una lista de caracteres únicos, y un número k, e imprima todas las posibles cadenas de longitud k formadas con los caracteres dados (permitiendo caracteres repetidos).
def combinaciones(lista, k, cadena_actual="", indice=0):
    if k == 0:
        print(cadena_actual)
        return
    if indice == len(lista):
        return

    # Incluye el carácter actual en la cadena y continúa la recursión
    combinaciones(lista, k - 1, cadena_actual + lista[indice], indice)

    # Omite el carácter actual y continúa la recursión
    combinaciones(lista, k, cadena_actual, indice + 1)


lista_de_caracteres = ['a', 'b', 'c']
k = 2
combinaciones(lista_de_caracteres, k)

#10.	La norma ISO 216 especifica tamaños de papel. Es el estándar que define el popular tamaño de papel A4 (210 mm de ancho y 297 mm de largo). Las hojas A0 miden 841 mm de ancho y 1189 mm de largo. A partir de la A0 las siguientes medidas, digamos la A(N+1), se definen doblando al medio la hoja A(N). Siempre se miden en milímetros con números enteros: entonces la hoja A1 mide 594 mm de ancho (y no 594.5) por 841 mm de largo.
def calcular_dimensiones_papel(n):
    if n < 0:
        return None
    elif n == 0:
        return (841, 1189)  # Dimensiones de A0
    else:
        dimensiones_anterior = calcular_dimensiones_papel(n - 1)
        ancho, largo = dimensiones_anterior
        if n % 2 == 0:
            return (largo // 2, ancho)  # Doblar al medio en la dirección más corta
        else:
            return (largo, ancho // 2)  # Doblar al medio en la dirección más larga


n = 4  # Cambia esto para calcular dimensiones para otros tamaños A(N)
dimensiones = calcular_dimensiones_papel(n)
if dimensiones is not None:
    ancho, largo = dimensiones
    print(f"Las dimensiones de A{n} son: {ancho} mm x {largo} mm")
else:
    print("Tamaño no válido.")







