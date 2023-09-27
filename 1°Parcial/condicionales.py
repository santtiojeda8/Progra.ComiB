dia_dd_mm=input('dia, dd/mm')
diaS=dia_dd_mm[0:dia_dd_mm.find(',')].lower()
dd=dia_dd_mm[dia_dd_mm.find(' ')+1:dia_dd_mm.find('/')]
mm=dia_dd_mm[dia_dd_mm.find('/')+1:]
print(f'{diaS}/{dd}/{mm}')


if(diaS=='lunes' or diaS=='martes' or diaS=='miercoles' or diaS=='jueves' or diaS=='viernes' or 
    diaS=='sabado' or diaS=='domingo' ) and (int(dd)>0 and int(dd)<=31) and (int(mm)>0 and int(mm)<=12):
    print('la fecha es valida') 
if(diaS=='lunes' ):
    print('Clases nivel inicial')
    cantAlumnos=int(input('cuantos alumnos hay: '))
    aprobados=int(input('cuantos alumnos aprobaron: '))    
    print(f'el porcentaje de alumnos aprobados es: {(aprobados*100)/cantAlumnos}')
    
elif(diaS=='martes'):
    print('Clases nivel intermedio')
    cantAlumnos=int(input('cuantos alumnos hay: '))
    aprobados=int(input('cuantos alumnos aprobaron: '))   
    print(f'el porcentaje de alumnos aprobados es: {(aprobados*100)/cantAlumnos}')
    
elif(diaS=='miercoles'):
    print('Clases nivel avanzado')
    cantAlumnos=int(input('cuantos alumnos hay: '))
    aprobados=int(input('cuantos alumnos aprobaron: '))
    print(f'el porcentaje de alumnos aprobados es: {(aprobados*100)/cantAlumnos}')

elif(diaS=='jueves'):
    print('dia de practica hablada no se dicta ningun examen')
    porc=float(input('ingrese porcentaje a clases: '))
    if(porc>=50):
        print('aisitio a la mayoria de las clases')
    else:
        print('no asistio a la mayoria de la clase')

    
elif(diaS=='viernes') and  ((int(dd)==1 and int(mm)==1) or (int(dd)==1 and int(mm)==7)) :

    print('Comienzo de nuevo ciclo')
    alum_nuevo_ciclo=int(input('ingrese cantidad de alumnos del nuevo ciclo: '))
    cuota=float(input('ingrese valor cuota: '))
    total=alum_nuevo_ciclo*cuota
    print(f'el total que recibe el colegio es: {total}$')
    
    # print('Dia de ingles extranjero no se dictan examenes')
else:
    print('la fecha es invalida')