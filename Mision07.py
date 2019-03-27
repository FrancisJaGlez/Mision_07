#FRANCISCO JAVIER GONZALEZ MOLINA A01748636
#Mision 07

def dividir (dividendo,divisor): #Calcula las divisiones
    a= dividendo
    b= divisor
    cociente=0
    while dividendo >= divisor:
        dividendo= dividendo-divisor
        cociente+=1


    return print(a ,"\\", b ," = ",cociente,", sobra ", dividendo)

def encontrarMayor ():  #calcula el numero mayor que el usuario introduce
    numeros = int(input("Teclea un numero [-1 para salir]: "))
    if numeros != -1:
        valorMayor = 0
        while numeros != -1:
            if numeros >= valorMayor:
                valorMayor= numeros
            numeros = int(input("Teclea un numero [-1 para salir]: "))
        print ("El mayor es: ",valorMayor)
    else:
        print ("No hay valor mayor")


def main():      #llama la funcion que escoja el usuario
    accion= int(input("""
--------------------------------------------------
    Mision. 07: Ciclos While
    Autor: Francisco Javier González Molina
    Matrícula: A01748636
    1.- Calcular divisiones
    2.- Encontrar el mayor
    3.- Salir
--------------------------------------------------
    Teclea tu opción: """))
    while accion != 3:
        if accion == 1:
            print("Calculando Divisores")
            dividendo= int (input("Dividendo: "))
            divisor= int (input("Divisor: "))
            dividir(dividendo,divisor)
            accion = int(input("""
--------------------------------------------------
    Mision. 07: Ciclos While
    Autor: Francisco Javier González Molina
    Matrícula: A01748636
    1.- Calcular divisiones
    2.- Encontrar el mayor
    3.- Salir
--------------------------------------------------
    Teclea tu opción: """))
        elif accion == 2:
            print("Calculando Mayor")
            encontrarMayor()
            accion = int(input("""
--------------------------------------------------
    Mision. 07: Ciclos While
    Autor: Francisco Javier González Molina
    Matrícula: A01748636
    1.- Calcular divisiones
    2.- Encontrar el mayor
    3.- Salir
--------------------------------------------------
    Teclea tu opción: """))
        else:
            print("ERROR, Teclea 1, 2 o 3")
            accion = int(input("""
--------------------------------------------------
    Mision. 07: Ciclos While
    Autor: Francisco Javier González Molina
    Matrícula: A01748636
    1.- Calcular divisiones
    2.- Encontrar el mayor
    3.- Salir
--------------------------------------------------
    Teclea tu opción: """))
    print("¡Gracias por usar este programa! Vuelve pronto :C")

main()    #ejecuta el programa