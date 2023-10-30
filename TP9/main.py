from Clases import Persona
from Clases import Cuenta
from Clases import Triangulo
from Clases import Agenda
p1=Persona()
p1.edad=19
p1.nombre="Santiago"
p1.dni=234567
p1.mostrar()
p1.esMayorDeEdad()
c1=Cuenta()
c1.titular="Sebastian"
c1.cantidad=10000.21
c1.ingresar(2000)
c1.retirar(3000)
c1.mostrar()
t1=Triangulo()
t1.lado1=7
t1.lado2=6
t1.lado3=6
t1.MayorLado()
t1.tipoTriangulo()
a1=Agenda()
a1.contacto=1
a1.nombre="Santiago"
a1.telefono=2616852245
a1.mail="ojedasi2004@gmail.com"
a1.mostrar()
a1.mostrarOpciones()