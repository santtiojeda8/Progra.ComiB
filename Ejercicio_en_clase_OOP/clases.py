class Motocicleta:
    new=True
    motor=False
    def __init__(self,color='',number_plate='',gas_lts='',num_wheels='',mark='',model='',date_fabric='',top_speed='',weight=''):
        self.color=color
        self.number_plate=number_plate
        self.gas_lts=gas_lts
        self.num_wheels=num_wheels
        self.mark=mark
        self.model=model
        self.date_fabric=date_fabric
        self.top_speed=top_speed
        self.weight=weight
    def Arrancar(self):
        if self.motor:
            print("Motor Ya Encendido")
        else:
            print("Encendiendo Motor")
            print("Motor Encendido")
            self.motor=True
    def Detener(self):
        if self.motor:
            print("Deteniendo Motor")
            print("Motor Detenido")
            self.motor=False
        else:
            print("Motor Ya Detenido")
    def price(self):
        print(f"El precio de la moto {self.mark} {self.model} es ${self.price_1}")

