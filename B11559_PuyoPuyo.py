# https://www.acmicpc.net/problem/11559
# date: 2020.02.01
# BFS
from collections import deque
from copy import deepcopy

dy = (0, -1, 0, 1)
dx = (1, 0, -1, 0)

# init (R: 12, C: 6)
R = 12
C = 6
arr = [list(input()) for _ in range(R)]
q = deque()
ans = 0

# 벗어나지 않게
def in_arr(y, x):
    if 0 <= y < 12 and 0 <= x < 6:
        return True

# bfs
def bfs(c, y, x):
    global ans
    v = []
    q.append([y, x])
    tmp_q = [[y, x]]
    while q:
        idx = q.popleft()
        v.append(idx)
        for d in range(4):
            dyy = idx[0] + dy[d]
            dxx = idx[1] + dx[d]
            if in_arr(dyy, dxx):
                if arr[dyy][dxx] == c and [dyy, dxx] not in v:
                    q.append([dyy, dxx])
                    tmp_q.append([dyy, dxx])


    if len(tmp_q) >= 4:
        for i in tmp_q:
            arr[i[0]][i[1]] = '.'

# 한번에 몇개 씩 연결되어 있는지
def bomb():
    for i in range(R - 1, -1, -1):
        for j in range(C):
            if (arr[i][j] == 'R'):
                bfs('R', i, j)
            if (arr[i][j] == 'G'):
                bfs('G', i, j)
            if (arr[i][j] == 'B'):
                bfs('B', i, j)
            if (arr[i][j] == 'Y'):
                bfs('Y', i, j)
            if (arr[i][j] == 'P'):
                bfs('P', i, j)

# 터진 후 빈공간 채우기
def grav():
    # flag 가 0 일 때, 아직 최하단 빈공간을 못 찾았을 때
    # flag 가 1 일 때, 최하단 빈공간을 가지고 있을 때
    for c in range(C):
        flag = 0
        for r in range(R - 1, -1, -1):
            if arr[r][c] == '.':
                if flag == 0:
                    hole = [r, c]
                    flag = 1
            if arr[r][c] != '.':
                if flag == 1:
                    arr[hole[0]][hole[1]] = arr[r][c]
                    arr[r][c] = '.'
                    hole[0] -= 1

f = 1
# 시뮬레이션
while f:
    tmp = deepcopy(arr)
    bomb()
    grav()
    if tmp == arr:
        f = 0
    else:
        ans += 1

print(ans)