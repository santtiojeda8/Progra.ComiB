pc=30
mouse=80
keyboard=80
screen=30
total=0
election=""
print("Bienvenidos a MegaTecnología")
total_products=[]
while True:
    if election.lower() == "no":
        break
    if election == "":
        decision=input("Desea realizar alguna compra? SI/NO")
    if (decision.lower() == "no"):
        print("Hasta Pronto")
        break
    elif(decision.lower() != "si"):
        print("La decision ingresada no es válida, ingrese una opción válida")
        continue
    print("Los productos que tenemos en stock son: 1_pc($2000), 2_mouse($800), 3_keyboard($600), 4_screen($200), 5_salir")
    while True:
        product=int(input("Que producto desea comprar? (Ingrese 0 si desea terminar la operación)"))
        if product>0 and product<6:
            break
        else:
            print("Valor inválido")
    if product == 0:
        break
    if product == 1 :
        while True:
            amount=int(input("Cuantas PC desea comprar?"))
            if amount == 0:
                print("Muchas Gracias!!")
            elif(amount <0):
                print("Ingrese una opción válida")
                continue
            else:
                if amount>pc:
                    print("Lo sentimos, no hay de este producto en stock")
                    break
                else:
                    pc-=amount
                    total+=amount*2000
                    total_products.append("PC")
                    print(f"El total actual es de {total}")
                    while True:
                        election=input("Desea seguir comprando? SI/NO")
                        if election.lower() == "si" or election.lower()=="no":
                            break
                        else:
                            print("Ingrese una opcion válida")
                    if election.lower()=="si":
                        break
                    elif election.lower()=="no":
                        break
    if product == 2 :
        while True:
            amount=int(input("Cuantos mouse desea comprar?"))
            if amount == 0:
                print("Muchas Gracias!!")
            elif(amount <0):
                print("Ingrese una opción válida")
                continue
            else:
                if amount>mouse:
                    print("Lo sentimos, no hay de este producto en stock")
                    break
                else:
                    mouse-=amount
                    total+=amount*800
                    total_products.append("Mouse")
                    print(f"El total actual es de {total}")
                    while True:
                        election=input("Desea seguir comprando? SI/NO")
                        if election.lower() == "si" or election.lower()=="no":
                            break
                        else:
                            print("Ingrese una opcion válida")
                    if election.lower()=="si":
                        break
                    elif election.lower()=="no":
                        break
    if product == 3 :
        while True:
            amount=int(input("Cuantos teclados desea comprar?"))
            if amount == 0:
                print("Muchas Gracias!!")
            elif(amount <0):
                print("Ingrese una opción válida")
                continue
            else:
                if amount>keyboard:
                    print("Lo sentimos, no hay de este producto en stock")
                    break
                else:
                    keyboard-=amount
                    total+=amount*600
                    total_products.append("Teclado")
                    print(f"El total actual es de {total}")
                    while True:
                        election=input("Desea seguir comprando? SI/NO")
                        if election.lower() == "si" or election.lower()=="no":
                            break
                        else:
                            print("Ingrese una opcion válida")
                    if election.lower()=="si":
                        break
                    elif election.lower()=="no":
                        break
    if product == 4 :
        while True:
            amount=int(input("Cuantas pantallas desea comprar?"))
            if amount == 0:
                print("Muchas Gracias!!")
            elif(amount <0):
                print("Ingrese una opción válida")
                continue
            else:
                if amount>screen:
                    print("Lo sentimos, no hay de este producto en stock")
                    break
                else:
                    screen-=amount
                    total+=amount*200
                    total_products.append("Pantalla")
                    print(f"El total actual es de {total}")
                    while True:
                        election=input("Desea seguir comprando? SI/NO")
                        if election.lower() == "si" or election.lower()=="no":
                            break
                        else:
                            print("Ingrese una opcion válida")
                    if election.lower()=="si":
                        break
                    elif election.lower()=="no":
                        break
    if product==5:
        print("Muchas gracias por elegirnos")
        break

product_list=set(total_products)
print("Los productos que compro son:")
for i in product_list:
    print(i,end=" ")