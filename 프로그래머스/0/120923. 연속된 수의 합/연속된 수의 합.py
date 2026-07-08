def solution(num, total):
    answer = []
    result_half = total//num
    answer.append(result_half)
    for i in range(1,num):
        if i%2==1:
            answer.append(result_half+(i+1)//2)
        elif i%2==0:
            answer.insert(0,result_half-i//2)
    return answer