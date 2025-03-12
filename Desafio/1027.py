def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high][0]  # Usando a coordenada x como pivô
    i = low - 1
    for j in range(low, high):
        if arr[j][0] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def max_points_on_wave(points):
    # Ordenar os pontos usando Quick Sort
    quick_sort(points, 0, len(points) - 1)

    # Inicializar contadores para os níveis superior e inferior
    t = [0] * len(points)
    b = [0] * len(points)

    # Contar os pontos
    for i in range(len(points)):
        t[i] = 1  # Inicializa o contador para o nível superior
        b[i] = 1  # Inicializa o contador para o nível inferior

    max_count = 1

    for i in range(1, len(points)):
        maxtop = 1
        maxbot = 1
        for j in range(i):
            if points[i][0] > points[j][0]:  # Verifica se x[i] > x[j]
                if points[i][1] == points[j][1] + 2:
                    maxtop = max(maxtop, b[j] + 1)
                elif points[i][1] == points[j][1] - 2:
                    maxbot = max(maxbot, t[j] + 1)

        t[i] = maxtop
        b[i] = maxbot
        max_count = max(max_count, t[i], b[i])

    return max_count

import sys

def main():
    results = []
    try:
        while True:
            line = input().strip()
            if not line:  # Ignora linhas em branco
                continue
            n = int(line)
            points = []
            for _ in range(n):
                point_line = input().strip()
                if point_line:  # Verifica se a linha não está vazia
                    x, y = map(int, point_line.split())
                    points.append((x, y))
            results.append(max_points_on_wave(points))
    except EOFError:
        pass  # Finaliza a leitura ao atingir o final do arquivo
    except ValueError:
        return  # Se houver erro de entrada, simplesmente retorna sem imprimir nada

    for result in results:
        print(result)

if __name__ == "__main__":
    main()