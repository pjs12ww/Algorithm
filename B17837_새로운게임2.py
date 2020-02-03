# https://www.acmicpc.net/problem/15685
# date: 2020.02.03
# 시뮬레이션

# 결과 => 턴수 (불가능한(1000<ans) 경우 -1 출력)

from collections import deque

# 0 흰색, 1 빨강, 2 파랑
dy = (0, 0, -1, 1)
dx = (1, -1, 0, 0)

# init
N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
tmp_arr = [[[] for _ in range(N)] for _ in range(N)]

info = [[] for _ in range(N)]

for k in range(K):
    y, x, d = map(int, input().split())
    info[k] = [[y-1, x-1], [d-1]]
    tmp_arr[y-1][x-1].append(k)

print(info)
# for i in range(K):
#     y, x, d = map(int, input().split())
#     tmp_arr[y-1][x-1].append([i, d-1])

# 벽 판정, 파란색도 동일하게 취급
def is_wall(y, x):
    if 0 <= y < N and 0 <= x < N and arr[y][x] != 2:
        return True

# 종료조건
def end():
    for k in range(K - 1):
        if info[k][0] != info[k + 1][0]:
            return False
    return True

# 이동하기
# 해당 idx 위의 배열만 옮기기
def move(y, x, yy, xx, k, wr):
    print(tmp_arr)
    print(info)

    idx = tmp_arr[y][x].index(k)
    # print(tmp_arr[y][x][idx:])
    # print(idx)


    if wr == 0:
        tmp_arr[yy][xx] += tmp_arr[y][x][idx:]
        tmp_arr[y][x] = tmp_arr[y][x][0:idx]

    if wr == 1:
        # print(sorted(tmp_arr[y][x][idx:], reverse=True))
        # print(idx)
        tmp_arr[yy][xx] += sorted(tmp_arr[y][x][idx:], reverse=True)
        tmp_arr[y][x] = tmp_arr[y][x][0:idx]

# 흰색 일때
def white(y, x, k):
    d = info[k][1][0]
    # info[k][0][0], info[k][0][1] = y + dy[d], x + dx[d]
    yy, xx = y + dy[d], x + dx[d]
    move(y, x, yy, xx, k, 0)
    for kk in tmp_arr[yy][xx]:
        info[kk][0][0], info[kk][0][1] = yy, xx

def red(y, x, k):
    d = info[k][1][0]
    # info[k][0][0], info[k][0][1] = y + dy[d], x + dx[d]
    yy, xx = y + dy[d], x + dx[d]
    move(y, x, yy, xx, k, 1)
    for kk in tmp_arr[yy][xx]:
        info[kk][0][0], info[kk][0][1] = yy, xx

def blue(y, x, k):
    if info[k][1][0] % 2:
        d = info[k][1][0] - 1
        print(info[k][1][0])
        info[k][1][0] = d
        y, x = y + dy[d], x + dx[d]
    else:
        d = info[k][1][0] + 1
        print(info[k][1][0])
        info[k][1][0] = d
        y, x = y + dy[d], x + dx[d]
    # 오류나면 여기
    if is_wall(y + dy[d], x + dx[d]):
        info[k][0][0], info[k][0][1] = y + dy[d], x + dx[d]

def sol():
    for ans in range(1000):
        for i in range(len(info)):
            y, x = info[i][0][0] + dy[info[i][1][0]], info[i][0][1] + dx[info[i][1][0]]
            if not is_wall(y, x):
                blue(info[i][0][0], info[i][0][1], i)
            elif arr[y][x] == 0:
                white(info[i][0][0], info[i][0][1], i)
            elif arr[y][x] == 1:
                red(info[i][0][0], info[i][0][1], i)

        if end():
            return ans

    return -1

print(sol())