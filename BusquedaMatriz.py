# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    # Recorremos las filas y columnas de la matriz
    for i in range(len(matriz)):  # Recorre las filas
        for j in range(len(matriz[i])):  # Recorre las columnas
            if matriz[i][j] == valor:  # Si encontramos el valor
                return (i, j)  # Retornamos la posición (i, j) de la matriz
    return None  # Si no encontramos el valor, retornamos None

# Matriz de ejemplo 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Valor que queremos buscar en la matriz
valor_a_buscar = 10

# Llamamos a la función de búsqueda
resultado = buscar_valor(matriz, valor_a_buscar)

# Mostramos el resultado
if resultado:
    print(f"El valor {valor_a_buscar} se encontró en la posición: {resultado}")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")
