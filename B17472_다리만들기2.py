# https://www.acmicpc.net/problem/17472
# date: 2020.02.04
# ??

# 조건
# 1. 다리길이 2 이상

from collections import deque
import sys

# the setrecursionlimit function is
# used to modify the default recursion
# limit set by python. Using this,
# we can increase the recursion limit
# to satisfy our needs

sys.setrecursionlimit(10 ** 6)

# init
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dy, dx = (1, 0, -1, 0), (0, 1, 0, -1)
def in_arr(y, x):
    if 0 <= y < N and 0 <= x < M:
        return True
ans = 123456789
q = deque()
num = 2
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            visited = []
            q.append((i, j))
            while q:
                y, x = q.popleft()
                visited.append((y, x))
                arr[y][x] = num
                for d in range(4):
                    yy, xx = y + dy[d], x + dx[d]
                    if in_arr(yy, xx):
                        if arr[yy][xx] == 1 and (yy, xx) not in visited:
                            q.append((yy, xx))
            num += 1
num -= 2
memory = [[0] * num for _ in range(num)]
for y in range(N):
    flag = 0
    cnt = 0
    for x in range(M):
        if flag and not arr[y][x] and flag != arr[y][x]:
            cnt += 1
        elif flag and arr[y][x] and flag != arr[y][x]:
            if cnt > 1:
                if memory[flag-2][arr[y][x]-2] != 0 and memory[flag][arr[y][x]-2] > cnt:
                    memory[flag-2][arr[y][x]-2] = cnt
                    memory[arr[y][x]-2][flag-2] = cnt
                if memory[flag-2][arr[y][x]-2] == 0:
                    memory[flag-2][arr[y][x] - 2] = cnt
                    memory[arr[y][x] - 2][flag-2] = cnt
            flag = arr[y][x]
            cnt = 0
        if arr[y][x]:
            flag = arr[y][x]

for x in range(M):
    flag = 0
    cnt = 0
    for y in range(N):
        if flag and not arr[y][x] and flag != arr[y][x]:
            cnt += 1
        elif flag and arr[y][x] and flag != arr[y][x]:
            if cnt > 1:
                if memory[flag-2][arr[y][x]-2] != 0 and memory[flag-2][arr[y][x]-2] > cnt:
                    memory[flag-2][arr[y][x]-2] = cnt
                    memory[arr[y][x]-2][flag-2] = cnt
                if memory[flag-2][arr[y][x]-2] == 0:
                    memory[flag-2][arr[y][x] - 2] = cnt
                    memory[arr[y][x] - 2][flag-2] = cnt
            flag = arr[y][x]
            cnt = 0
        if arr[y][x]:
            flag = arr[y][x]
def finish(v):
    for i in range(len(v)):
        if v[i] == 0:
            return False
    return True

def dfs(a, length, v):

    # print(v)
    global ans
    if length > ans:
        return
    if finish(v):
        ans = length
        # print(ans)
        return
    for i in range(num):
        if memory[a][i] != 0:
            v[i] = 1
            dfs(i, length + memory[a][i], v)
            v[i] = 0
# print(memory)
def sol():
    global ans
    for n in range(num):
        sum_n = 0
        for nn in range(num):
            sum_n += memory[n][nn]
        if not sum_n:
            return -1

    for a in range(num):
        visited_d = [0] * num
        visited_d[a] = 1
        dfs(a, 0, visited_d)
    return ans
# print(memory)
print(sol())


