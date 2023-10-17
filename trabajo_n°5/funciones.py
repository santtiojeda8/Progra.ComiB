#1
def digits(dni_number):
    dni=str(dni_number)
    if len(dni)==7 or len(dni)==8:
        return True
    else:
        return False

#2
def last_word(phrase):
    word=phrase.split()
    if len(word)>1:
        return word[-1]
    else:
        return "Se ingreso una sola palabra"

#3
def cant_digits(last_name):
    cant_last_name=len(last_name)
    cant_last_name=str(cant_last_name)
    return cant_last_name

def first_digits(dni_number):
    dni_number=str(dni_number)
    dni_number=dni_number[:3]
    return dni_number

#4
def multi(num1,num2):
    if num1%num2==0:
        return True
    else:
        return False
#5
def temperature(max_temp,min_temp):
    average_temp=(max_temp+min_temp)/2
    return average_temp

#6
def space (phrase):
    word=""
    for i in phrase:
        word+=i+" "
    return word

#7
def max_and_min(number_ls):
    min=99999999
    max=0
    for i in number_ls:
        if i>max:
            max=i
        elif min<=i:
            min=min
        else:
            min=i
    return max,min

#8
def area(num,radio):
    area_circ=num*(radio**2)
    diameter=2*num*radio
    return area_circ,diameter

#9
def login(user,password,attempt):
    if user=="usuario1" and password=="asdasd":
        return True
    attempt +=1
    return attempt

#10 
def total(garment,discount):
    total_whit_discount={}
    for i in garment:
        if garment[i]<5000:
            total_whit_discount[i]=garment[i]-(garment[i]*discount["1"])
        elif garment[i]>=5000 and garment[i]<10000:    
            total_whit_discount[i]=garment[i]-(garment[i]*discount["2"])
        elif garment[i]>=10000:
            total_whit_discount[i]=garment[i]-(garment[i]*discount["3"])
    return total_whit_discount

#11
def first(list_of_number):
    for i in range(len(list_of_number)):
        list_of_number[i]=double(list_of_number,i)
    return list_of_number

def double(list_of_number,i):
    second_number=[]
    second_number.append(list_of_number[i]*2)
    return second_number
#12
def diccio(phrase):
    words={}
    j=0
    for i in phrase:
        j+=1
        words[j]=i
    return words

#13
def mod(num1,num2):
    import math
    modul=math.sqrt((num1**2)+(num2**2))
    return modul

#14
def primo(num):
    counter=0
    for i in range(1,num+1):
        if num%i==0:
            counter+=1
    if counter==2:
        return True
    else:
        return False

#15
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact

def counter(num1):
    account=0
    for i in range(num1):
        account+=1
    return account

#16
def frequency(num,num1):
    digits=str(num)
    counter=0
    for i in digits:
        if i==num1:
            counter+=1
    return counter

#17
def sum_digits(num):
    total=str(num)
    total=len(total)
    return total

def factorial_1(max):
    fact=1
    for i in range(1,max+1):
        fact=fact*i
    return fact
