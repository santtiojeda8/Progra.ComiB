#1.	Escribe un programa que tome una lista de números como entrada y la ordene en orden ascendente utilizando el método de ordenamiento de burbuja.
def ordenamiento_burbuja(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Función para ingresar una lista de números desde el teclado
def ingresar_lista():
    entrada = input("Ingresa una lista de números separados por espacios: ")
    numeros = [int(x) for x in entrada.split()]
    return numeros

# Programa principal
if __name__ == "__main__":
    lista = ingresar_lista()
    ordenamiento_burbuja(lista)

    print("Lista ordenada en orden ascendente:")
    print(lista)

#  2.	Crea un programa que tome una lista de palabras como entrada y las ordene alfabéticamente en orden ascendente utilizando el método de ordenamiento de selección.

def ordenamiento_seleccion(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Función para ingresar una lista de palabras desde el teclado
def ingresar_lista():
    entrada = input("Ingresa una lista de palabras separadas por espacios: ")
    palabras = entrada.split()
    return palabras

# Programa principal
if __name__ == "__main__":
    lista = ingresar_lista()
    ordenamiento_seleccion(lista)

    print("Lista ordenada alfabéticamente en orden ascendente:")
    print(" ".join(lista))


#3.	Crea una lista de diccionarios, donde cada diccionario contiene información sobre un libro (título, autor, año de publicación, etc.). Luego, escribe un programa que ordene la lista de libros en función de un campo específico, como el año de publicación o el autor.

libros = [
    {"titulo": "Iron Man", "autor": "G.Paulo Guidolin", "año": 2002},
    {"titulo": "Cenicienta", "autor": "Disney", "año": 1967},
    {"titulo": "El extraño mundo de jack", "autor": "Sheckpeasre", "año": 1860},

]

# Función para ordenar la lista de libros en función de un campo específico
def ordenar_libros_por_campo(libros, campo):
    return sorted(libros, key=lambda x: x[campo])

# Campo por el que deseamos ordenar los libros (en este caso, "año")
campo_ordenamiento = "año"

# Llamamos a la función de ordenamiento
libros_ordenados = ordenar_libros_por_campo(libros, campo_ordenamiento)

# Imprimimos la lista de libros ordenada
for libro in libros_ordenados:
    print(f"Título: {libro['titulo']}, Autor: {libro['autor']}, Año: {libro['año']}")
#4.	Escribe un programa que tome una lista de cadenas como entrada y las ordene en orden ascendente según su longitud. Puedes utilizar el método de ordenamiento de inserción.

def ordenamiento_insercion_por_longitud(cadenas):
    for i in range(1, len(cadenas)):
        cadena_actual = cadenas[i]
        j = i - 1
        while j >= 0 and len(cadena_actual) < len(cadenas[j]):
            cadenas[j + 1] = cadenas[j]
            j -= 1
        cadenas[j + 1] = cadena_actual

# Función para ingresar una lista de cadenas desde el teclado
def ingresar_cadenas():
    entrada = input("Ingresa una lista de cadenas separadas por espacios: ")
    cadenas = entrada.split()
    return cadenas

# Programa principal
if __name__ == "__main__":
    lista_cadenas = ingresar_cadenas()
    ordenamiento_insercion_por_longitud(lista_cadenas)

    print("Lista de cadenas ordenadas por longitud en orden ascendente:")
    for cadena in lista_cadenas:
        print(cadena)

#5.	Modifica uno de los ejercicios anteriores para ordenar la lista de números en orden descendente en lugar de ascendente.
def ordenamiento_burbuja_descendente(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:  # Cambio de '>' a '<' para orden descendente
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Ejemplo de uso:
lista = [64, 34, 25, 12, 22, 11, 90]
ordenamiento_burbuja_descendente(lista)
print("Lista ordenada en orden descendente:")
print(lista)         

#6.	Escribe un programa que tome una lista de números enteros y ordene la lista utilizando el algoritmo de ordenamiento por conteo.

def ordenamiento_por_conteo(arr):
    if len(arr) <= 1:
        return arr

    # Encuentra el valor máximo en la lista
    max_valor = max(arr)

    # Crea un arreglo de conteo para contar la ocurrencia de cada número
    conteo = [0] * (max_valor + 1)

    # Llena el arreglo de conteo con las ocurrencias de cada número en la lista
    for num in arr:
        conteo[num] += 1

    # Reconstruye la lista ordenada a partir del arreglo de conteo
    resultado = []
    for i in range(max_valor + 1):
        resultado.extend([i] * conteo[i])

    return resultado

# Ejemplo de uso:
lista = [4, 2, 2, 8, 3, 3, 1]
lista_ordenada = ordenamiento_por_conteo(lista)
print("Lista ordenada:")
print(lista_ordenada)


#7.	Crea una lista que contenga tanto números como cadenas de caracteres. Escribe un programa que ordene esta lista de manera que primero estén los números ordenados de menor a mayor y luego las cadenas de caracteres ordenadas alfabéticamente.

def ordenar_numeros_cadenas(lista):
    # Separar los números y las cadenas en listas separadas
    numeros = [x for x in lista if isinstance(x, (int, float))]
    cadenas = [x for x in lista if isinstance(x, str)]

    # Ordenar las listas
    numeros.sort()
    cadenas.sort()

    # Combinar las dos listas ordenadas
    lista_ordenada = numeros + cadenas

    return lista_ordenada

# Ejemplo de uso
lista = [3, 'manzana', 1, 'banana', 2.5, 'pera', 10, 'naranja']
lista_ordenada = ordenar_numeros_cadenas(lista)

print("Lista ordenada:")
print(lista_ordenada)

#8.	Implementa el algoritmo de ordenamiento Merge Sort y úsalo para ordenar una lista de números.

def merge_sort(arr):
    if len(arr) > 1:
        # Divide la lista en dos mitades
        mitad = len(arr) // 2
        mitad_izquierda = arr[:mitad]
        mitad_derecha = arr[mitad:]

        # Llama recursivamente a merge_sort para ordenar ambas mitades
        merge_sort(mitad_izquierda)
        merge_sort(mitad_derecha)

        i = j = k = 0

        # Combina las dos mitades ordenadas en la lista original
        while i < len(mitad_izquierda) and j < len(mitad_derecha):
            if mitad_izquierda[i] < mitad_derecha[j]:
                arr[k] = mitad_izquierda[i]
                i += 1
            else:
                arr[k] = mitad_derecha[j]
                j += 1
            k += 1

        while i < len(mitad_izquierda):
            arr[k] = mitad_izquierda[i]
            i += 1
            k += 1

        while j < len(mitad_derecha):
            arr[k] = mitad_derecha[j]
            j += 1
            k += 1

# Ejemplo de uso
lista = [64, 34, 25, 12, 22, 11, 90]
merge_sort(lista)
print("Lista ordenada utilizando Merge Sort:")
print(lista)
  