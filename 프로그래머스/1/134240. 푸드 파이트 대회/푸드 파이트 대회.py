def solution(food):
    answer = ''
    q = []
    for i in range(1,len(food)):
        q.append([i]*(food[i]//2))
    q = sum(q,[])
    q+=[0]*food[0]+q[::-1]
    return ''.join(map(str, q))