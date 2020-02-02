# https://www.acmicpc.net/problem/3055
# date: 2020.02.01
# BFS
from collections import deque

dy = (1, 0, -1, 0)
dx = (0, 1, 0, -1)

# Init
R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'D':
            D_idx = [i, j]
        if arr[i][j] == 'S':
            S_idx = [i, j]
queue = deque()
queue.append(S_idx + [1])
step = 0
visited = []


# arr 을 벗어나는 idx 찾는 함수
def in_arr(r, c):
    if 0 <= r < R and 0 <= c < C:
        return True

# 물이 찰 예정인 곳을 찾는 함수
def will_fill():
    for i in range(R):
        for j in range(C):
            if arr[i][j] == '*':
                for d in range(4):
                    dyy = i + dy[d]
                    dxx = j + dx[d]
                    if in_arr(dyy, dxx):
                        if arr[dyy][dxx] == '.' or arr[dyy][dxx] == 'S':
                            arr[dyy][dxx] = 'W'

# 물이 찰 예정인 곳을 물로 채우는 함수
def fill():
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'W':
                arr[i][j] = '*'

# BFS
def bfs():
    global step
    while queue:
        S_idx = queue.popleft()
        visited.append([S_idx[0], S_idx[1]])

        if step != S_idx[2]:
            fill()
            will_fill()
            step += 1
        for d in range(4):
            dyy = S_idx[0] + dy[d]
            dxx = S_idx[1] + dx[d]
            if [dyy, dxx] == D_idx:
                return step
            if in_arr(dyy, dxx):
                if arr[dyy][dxx] == '.' and [dyy, dxx] not in visited:
                    queue.append([dyy, dxx, step + 1])
    return 'KAKTUS'

print(bfs())