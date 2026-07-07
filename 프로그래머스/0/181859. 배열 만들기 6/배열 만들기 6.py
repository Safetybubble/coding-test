def solution(arr):
    answer = []
    for i in range(len(arr)):
        
        if len(answer)==0 or(len(answer)!=0 and answer[-1] != arr[i]):
            answer.append(arr[i])
        elif len(answer)!=0 and answer[-1] == arr[i]:
            answer.pop()
    if len(answer) == 0:
        answer.append(-1)
    return answer