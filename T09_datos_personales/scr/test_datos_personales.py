from datos_personales import *
def test_lee_datos_personales(personas:list[Persona]):
    print("\nel numero de registro es:", len(personas))
    print("\nel tercer registro es: ", personas[2])
    print("\nlos tres primeros: ", personas[:3])
    print("\nlos tres ultimos: ", personas[-3:])

def test_lee_datos_personales2(personas:list[Persona2]):
    print("\nel numero de registro es:", len(personas))
    print("\nel tercer registro es: ", personas[2])
    print("\nlos tres primeros: ", personas[:3])
    print("\nlos tres ultimos: ", personas[-3:])

def test_lee_datos_personales3(personas:list[Persona3]):
    print("\nel numero de registro es:", len(personas))
    print("\nel tercer registro es: ", personas[2])
    print("\nlos tres primeros: ", personas[:3])
    print("\nlos tres ultimos: ", personas[-3:])

def test_lee_datos_personales4(personas:list[Persona4]):
    print("\nel numero de registro es:", len(personas))
    print("\nel tercer registro es: ", personas[2])
    print("\nlos tres primeros: ", personas[:3])
    print("\nlos tres ultimos: ", personas[-3:])

def test_todos_entran_entre_anos(personas:list[Persona4]):
    ano1=2015
    ano2=2025
    print("\ntest_todos_entran_entre_anos")
    print("Entre {} y {},{}".format(ano1,ano2,todos_entran_entre_anos(personas,ano1,ano2)))
    ano2=2020
    print("Entre {} y {},{}".format(ano1,ano2,todos_entran_entre_anos(personas,ano1,ano2)))

def test_alguien_ha_madrugado(personas:list[Persona4]):
    hora=8
    print("\n test_alguien_ha_madragado")
    print("Antes de las {}:{}".format(hora,alguien_ha_madrugado(personas, hora)))

def test_persona_mas_alta(lista:list[Persona4])->tuple:
    print("la persona mas alta es:", persona_mas_alta(lista))

def test_relacion_alfabetica_de_personas(lista:list[Persona4])->list:
    print("lista ordenada de las personas:", relacion_alfabetica_de_personas(lista))

def test_n_personas_mayor_de_edad(lista:list[Persona4], n):
    print(f"{n}personas mayor de edads son:", n_personas_mayor_de_edad(lista, 10))

if __name__=='__main__':
    datos=lee_datos_personales("Proyectos Python\T09_datos_personales\data\datos_personales.csv")
    datos2=lee_datos_personales2("Proyectos Python\T09_datos_personales\data\datos_personales2.csv")
    datos3=lee_datos_personales3("Proyectos Python\T09_datos_personales\data\datos_personales3.csv")
    datos4=lee_datos_personales4("Proyectos Python\T09_datos_personales\data\datos_personales4.csv")
#    test_lee_datos_personales(datos)
#    test_lee_datos_personales2(datos2)
#    test_lee_datos_personales3(datos3)
#    test_lee_datos_personales4(datos4)
#    test_todos_entran_entre_anos(datos4)
#    test_alguien_ha_madrugado(datos4)
    test_persona_mas_alta(datos4)
    test_relacion_alfabetica_de_personas(datos4)
    test_n_personas_mayor_de_edad(datos4, 10)
