# https://www.acmicpc.net/problem/17143
# date: 2020.02.02

# from copy import deepcopy
dy = (1, 0, -1, 0)
dx = (0, -1, 0, 1)

# 배열 돌리기
# 시계방향
dy_a = (1, 0, -1, 0)
dx_a = (0, 1, 0, -1)
# 반시계방향
dy_r = (-1, 0, 1, 0)
dx_r = (0, 1, 0, -1)

# init
R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
fresher = []
ans = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] == -1:
            fresher.append((i, j))

# 퍼질 수 있는 좌표가 몇개 있는지
def can_s(y, x, div_n):
    sub_n = 0
    tmp = []
    for d in range(4):
        dyy, dxx = y + dy[d], x + dx[d]
        if in_arr(dyy, dxx):
            sub_n -= div_n
            tmp.append((dyy, dxx))
    return sub_n, tmp

# 벗어나는지
def in_arr(y, x):
    if 0 <= y < R and 0 <= x < C:
        if arr[y][x] != -1:
            return True

# 확산
def spread():
    tmp_arr = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if arr[r][c] != 0 and arr[r][c] != -1:
                div_n = int(arr[r][c] / 5)   # 확산양
                sub_n, tmp_idx = can_s(r, c, div_n)
                tmp_arr[r][c] += sub_n
                for idx in tmp_idx:
                    tmp_arr[idx[0]][idx[1]] += div_n

    for r in range(R):
        for c in range(C):
            arr[r][c] += tmp_arr[r][c]


# 공기청정기
def push_air():
    for i in range(2):
        if i == 0:
            d = 0
            end_point = fresher[i][0]
            arr[fresher[i][0] - 1][fresher[i][1]] = 0
            y, x = fresher[i][0] - 1, fresher[i][1]
            while 1:
                dyy, dxx = y + dy_r[d], x + dx_r[d]
                if not in_arr(dyy, dxx) or dyy > end_point:
                    d += 1
                    # 종료 조건
                    if d == 4:
                        arr[y][x] = 0
                        break
                    dyy, dxx = y + dy_r[d], x + dx_r[d]
                arr[y][x] = arr[dyy][dxx]
                y, x = dyy, dxx

        if i == 1:
            d = 0
            end_point = fresher[i][0]
            arr[fresher[i][0] + 1][fresher[i][1]] = 0
            y, x = fresher[i][0] + 1, fresher[i][1]
            while 1:
                dyy, dxx = y + dy_a[d], x + dx_a[d]
                if not in_arr(dyy, dxx) or dyy < end_point:
                    d += 1
                    # 종료 조건
                    if d == 4:
                        arr[y][x] = 0
                        break
                    dyy, dxx = y + dy_a[d], x + dx_a[d]

                arr[y][x] = arr[dyy][dxx]
                y, x = dyy, dxx

# solve
for _ in range(T):
    spread()
    push_air()

for r in range(R):
    for c in range(C):
        if arr[r][c] != -1:
            ans += arr[r][c]
print(ans)