# https://www.acmicpc.net/problem/6118
# date: 2020.01.09
# BFS
from collections import deque

N, M = map(int, input().split())
farm = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    farm[A][B] = 1
    farm[B][A] = 1
visited = [0] * (N + 1)


# 검증
# for i in range(N + 1):
#     print(farm[i])