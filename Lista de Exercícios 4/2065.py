import heapq

n, m = map(int, input().split())
v = list(map(int, input().split()))
c = list(map(int, input().split()))

# Heap que armazena tuplas: (tempo_total, indice_funcionario)
# Começa com todos os tempos zerados
heap = [(0, i) for i in range(n)]
heapq.heapify(heap)

# Vetor que acumula a carga de trabalho de cada funcionário
vt = [0] * n

for i in range(m):
    tempo, idx = heapq.heappop(heap)  # Pega funcionário com menor carga
    carga = v[idx] * c[i]
    vt[idx] += carga
    heapq.heappush(heap, (vt[idx], idx))  # Atualiza heap com nova carga

print(max(vt))
