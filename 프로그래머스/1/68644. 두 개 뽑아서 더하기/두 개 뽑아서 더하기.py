def solution(numbers):
    answer = []
    PA = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            PA.append(numbers[i]+numbers[j])
    return sorted(set(PA))