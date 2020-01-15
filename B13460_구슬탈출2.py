# https://www.acmicpc.net/problem/13460
# date: 2020.01.12
# BFS /// 다른 풀이 : Brute

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
cnt = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            R_q = [(i, j, 0)]
            visited = [(i, j)]
        if arr[i][j] == 'B':
            B_q = [(i, j)]
        if arr[i][j] == 'O':
            O = (i, j)

while R_q:

    R = R_q.pop(0)
    B = B_q.pop(0)

    r_flag = 0

    if R[2] > 10:
        r_flag = -1
        break

    for i in range(4):
        flag = 1
        Ry_tmp, Rx_tmp = R[0], R[1]
        By_tmp, Bx_tmp = B[0], B[1]

        while arr[Ry_tmp + dy[i]][Rx_tmp + dx[i]] != '#':

            Ry_tmp, Rx_tmp = Ry_tmp + dy[i], Rx_tmp + dx[i]

            if arr[Ry_tmp][Rx_tmp] == 'O':
                r_flag = 1
                break

        while arr[By_tmp + dy[i]][Bx_tmp + dx[i]] != '#':
            By_tmp, Bx_tmp = By_tmp + dy[i], Bx_tmp + dx[i]
            if arr[By_tmp][Bx_tmp] == 'O':
                r_flag = 3
                break

        if r_flag == 1:
            cnt = R[2] + 1
            break

        if Ry_tmp == By_tmp and Rx_tmp == Bx_tmp:
            if i == 0:
                if R[1] > B[1]:
                    Bx_tmp -= 1
                else:
                    Rx_tmp -= 1
            elif i == 1:
                if R[0] > B[0]:
                    Ry_tmp += 1
                else:
                    By_tmp += 1
            elif i == 2:
                if R[1] > B[1]:
                    Rx_tmp += 1
                else:
                    Bx_tmp += 1
            else:
                if R[0] > B[0]:
                    By_tmp -= 1
                else:
                    Ry_tmp -= 1

        if (Ry_tmp, Rx_tmp) not in visited and r_flag == 0:
            depth = R[2] + 1
            visited.append((Ry_tmp, Rx_tmp))
            R_q.append((Ry_tmp, Rx_tmp, depth))
            B_q.append((By_tmp, Bx_tmp))
    if r_flag == 1:
        break

# print(visited)
if r_flag == 1:
    print(cnt)
else:
    print(-1)