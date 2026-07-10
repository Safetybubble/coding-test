def solution(array, commands):
    answer = []
    for i,j,k in commands:
        soso = sorted(array[i-1:j])
        answer.append(soso[k-1])
    return answer