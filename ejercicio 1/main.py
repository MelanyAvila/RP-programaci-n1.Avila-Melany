from funciones.generales import *
from funciones.concretas import *

# Los puntos 2 y 3 deben utilizar la misma función (calcular_totales). La misma debe poder
# sumar por filas o por columnas. Además, deberán utilizar la función estimar_stock que recibe
# una lista de totales, una lista de strings con el nombre de cada total y reciba por parámetro
# cuál es el límite que debe tomar para informar.
# Realizar un menú de opciones:
depositos = ['tierra del fuego', 'tucumán', 'mendoza', 'bs as', 'misiones', 'santa fé']
camisetas = ['barcelona', 'inter miami', 'psg', 'manchester city', 'real madrid']

ejecutar = True
cargar = True # asi no se carga siempre

matriz = [[00, 0000, 300000, 299292, 100], [00, 222, 3334, 29922, 2222], 
          [000, 34, 111111, 55555, 33], [0, 2, 3334, 29922, 2222],
           [0, 33, 3332, 33332, 222122], [0, 33, 3332, 33332, 222122]]

while ejecutar == True:
    print('''\nMenú de opciones:
          1- obtener existencias.
          2- mostrar depósitos que tienen en stock más de 10k camisetas.
          3- mostrar equipos que hay en stock más de 5.000 camisetas.
          4- obtener máxima cantidad de camisetas de cada equipo y en que deposito estan.
        ''')
    
    opcion = input('ingrese la opción que desea realizar: ')

    match opcion:
        case '1':
            if cargar == False:
                matriz = inicializar_matriz(len(depositos, len(camisetas, 0)))  
                for i in range(len(depositos)):
                    for j in range(len(camisetas)):
                        cantidad = int(input(f'ingrese la cantidad de camisetas de {camisetas[j]} en {depositos[i]}: '))
                        matriz[i][j] = cantidad
                mostrar_matriz(matriz)
                cargar = True
            else:
                mostrar_matriz(matriz)
        case '2':
            mayor_stock = calcular_mayor_stock(matriz)
            depositos_10000 = []
            for i in range(len(mayor_stock)):
                if mayor_stock[i] > 10000:
                    depositos_10000 += [depositos[i]]
            print(f'depositos con más de 10k camisetas: {depositos_10000}... (son {len(depositos_10000)})')
        case '3':
            mayor_stockk = calcular_mayor_stock(matriz)
            equipos_5000 = [0] * len(matriz[0])
            for i in range(len(matriz)):
                for j in range(len(matriz[i])):
                    if matriz[i][j] > 5000:
                        equipos_5000[j] += 1
            print(f'los equipos con más de 5k camisetas: {equipos_5000}')
        case '4':
            for i in range(len(camisetas)):
                maximo = -1
                deposito_maximo = 0
                for j in range(len(depositos)):
                    if matriz[j][i] > maximo:
                        maximo = matriz[j][i]
                        deposito_maximo = depositos[j]
                print(f'el deposito con más camisetas de {camisetas[i]} es {deposito_maximo}')
        case '5':
            pass
        case '6':
            print('ejercicio terminado!!')
            ejecutar = False
            
# 5. Cargar ventas: se deberá poder cargar ventas de un determinado producto para un
# determinado depósito. 
#Esto es carga distribuida o aleatoria. 
#! Al cargarse las ventasse deben restar los productos vendidos del stock 
# y generar una matriz con la recaudación que reciba el listado de precios por parámetro, 
# en caso de no recibir un listado deberá tener un precio de 100 cada producto. Utilizar parámetro opcional.