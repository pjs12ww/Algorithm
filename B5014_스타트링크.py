# https://www.acmicpc.net/problem/5014
# date: 2020.01.19
# BFS

from collections import deque

F, S, G, U, D = map(int, input().split())
q = deque()
q.append((S, 0))
visited = []
ds = [U, -1 * D]

def BFS(q, visited):
    while q:
        s, cnt = q.popleft()

        if s in visited:
            continue
        if s > F or s < 1:
            continue

        visited.append(s)
        if s == G:
            return cnt
        cnt += 1
        for i in range(2):
            q.append((s + ds[i], cnt))

    return -1

ans = BFS(q, visited)

if ans == -1:
    print('use the stairs')
else:
    print(ans)
    print('test')


# F, S, G, U, D = map(int, input().split())
# ans = 1000001
# def DFS(s, visited, cnt):
#     global ans
#     if cnt > ans:
#         return
#     if s > F or s < 1 or s in visited:
#         return
#     if s == G:
#         ans = cnt
#         return
#     visited.append(s)
#     DFS(s + U, visited, cnt + 1)
#     DFS(s - D, visited, cnt + 1)
#
# DFS(S, [], 0)
# if ans == 1000001:
#     print('use the stairs')
# else:
#     print(ans)