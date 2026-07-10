def solution(arr):
    answer = [[]]
    if len(arr) > len(arr[0]): # 세로가 가로보다 크다면
        for i in range(len(arr)):
            while len(arr[i]) < len(arr): arr[i].append(0)
    elif len(arr) < len(arr[0]): # 가로가 세로보다 크다면
        while len(arr) != len(arr[0]):
            arr.append([0]*len(arr[0]))
    return arr