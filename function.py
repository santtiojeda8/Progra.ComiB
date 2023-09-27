
#EJERCICIO FUNCIONES 1°
def most (x,y):
    if (x>y):
        return x
    else:
        return y

def least(x,y):
    if (x<y):
        return x
    else:
        return y

x=int(input("Ingrese el valor de x"))
y=int(input("Ingrese el valor de y"))

print(most(x-3,least(x+2,y-5)))

#EJEMPLO DE OTRA FORMA DE APLICAR
def add_diigits(number):
    add=0
    while number !=0:
        digit=number%10
        add +=digit
        number //=10
    return add

total_number=0
while True:
    number=int(input("Ingrese un numero (0 para finalizar)"))
    if number==0:
        break
    sum=add_diigits(number)
    total_number+=number
    print(f"Suma de digitos: {sum}")
sum=add_diigits(total_number)
print(f"La suma de todos los numero ingresado es de: {total_number}")
print(f"Y la suma de sus digitos es igual a: {sum}")


