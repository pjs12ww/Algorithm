# https://www.acmicpc.net/problem/6118
# date: 2020.01.09
# 다익스트라
import heapq

N, M = map(int, input().split())
path = [[] for _ in range(N + 1)]
dist = [float("inf")] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    path[A].append(B)
    path[B].append(A)

pq = [(0, 1)]
dist[1] = dist[0] = 0

while pq:
    d, n = heapq.heappop(pq)
    for p in path[n]:
        if dist[p] > d + 1:
            dist[p] = d + 1
            heapq.heappush(pq, (d + 1, p))

max_dist = max(dist)
cnt = 0
ff = True

for i in range(1, N + 1):
    if max_dist == dist[i]:
        cnt += 1
        if ff:
            print(i, end=' ')
            ff = False

print(max_dist, cnt)