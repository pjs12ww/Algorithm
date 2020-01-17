# https://www.acmicpc.net/problem/17779
# date: 2020.01.17

from copy import deepcopy

# input
N = int(input())
mat = [list(map(int, input().split(' '))) for _ in range(N)]

result = 123456789
area = [0] * 5

# x, y, d1, d2 가 성립하는지 판정
def judge(x, y, d1, d2):
    if x + d1 + d2 >= N:
        return False
    if y - d1 < 0:
        return False
    if y + d2 >= N:
        return False
    return True

# 5번 선거구 라인 긋기
def draw_line(x, y, d1, d2):
    tmp_mat = [[0] * N for _ in range(N)]

    tmp_x_1 = x
    tmp_y_1 = y
    tmp_x_2 = x + d1 + d2
    tmp_y_2 = y + (d2 - d1)
    tmp_mat[tmp_y_2][tmp_x_2] = 5
    tmp_mat[tmp_y_1][tmp_x_1] = 5
    # 1, 3
    for i in range(d1):
        tmp_x_1 += 1
        tmp_y_1 -= 1
        tmp_x_2 -= 1
        tmp_y_2 += 1
        tmp_mat[tmp_y_2][tmp_x_2] = 5
        tmp_mat[tmp_y_1][tmp_x_1] = 5
    for i in range(d2):
        tmp_x_1 += 1
        tmp_y_1 += 1
        tmp_x_2 -= 1
        tmp_y_2 -= 1
        tmp_mat[tmp_y_2][tmp_x_2] = 5
        tmp_mat[tmp_y_1][tmp_x_1] = 5

    return tmp_mat

def fill(x, y, d1, d2, tmat):
    info = [(0, x + d1, 0, y - 1),
            (x + d1, N - 1, 0, y - d1 + d2),
            (0, x + d2 - 1, y, N - 1),
            (x + d1, N - 1, y - d1 + d2 + 1, N - 1)]

    for i in range(4):
        if i % 2:
            for j in range(info[i][2], info[i][3] + 1):
                for k in range(info[i][0], info[i][1] + 1):
                    if tmat[j][k] == 5:
                        break
                    else:
                        tmat[j][k] = i + 1
        else:
            for j in range(info[i][2], info[i][3] + 1):
                for k in range(info[i][1], info[i][0] - 1):
                    if tmat[j][k]== 5:
                        break
                    else:
                        tmat[j][k] = i + 1

    for a in range(N):
        for b in range(N):
            if tmat[a][b] == 0:
                tmat[a][b] = 5

    return tmat

def mmf(mmm):
    global result
    for i in range(4):
        cnt = 0
        for n in range(N):
            for m in range(N):
                if mmm[n][m] == i + 1:
                    cnt += 1
        area[i] += cnt
    ttt = max(area) - min(area)

    if ttt < result:
        result = ttt




arr = [[0] * N for _ in range(N)]
for y in range(1, N - 1):
    for x in range(N):
        for d1 in range(1, N - 1):
            for d2 in range(1, N - 1):
                if not judge(x, y, d1, d2):
                    break
                else:
                    ttmap = deepcopy(arr)
                    ttmap = fill(x, y, d1, d2, draw_line(x, y, d1, d2))
                    mmf(ttmap)

print(result)