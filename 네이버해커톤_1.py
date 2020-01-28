from itertools import combinations

def solution(A):
    length = len(A)
    ans = 0
    arr = []
    for i in range(length):
        arr.append(i)
    per = []
    for i in range(length-1, -1, -1):
        per += list(combinations(arr, i))

    for a in per:
        tmp = ''
        for b in a:
            tmp += A[b]
        for c in tmp:
            cnt = 0
            flag = 0
            for d in tmp:
                if c == d:
                    cnt += 1
                if cnt > 1:
                    flag = 1
                    break
            if flag == 1:
                break
        if flag == 0:
            return len(tmp)
    return len(tmp)


