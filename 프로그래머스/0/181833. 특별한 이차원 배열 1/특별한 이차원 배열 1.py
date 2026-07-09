def solution(n):
    answer = []
    for i in range(n):
        doma = []
        for j in range(n):
            if i==j: doma.append(1)
            else: doma.append(0)
        answer.append(doma)
    return answer