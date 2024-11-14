matriz = [
    [1,  2,  3,  4],
    [5,  7,  8,  9],
    [10, 11, 12, 3],
    [5,  8,  14, 22]
]

def verificar_matriz_cuadrada(matriz: list) -> bool:
    '''
    esta funcion verifica si una matriz es cuadrada.
    recibe la matriz y retorna verdadero o falso
    '''
    if not matriz:
        return False
    
    num_filas = len(matriz)
    num_columnas = len(matriz[0])
    
    for i in matriz:
        if num_filas != num_columnas:
            return False
    return True

# matriz_cuadrada = verificar_matriz_cuadrada(matriz)
# print(matriz_cuadrada)

# 2
def sumar_diagonales(matriz):
    '''
    esta funcion suma las diagonales ya sea la principal o secundaria
    recibe la matriz y retorna la suma de las diagonales
    '''
    suma_diagonal_principal = 0 
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if i == j:
                suma_diagonal_principal += matriz[i][j]
    suma_diagonal_secundaria = 0 
    n = len(matriz)
    for i in range(n):
        suma_diagonal_secundaria += matriz[i][n - 1 - i]
    return suma_diagonal_principal, suma_diagonal_secundaria

# 3
def transponer_matriz(matriz):
    '''
    eta funcion cambia las posiciones de las filas y las columnas de una matriz.
    recibe una matriz y retorna la transpuesta
    '''
    for i in range(len(matriz[0])):
        for j in range(len(matriz)):
            print(matriz[j][i], end=" ")
        print(" ")

