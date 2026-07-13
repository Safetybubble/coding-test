def solution(participant, completion):
    answer=''
    check=dict()
    for i in participant:
        if i in check:
            check[i]+=1
        else:
            check[i]=1
    for j in completion:
        if j in check:
            check[j]-=1
    
    return ''.join([i for i in check if check[i]!=0])