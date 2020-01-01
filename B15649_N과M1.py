# https://www.acmicpc.net/problem/15649
# date: 2020.01.01
# 순열 문제
# 재귀를 활용한 풀이

N, M = map(int, input().split())
result = [0] * M
picked = [0] * N

# M depth 의 재귀 필요
def make_seq(depth):
    if depth == M + 1:
        print(' '.join(result))
        return

    else:
        for i in range(N):
            if picked[i] == 0:
                result[depth - 1] = str(i + 1)
                picked[i] = 1
                make_seq(depth + 1)
                picked[i] = 0

make_seq(1)

# # 라이브러리를 활용한 풀이
# from itertools import permutations
#
# N, M = map(int, input().split())
#
# arr = [i for i in range(1, N + 1)]
#
# result = list(permutations(arr, M))
# for i in range(len(result)):
#     for j in range(M):
#         print(result[i][j], end=' ')
#     print()