#AHORCADO
import random
def word_select(a):
    num_ramdom=random.choice(a)
    print("Palabra seleccionada")
    word=num_ramdom
    return word
def show_word(letter,word,spaces):
    for i,ch in enumerate(word):
        if ch==letter:
            spaces[i]=letter
    return spaces

list=["phyton","java","variables","funciones","hardware"]
lives=6
while True:
    word=word_select(list)
    spaces=["_"]*len(word)
    while True:
        letter=input("Ingrese una letra")
        if letter in word:
            print (" ".join(show_word(letter,word,spaces)))
        else:
            print("Fallo -1 vida")
            print (" ".join(show_word(letter,word,spaces)))
            lives-=1
        if lives==0:
            print("Perdiste")
            lives=6
            break

        if "_" not in spaces:
            print("!Ganaste¡") 
            break
    while True:
        decision=input("desea jugar de nuevo? SI/NO")
        if decision.lower()=="si":
            print("Reiniciando partida")
            break
        elif decision.lower()=="no":
            print("Muchas gracias por jugar")
            break
        else:
            print("Ingrese una opcion valida")
    if decision=="no":
        break