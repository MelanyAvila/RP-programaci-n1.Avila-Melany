def inicializar_matriz(filas: int, columnas: int, valor_inicial: any = 0) -> list:
    '''
    inicializa una matriz de un tamaño especifico, inicializando todos los elementos con un valor dado.
    recibe el valor inicial, y los numeros de filas y columnas.
    retorna una lista de listas
    '''
    matriz = []
    for _ in range(filas):
        fila = [valor_inicial] * columnas
        matriz += [fila]
    return matriz

def apend(lista: list, elemento: any) -> list:
    '''
    esta funcion crea una nueva lista (con todos los elementos de la lista original) y añade un elemento
    recibe como parametros la lista a la que se le quiere agregar un elemento y el elemento.
    retorna la nueva lista
    '''
    nueva_lista = [0] * (len(lista) + 1)

    for i in range(len(lista)):
        nueva_lista[i] = lista[i]

    nueva_lista[-1] = elemento
    return nueva_lista

def mostrar_matriz(matriz: list) -> list:
    '''
    imprime matrices de la manera correcta.
    recibe una lista de listas.
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=' ')
        print('')
