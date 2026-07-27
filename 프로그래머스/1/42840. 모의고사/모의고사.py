def solution(answers):
    answer = []
    number1 = [1,2,3,4,5]
    number2 = [2,1,2,3,2,4,2,5]
    number3 = [3,3,1,1,2,2,4,4,5,5]
    total_point = [0,0,0]
    for i in range(len(answers)):
        if answers[i] == number1[i%(len(number1))]:
            total_point[0]+=1
        if answers[i] == number2[i%(len(number2))]:
            total_point[1]+=1
        if answers[i] == number3[i%(len(number3))]:
            total_point[2]+=1
    M = max(total_point)
    for j,k in enumerate(total_point):
        if k == M:
            answer.append(j+1)
        
    return answer