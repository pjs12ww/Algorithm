# https://www.acmicpc.net/problem/17143
# date: 2020.01.22

# 사람 이동
# 상어 이동
# 상어 정산

R, C, M = map(int, input().split())
# r, c, s 속도, d 방향, z 크기
# d: 1 => y -= 1, d: 2 => y += 1, d: 3 => x += 1, d: 4 => x -= 1
mat = [[(0, 0, 0)] * C for _ in range(R)]

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    mat[r - 1][c - 1] = (s, d, z)


def moveshark(r, c, s, d):
    print(r, c, s, d)
    if d == 1:
        tmp = s - r
        if tmp < 0:
            return r - s, c, s, d
        cnt_dis = tmp % (R - 1)
        dir = tmp // (R - 1)

        if dir % 2 == 0:
            return cnt_dis + 1, c, s, d + 1
        if dir % 2 == 1:
            return R - cnt_dis - 2, c, s, d

    if d == 2:
        tmp = s + r
        if tmp < R - 1:
            return tmp, c, s, d
        cnt_dis = tmp % (R - 1)
        dir = tmp // (R - 1)

        if dir % 2 == 0:
            return R - cnt_dis - 2, c, s, d - 1
        if dir % 2 == 1:
            return cnt_dis + 1, c, s, d
    if d == 3:
        print(1)
        tmp = s + c
        if tmp < C - 1:
            return r, tmp, s, d
        cnt_dis = tmp % (R - 1)
        dir = tmp // (R - 1)

        if dir % 2 == 0:
            return r, C - cnt_dis - 2, s, d + 1
        if dir % 2 == 1:
            return r, cnt_dis + 1, s, d
    if d == 4:
        tmp = s - c
        if tmp < 0:
            return r, c - s, s, d
        cnt_dis = tmp % (R - 1)
        dir = tmp // (R - 1)

        if dir % 2 == 0:
            return r, cnt_dis + 1, s, d - 1
        if dir % 2 == 1:
            return r, C - cnt_dis - 2, s, d

def delshark():
    pass


for i in range(C):
    king_idx = i
    mat_tmp = [[(0, 0, 0)] * C for _ in range(R)]
    for i in range(R):

        for j in range(C):
            tmp = mat[i][j]
            if tmp[1] != 0:
                print()
                print(i, j, tmp[0], tmp[1])
                print(moveshark(i, j, tmp[0], tmp[1]))
                if moveshark(i, j, tmp[0], tmp[1]):
                    tr, tc, ts, td = moveshark(i, j, tmp[0], tmp[1])
                    mat[tr][td] = (ts, td, tmp[2])
                    mat[i][j] = (0, 0, 0)

print(mat)
