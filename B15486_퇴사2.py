# https://www.acmicpc.net/problem/15486
# date: 2020.01.01
# 완전탐색
N = int(input())
T = [0] * (N + 1)
P = [0] * (N + 1)
for n in range(N):
    T[n], P[n] = map(int, input().split())

dp = [0] * (N + 1)

for i in range(N - 1, -1, -1):
    tmp_T = T[i] + i
    if tmp_T <= N:
        if dp[tmp_T] + P[i] > dp[i + 1]:
            dp[i] = dp[tmp_T] + P[i]
            continue

    dp[i] = dp[i + 1]

print(dp[0])