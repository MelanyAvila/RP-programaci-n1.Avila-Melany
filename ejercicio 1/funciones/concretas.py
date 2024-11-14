from funciones.generales import *

# 2
def calcular_mayor_stock(matriz: list) -> list:
    '''
    esta funcion calcula los totales almacenando la suma de cada fila.
    recibe una lista de listas y retorna una lista con la suma de los elementos.
    '''
    mayor_stock = [0] * len(matriz)

    for i in range(len(matriz)):
        acumulador = 0
        for j in range(len(matriz[i])):
            acumulador += matriz[i][j]

        mayor_stock[i] = acumulador
    return mayor_stock

# # 5
# def cargar_ventas(matriz_stock: list, filas: int, columnas: int):
#     ventas = inicializar_matriz(filas, columnas, 0)
#     for i in range(filas):
#         for J in range(columnas):