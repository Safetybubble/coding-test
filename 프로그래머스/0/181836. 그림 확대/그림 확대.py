def solution(picture, k):
    answer = []
    for i in range(len(picture)):
        doma=[]
        for j in range(len(picture[i])):
            doma.append(picture[i][j]*k)
        for p in range(k):
            answer.append("".join(doma))
    return answer