from collections import namedtuple
import csv
from datetime import date, time, datetime
Persona=namedtuple('persona','dni, nombre, apellidos, edad,\
                    estatura, peso, localidad, provincia')
Persona2=namedtuple('persona','dni, nombre, apellidos, edad,\
                    estatura, peso, localidad, provincia, esmujer')
Persona3=namedtuple('persona','dni, nombre, apellidos, edad,\
                    estatura, peso, localidad, provincia, esmujer, hobbies')
Persona4=namedtuple('persona','dni, nombre, apellidos, edad,\
                    estatura, peso, localidad, provincia, esmujer, hobbies, fecha, hora')

def lee_datos_personales(ruta:str)->list[Persona]:
    res=list()
    with open(ruta,'rt',encoding='utf-8') as f:
        lector=csv.reader(f, delimiter=';')
        next(lector)
        for dni, nombre, apellidos, edad,\
              estatura, peso, localidad, provincia in lector:
            edad=int(edad)
            estatura=float(estatura)
            peso=float(peso)
            tupla=Persona(dni, nombre, apellidos, edad, estatura, peso, localidad, provincia)
            res.append(tupla)
    return res

def es_mujer(ruta:str)->bool:
    res=False
    if ruta=="SI":
        res=True    
    return res

def lee_datos_personales2(ruta:str)->list[Persona2]:
    res=list()
    with open(ruta, 'rt', encoding='utf-8')as f:
        lector=csv.reader(f, delimiter=';')
        next(lector)
        for dni, nombre, apellidos, edad, estatura, peso, localidad, provincia, esmujer in lector :
            edad=int(edad)
            estatura=float(estatura)
            esmujer=es_mujer(esmujer)
            nueva_tupla=Persona2(dni, nombre, apellidos, edad, estatura, float(peso.replace(',','.')), \
                                  localidad, provincia, esmujer)
            res.append(nueva_tupla)
    return res

def hobby(ruta:str)->list[str]:
    res=list()
    for i in ruta.split('/'):
        res.append(i)
    return res

def lee_datos_personales3(ruta:str)->list[Persona3]:
    res=list()
    with open(ruta, 'rt', encoding='utf-8')as f:
        lector=csv.reader(f, delimiter=';')
        next (lector)
        for dni, nombre, apellidos, edad, estatura, peso, localidad, provincia, esmujer, hobbies in lector :
            edad=int(edad)
            estatura=float(estatura)
            esmujer=es_mujer(esmujer)
            #esmujer=(esmujer=="SI") en el lugar de funcion es_mujer
            hobbies=hobby(hobbies)
            tupla3=Persona3(dni, nombre, apellidos, edad, estatura, float(peso.replace(',','.')), \
                             localidad, provincia, esmujer, hobbies)
            res.append(tupla3)
    return res

'''def parsea_fecha_hora(ruta:str)->list[str]:
    res=list()
    for i in ruta.split('#'):
        res.append(i)
    return res'''

def lee_datos_personales4(ruta:str)->list[Persona4]:
    res=list()
    with open(ruta, 'rt', encoding='utf-8')as f:
        lector=csv.reader(f, delimiter=';')
        next (lector)
        for dni, nombre, apellidos, edad, estatura, peso, localidad, provincia, esmujer, hobbies, fecha_hora in lector:
            edad= int(edad)
            estatura= float(estatura)
            esmujer= es_mujer(esmujer)
            hobbies= hobby(hobbies)
#            fecha_hora= parsea_fecha_hora(fecha_hora)
#            fecha= datetime.strptime(fecha_hora[0], "%d/%m/%Y").date()
#            hora= datetime.strptime(fecha_hora[1], "%H:%M:%S").time()
#            fecha= fecha.strftime("%d/%m/%Y")
#            hora= hora.strftime("%H:%M:%S")            
            fecha= datetime.strptime(fecha_hora, "%d/%m/%Y#%H:%M:%S").date()
            hora= datetime.strptime(fecha_hora, "%d/%m/%Y#%H:%M:%S").time()
            tupla4=Persona4(dni, nombre, apellidos, edad, estatura, peso, \
                             localidad, provincia, esmujer, hobbies,fecha, hora)
            res.append(tupla4)
    return res

def todos_entran_entre_anos(personas:list[Persona4], ano1:int, ano2:int)->bool:
    res=True
    for p in personas:
#        if p.fecha.year<ano1 or ano2<p.facha.year:
        if not(ano1<=p.fecha.year<=ano2):
            res=False
            break
    return res
            
def alguien_ha_madrugado(personas:list[Persona4], hora:int)->bool:
    res=False
    for p in personas:
        if p.hora.hour<hora:
            res=True
            break
    return res

def persona_mas_alta(lista:list[Persona4])->tuple:
    #persona=max(lista, key=lambda e:e.estatura)
    #return(lista.apellidos, lista.nombre)
    estatura_i=0
    res=[]
    for p in lista:
        if p.estatura>estatura_i:
            estatura_i = p.estatura
    res=(p.apellidos, p.nombre)
    return res

def relacion_alfabetica_de_personas(lista:list[Persona4])->list:
    res=[]
    for p in lista:
        res.append((p.apellidos, p.nombre, p.edad))
    return sorted(res)

def n_personas_mayor_de_edad(lista:list[Persona4], n:int)->list:
    res=[]
    for p in lista:
        res.append((p.edad, p.dni, p.peso, p.estatura))
    return sorted(res, key=lambda e:e[0], reverse=True)[:n]