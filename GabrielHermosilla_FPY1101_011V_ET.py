import random
import os
import csv
opt = True
trabajadores = ["Juan Pérez" , "María García" , "Carlos López" , "Ana Martínez" , "Pedro Rodríguez" , "Laura Hernández" , "Miguel Sánchez" , "Isabel Gómez" , "Francisco Díaz" , "Elena Fernández"]
sueldos = []


def sueldos_aleatorios():
    sueldos = []
    for a in range(10):
        sueldos.append(random.randint(300000,2500000))
    return sueldos

def clasificar_sueldos(trabajadores,sueldos):
    if len(sueldos) == 0:
        os.system('cls')
        print("Debe ingresar sueldos alateorios antes de continuar.")
        volver()
    else:
     menor800 = []
     entre = []
     mayor2 = []
     for b in range(len(trabajadores)):
        if sueldos[b] < 800000:
             print(sueldos)
             menor800.append((trabajadores[b],sueldos[b]))
        elif sueldos[b] >= 800000 and sueldos[b] <=2000000:
            entre.append((trabajadores[b],sueldos[b]))
        elif sueldos[b] > 2000000:
            mayor2.append((trabajadores[b],sueldos[b]))
        else:
            print("no se registra ningun sueldo de estos parametros")

     print(f"\nSueldos menores a $800.000 TOTAL:{len(menor800)}")
     print(f"\n{'Nombre Empleado':<20}{'Sueldo':<10}") 
     for trabajador1, sueldo1 in menor800:
        print(f"{trabajador1:<20}${sueldo1:<10}")
     print(f"\nSueldos entre $800.000 y $2.000.000  TOTAL:{len(entre)}")
     print(f"\n{'Nombre Empleado':<20}{'Sueldo':<10}") 
     for trabajador2,sueldo2 in entre:
        print(f"{trabajador2:<20}${sueldo2:<10}")
     print(f"\nSueldos mayores a $2.000.000 TOTAL:{len(mayor2)}")
     print(f"\n{'Nombre Empleado':<20}{'Sueldo':<10}") 
     for trabajador3,sueldo3 in mayor2:
        print(f"{trabajador3:<20}${sueldo3:<10}\n")


def estadisticas():
    if len(sueldos) == 0:
        os.system('cls')
        print("Debe ingresar sueldos alateorios antes de continuar.")
        volver()
    else:   
     maximo = max(sueldos)
     minimo = min(sueldos)
     promedio = sum(sueldos)/len(sueldos)
     producto = 1
     for valor in sueldos:
        producto *= valor
     media_geometrica = producto**(1/(len(sueldos)))
     print(f"El sueldo maximo es de: ${maximo}")
     print(f"El sueldo minimo es de: ${minimo}")
     print(f"El promedio de sueldos es de: ${promedio}")
     print(f"La media geometrica de sueldos es de: ${media_geometrica}")
    

def reporte(trabajadores,sueldos):
    if len(sueldos) == 0:
        os.system('cls')
        print("Debe ingresar sueldos alateorios antes de continuar.")
        volver()
    else:
     dcto_salud = []
     dcto_afp = []
     sueldo_liquido = []
     for b in range(len(trabajadores)):
        dcto_salud.append(round((sueldos[b]*0.07),2))
        dcto_afp.append(round((sueldos[b]*0.12),2) )
     print(f"{'Nombre Empleado':<20}{'Sueldo Base':<15}{'Descuento salud':<20}{'Descuento AFP':<15}{'Sueldo Liquido':<15}")
     for d in range(len(trabajadores)):
        print(f"{trabajadores[d]:<20}{sueldos[d]:<15}")

     with open("sueldos.csv",'w',newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Nombre empleado","Sueldo Base","Descuento Salud","Descuento AFP","Sueldo Liquido"])
        for c in range(len(trabajadores)):
            escritor.writerow([trabajadores[c],sueldos[c]])
        print("Se ha registrado correctamente el archivo")   

def volver():
    flag = True
    while flag==True:
        print("ingrese (M) para volver al menu")
        m = input (": ").upper()
        if m == "M":
            flag = False
            os.system('cls')
        else:
            os.system('cls')
            print("ingrese la opción correcta.")
            flag = True
            

def salir():
    os.system('cls')
    print("Finalizando el programa...")
    print("Programa desarrollado por Gabriel Hermosilla")
    print("RUT 18.499.797-5")

def principal():
    print("Bienvenidos al programa de sueldos")
    print("-"*40)
    menu = ("1.Asignar sueldos alateorios","2.Clasificar sueldos","3.Ver estadisticas","4.Reporte de sueldos","5.Salir del programa")
    for a in menu:
        print(a)
    try:
        opciones = int(input("Ingrese su opción: "))
        return opciones
    except ValueError:
       print("Ingrese solo numeros.")

while opt == True:
     opciones = principal()
     if opciones ==1:
         sueldos = sueldos_aleatorios()
     elif opciones == 2:
         clasificar_sueldos(trabajadores,sueldos)
     elif opciones == 3:
         estadisticas()
     elif opciones == 4:
          reporte(trabajadores,sueldos)
     elif opciones == 5:
         salir()
         opt=False
     else:
         print("Ingrese la opción correcta.")

