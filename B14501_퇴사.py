# https://www.acmicpc.net/problem/14501
# date: 2020.01.01
# 완전탐색
N = int(input())
T = [0] * N
P = [0] * N
for n in range(N):
    T[n], P[n] = map(int, input().split())

result = 0

def Max_P(day, P_sum):
    global result
    if day >= N:
        if result < P_sum:
            result = P_sum
        return
    if day + T[day] <= N:
        Max_P(day + T[day], P_sum + P[day])
    if day + 1 <= N:
        Max_P(day + 1, P_sum)

Max_P(0, 0)
print(result)