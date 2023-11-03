import Funciones  #Importamos las funciones

dna=(Funciones.AdnCreation())  #Guardamos los datos ingresados ya validados en una variable

Funciones.line_validation(dna) #Validamos si se encuentra la secuencia mutante dentro de las filas del ADN

Funciones.column_validation(dna)  #Validamos si se encuentra la secuencia mutante dentro de las columnas del ADN

Funciones.diagonal_validation(dna)  #Validamos si se encuentra la secuencia mutante dentro de las diagonales hacia abajo del ADN

Funciones.diagonal2_validation(dna)  #Validamos si se encuentra la secuencia mutante dentro de las diagonales hacia arriba del ADN

if Funciones.is_mutant(dna): #Segun el resultado de la validacion de si es mutante o no mostramos alguno de los siguientes mensajes al usuario
    print("Se encontro el gen mutante dentro del ADN del ser humano")
else:
    print("No se encontro el gen mutante dentro del ADN del ser humano")



#ADN DE PRUEBA 
#El suguiente ADN nos devuelve que es mutante
#dna=[
#    "acgttg",
#    "gtaacc",
#    "ggggtt",
#    "gtatag",
#    "gaacac",
#    "cacaca",
# ]

#El siguiente ADN nos devuelve que no es mutante
#dna=[
#    "actgca",
#    "cgtatt",
#    "tgaaat",
#    "caccaa",
#    "tgaagc",
#    "accaac",
# ]