def solution(myString, pat):
    answer = 0
    for i in range(len(myString)):
        if myString.startswith(pat, i):
            answer+=1
    return answer