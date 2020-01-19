# https://www.acmicpc.net/problem/6118
# date: 2020.01.15
# BFS

from collections import deque

dx = (-1, 1, 0, 0, 0, 0)
dy = (0, 0, -1, 1, 0, 0)
dz = (0, 0, 0, 0, -1, 1)
m, n, h = map(int, input().split())
mat = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if mat[i][j][k] == 1:
                q.append((i, j, k))

def bfs():
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
                continue
            if mat[nx][ny][nz]:
                continue
            mat[nx][ny][nz] = mat[x][y][z] + 1
            q.append((nx, ny, nz))

def solve():
    bfs()
    ans = 0

    for i in range(h):
        for j in range(n):
            if 0 in mat[i][j]:
                return -1

            ans = max(ans, max(mat[i][j]))
    return ans - 1

print(solve())
