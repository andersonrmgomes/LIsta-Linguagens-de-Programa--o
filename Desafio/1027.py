import sys

def max_subsequencia(pontos):
    # Ordena os pontos por coordenada x
    pontos.sort(key=lambda x: x[0])
    
    # Inicializa a tabela de programação dinâmica
    N = len(pontos)
    DP = [[1, 1] for _ in range(N)]
    
    resposta = 1
    
    for i in range(1, N):
        for j in range(i):
            if pontos[i][0] == pontos[j][0]:
                break
            if pontos[i][1] - pontos[j][1] == 2:
                # Descendo, acrescentando mais um no caso em que j está acima
                DP[i][1] = max(DP[i][1], DP[j][0] + 1)
            elif pontos[i][1] - pontos[j][1] == -2:
                # Subindo, acrescentando mais um no caso em que j está abaixo
                DP[i][0] = max(DP[i][0], DP[j][1] + 1)
        resposta = max(resposta, max(DP[i][0], DP[i][1]))
    
    return resposta

# Leitura dos dados
while True:
    try:
        N = int(input())
        pontos = []
        for _ in range(N):
            x, y = map(int, input().split())
            pontos.append((x, y))
        
        print(max_subsequencia(pontos))
    except EOFError:
        break
    