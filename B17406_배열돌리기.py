# https://www.acmicpc.net/problem/6118
# date: 2020.01.15

from itertools import permutations
from copy import deepcopy

N, M, K = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
oper = []

for i in range(K):
    r, c, s = map(int, input().split())
    r, c = r-1, c-1 # 배열인덱스조절
    oper.append((r, c, s))

def rotation(center, s):
    global m
    r, c = center[0], center[1]

    for z in range(1, s + 1):
        tmp = m[r - z][c - z]
        for i in range(-z, z):
            m[r + i][c - z] = m[r + i + 1][c - z]

        for i in range(-z, z):
            m[r + z][c + i] = m[r + z][c + i + 1]

        for i in range(-z, z):
            m[r - i][c + z] = m[r - i - 1][c + z]

        for i in range(-z, z):
            m[r - z][c - i] = m[r - z][c - i - 1]

        m[r - z][c - z + 1] = tmp

def sums(mats):
    s = float('INF')
    for i in mats:
        if sum(i) < s:
            s = sum(i)
    return s

perm = list(permutations(oper, K))
ans = []
for p in perm:
    m = deepcopy(mat)

    for op in p:
        rotation((op[0],op[1]),op[2])
    ans.append(sums(mat))
print(min(ans))
