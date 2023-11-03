def AdnCreation():  #Función para validar que los datos ingresados esten correctos
    dna=[]  #Creamos la lista donde vamos a almacenar el ADN
    for i in range(6):
        line_dna=input("Ingrese una linea de ADN con los caracteres (A,C,G,T): ACGTGT  ")
        validation=False
        while True:
            if len(line_dna)==6:  #Validamos que haya ingresado 6 caracteres
                for j in line_dna:
                    if j.lower()=="a" or j.lower()=="c" or j.lower()=="t" or j.lower()=="g":  #Validamos que si o si sean caracteres permitidos
                        validation=True
                    else:
                        validation=False
                if validation==True:  #Una vez validados si estan bien avisamos que estan bien ingresados y los agregamos al adn en mayúsculas
                    print("Linea correcta")
                    dna.append(line_dna.upper())
                    break
                else:  #Si estan mal pedimos que los vuelvan a ingresar
                    print("Linea incorrecta")
                    line_dna=input("Ingrese la linea nuevamente  ")
            else:  #Si no hay 6 caracteres pedimos que ingrese nuevamente los datos
                print("Linea incorrecta")
                line_dna=input("Ingrese la linea nuevamente  ")
    return dna

def line_validation(dna):  #Funcion para validar las filas
    for i in range(3):
        for j in range(3):
            if dna[j][i]==dna[j][i+1] and dna[j][i+1]==dna[j][i+2] and dna[j][i+2]==dna[j][i+3]:  #Validamos el primer caracter del indice que pedimos y los tres siguientes
                return True  #Si se encuentra el Gen Mutante nos devuelve True


def column_validation(dna):  #Funcion para validar las columnas
    for i in range(3):
        for j in range(3):
            if dna[j][i]==dna[j+1][i] and dna[j+1][i]==dna[j+2][i] and dna[j+2][i]== dna[j+3][i]:  #Validamos el primer caracter del indice que pedimos y los tres de abajo
                return True  #Si se encuentra el Gen Mutante nos devuelve True

def diagonal_validation(dna):
    for i in range (3):
        for j in range(3):
            if dna[j][i]==dna[j+1][i+1] and dna[j+1][i+1]==dna[j+2][i+2] and dna[j+3][i+3]:  #Validamos el primer caracter del indice que pedimos y los tres siguientes en diagonal hacia abajo
                return True  #Si se encuentra el Gen Mutante nos devuelve True

def diagonal2_validation(dna):
    for i in range(5,2,-1):
        for j in range(3):
            if dna[i][j]==dna[i-1][j+1] and dna[i-1][j+1]==dna[i-2][j+2] and dna[i-2][j+2]==dna[i-3][j+3]:  #Validamos el primer caracter del indice que pedimos y los tres siguientes en diagonal hacia arriba
                return True  #Si se encuentra el Gen Mutante nos devuelve True

def is_mutant(dna):  #Funcion para saber si el humano es mutante o no
    counter=0  #Contador para  saber la cantidad de veces que se encontro la coincidencia necesaria
    if line_validation(dna):
        counter+=1
    if column_validation(dna):
        counter+=1
    if diagonal_validation(dna):
        counter+=1
    if diagonal2_validation(dna):
        counter+=1
    if counter>=2:  #Si se encontraron 2 o mas coincidencias es mutante y nos devuelve True
        return True
