def solution(rank, attendance):
    result=[]
    for i in range(len(attendance)):
        if attendance[i]: result.append(rank[i])
    result = sorted(result)
    return 10000*rank.index(result[0])+100*rank.index(result[1])+rank.index(result[2])