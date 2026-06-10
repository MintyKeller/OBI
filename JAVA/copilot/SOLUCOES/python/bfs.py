# Solução: BFS - Busca em Largura

from collections import deque

n, m = map(int, input().split())
labirinto = []

for _ in range(n):
    linha = input().split()
    labirinto.append(linha)

coordenadas = list(map(int, input().split()))
start_x, start_y, end_x, end_y = coordenadas

# BFS
fila = deque([(start_x, start_y, 0)])  # (x, y, distancia)
visitado = set()
visitado.add((start_x, start_y))

direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # direita, esquerda, baixo, cima

while fila:
    x, y, dist = fila.popleft()
    
    if x == end_x and y == end_y:
        print(dist)
        break
    
    for dx, dy in direcoes:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visitado and labirinto[nx][ny] == '.':
            visitado.add((nx, ny))
            fila.append((nx, ny, dist + 1))
else:
    print(-1)
