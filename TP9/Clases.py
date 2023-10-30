class Persona:
    def __init__(self):
        self.__nombre=""
        self.__edad=int(0)
        self.__dni=int(0)
    
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,new_at):
        self.__nombre=new_at
    
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self,new_at):
        self.__edad=new_at
    
    @property
    def dni(self):
        return self.__dni
    @dni.setter
    def dni(self,new_at):
        self.__dni=new_at
    
    def mostrar(self):
        print(f"Nombre: {self.__nombre} \nEdad: {self.__edad} \nDNI: {self.__dni}")
    
    def esMayorDeEdad(self):
        if self.__edad>18:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")

class Cuenta:
    def __init__(self):
        self.__titular=""
        self.__cantidad=float(0.0)
    @property
    def titular(self):
        return self.__titular
    @titular.setter
    def titular(self,new):
        self.__titular=new
    @property
    def cantidad(self):
        return self.__cantidad
    @cantidad.setter
    def cantidad(self,new):
        self.__cantidad=new
    def mostrar(self):
        print(f"Titular: {self.__titular} \nCantidad: {self.__cantidad}")
    def ingresar(self,cant):
        if cant<0:
            return print("no se puede ingresar cantidades negativas")
        else:
            self.__cantidad+=cant
            print("Operacion finalizada")
    def retirar(self,cant):
        if cant>self.__cantidad:
            print("saldo insuficiente")
        else:
            self.__cantidad-=cant
            print("Operacion finalizada")

class Triangulo:
    def __init__(self,lado1=0,lado2=0,lado3=0):
        self.lado1=lado1
        self.lado2=lado2
        self.lado3=lado3
    def MayorLado(self):
        max=self.lado1
        if max<self.lado2:
            max=self.lado2
        elif max<self.lado3:
            max=self.lado3
        print(max)
    def tipoTriangulo(self):
        if self.lado1==self.lado2 and self.lado2==self.lado3:
            print("El triangulo es un triangulo equilatero")
        elif self.lado1==self.lado2 or self.lado2==self.lado3 or self.lado2==self.lado3:
            print("EL trinagulo es isóscles")
        elif self.lado1!=self.lado2 and self.lado2!=self.lado3:
            print("El trinagulo es escaleno")

class Agenda:
    def __init__(self,contacto='',nombre='',telefono='',mail=''):
        self.nombre=nombre
        self.contacto=contacto
        self.telefono=telefono
        self.mail=mail
    def mostrarOpciones(self):
        print(f"Añadir Contacto \nLista de Contacto \nBuscar Contacto \nEditar Contacto \nCerrar Agenda")
    def mostrar(self):
        print(f"Contacto: {self.contacto}\nNombre: {self.nombre}\nNúmero: {self.telefono}\nMail: {self.mail}")