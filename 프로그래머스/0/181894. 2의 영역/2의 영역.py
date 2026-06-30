def solution(arr):
    answer = []
    start = 0
    end = 0
    if 2 not in arr:
        answer.append(-1)
        return answer
    else:
        for i in range(len(arr)):
            if arr[i] == 2:
                start = i
                break
        for j in range(len(arr)-1,0,-1):
            if arr[j] == 2:
                end = j
                break
    return arr[start:end+1]