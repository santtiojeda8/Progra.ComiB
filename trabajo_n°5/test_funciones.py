import pytest
from funciones import *

#1
@pytest.mark.parametrize("dni_number,res",[
    (94205043,True),
    (45966570,True),
    (4569925,False),
    (55,True)
])
def test_digits(dni_number,res):
    assert digits(dni_number)==res

#2
@pytest.mark.parametrize("phrase,res",[
    ("Como estas","estas"),
    ("La vida es una","una"),
    ("Que lindo es jugar","que")
])
def test_last_word(phrase,res):
    assert last_word(phrase)==res

#3
@pytest.mark.parametrize("last_name,res",[
    ("ojeda","5"),
    ("bosich","6"),
    ("Astudillo","9"),
    ("Guidolin","2")
])
def test_cant_digits(last_name,res):
    assert cant_digits(last_name)==res 

@pytest.mark.parametrize("dni_number,res",[
    (94205043,"942"),
    (45966570,"459"),
    (24524523,"523")
])
def test_first_digits(dni_number,res):
    assert first_digits(dni_number)==res

#4
@pytest.mark.parametrize("num1,num2,res",[
    (8,4,True),
    (10,5,True),
    (2,5,True)
])
def test_multi(num1,num2,res):
    assert multi(num1,num2)==res

#5
@pytest.mark.parametrize("a,b,res",[
    (20,10,15),
    (10,5,7.5),
    (10,6,8),
    (25,10,17.5)
])
def test_temperature(a,b,res):
    assert temperature(a,b)==res

#6
@pytest.mark.parametrize("a,res",[
    ("hola","h o l a "),
    ("adios","a d i o s "),
    ("bueno","bueno")
])
def test_space(a,res):
    assert space(a)==res

#7
@pytest.mark.paramnetrize("number_ls,res",[
    (3,2),
    (5,3),
    (6,6)
])
def test_max_and_min(number_ls,res):
    assert max_and_min(number_ls)==res

#9
@pytest.mark.parametrize("user,password,attempt,res",[
    ("usuario1","asdasd",1,True),
    ("santiago","colo",2,3)
])
def test_login(user,password,attempt,res):
    assert login(user,password,attempt)==res