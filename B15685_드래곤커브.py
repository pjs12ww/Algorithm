# https://www.acmicpc.net/problem/15685
# date: 2020.01.11
# 시뮬레이션

N = int(input())
arr = [[0] * 101 for _ in range(101)]
dy = (0, -1, 0, 1)
dx = (1, 0, -1, 0)

cnt = 0

for _ in range(N):
    x, y, d, g = map(int, input().split())

    curve_info=[d]
    for _ in range(g):
        curve_info += [(i+1) % 4 for i in curve_info[::-1]]
    arr[y][x] = 1
    nx = x
    ny = y

    for curve in curve_info:
        ny = ny + dy[curve]
        nx = nx + dx[curve]
        arr[ny][nx] = 1

for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
            cnt += 1

print(cnt)