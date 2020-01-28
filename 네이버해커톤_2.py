# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
def solution(S):
    length = len(S)
    S_arr = list(S)
    for i in range(length//2):
        flag = 0
        if S_arr[i] == S_arr[length-i-1]:
            flag = 1
        if S_arr[i] == '?' and S_arr[length - i - 1] == '?':
            S_arr[i] = S_arr[length - i - 1] = 'a'
            flag = 1
        if S_arr[i] == '?':
            S_arr[i] = S_arr[length-i-1]
            flag = 1
        if S_arr[length-i-1] == '?':
            S_arr[length - i - 1] = S_arr[i]
            flag = 1
        if flag == 0:
            return 'NO'
    S = ''.join(S_arr)
    return S



