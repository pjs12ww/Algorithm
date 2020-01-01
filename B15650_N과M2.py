# https://www.acmicpc.net/problem/15650
# date: 2020.01.01
# 조합 문제
# 재귀를 활용한 풀이

N, M = map(int, input().split())
result = [0] * M
picked = [0] * N

# M depth 의 재귀 필요
def make_seq(ind, depth):
    if depth == M + 1:
        print(' '.join(result))
        return

    else:
        for i in range(ind, N):
            if picked[i] == 0:
                result[depth - 1] = str(i + 1)
                picked[i] = 1
                make_seq(i, depth + 1)
                picked[i] = 0

make_seq(0, 1)

# # 라이브러리를 활용한 풀이
# from itertools import combinations
#
# N, M = map(int, input().split())
#
# arr = [i for i in range(1, N + 1)]
#
# result = list(combinations(arr, M))
# for i in range(len(result)):
#     for j in range(M):
#         print(result[i][j], end=' ')
#     print()


