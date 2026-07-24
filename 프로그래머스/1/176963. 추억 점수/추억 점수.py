def solution(name, yearning, photo):
    answer = []
    D = dict(zip(name,yearning))
    for i in range(len(photo)):
        result = 0
        for j in photo[i]:
            if j in name:
                result+=D[j]
        answer.append(result)
    return answer