from clases import Motocicleta
moto1=Motocicleta(gas_lts=10,num_wheels=2,model="H2R",mark="Kawasaki")  
moto2=Motocicleta(gas_lts=10,num_wheels=2,mark="Honda",model="Wave")
moto1.Arrancar()
moto2.Detener()
print(moto1.gas_lts,moto1.num_wheels)
moto1.price_1=3500
moto1.price()
moto2.price()