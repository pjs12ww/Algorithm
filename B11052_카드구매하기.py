# https://www.acmicpc.net/problem/11052
# date: 2020.01.06

# 완전탐색 => 최대값 찾기 => 시간 초과
# N = int(input())
# P = list(map(int, input().split()))
# P.insert(0, 0)
# result = 0
#
# def DFS(n, cost):
#     global result
#     if n > N:
#         return
#     if n == N:
#         if cost > result:
#             result = cost
#         return
#     for i in range(1, N + 1):
#         DFS(n + i, cost + P[i])
#
# for i in range(1, N + 1):
#     DFS(i, P[i])
# print(result)

# DP
N = int(input())
P = list(map(int, input().split()))
P.insert(0, 0)
dp = [0] * (N + 1)
for i in range(1, N + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - j] + P[j])

print(dp[N])

