def solution(citations):
    answer = 0
    check = []
    citations.sort(reverse = True)
    for i in range(len(citations)+1):
        Alex = 0
        for j in citations:
            if j>=i:
                Alex+=1
            else:
                break
        if Alex >= i:
            answer = i
    return answer