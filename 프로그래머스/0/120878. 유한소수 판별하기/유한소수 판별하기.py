def solution(a, b):
    Query = []
    n = 2
    for i in range(min(a,b),0,-1):
        if a%i==0 and b%i==0:
            a//=i
            b//=i
            
    while n*n<=b:
        while b%n==0:
            Query.append(n)
            b//=n
        n+=1
        
    if b>1:
        Query.append(b)
    
    while 2 in Query:
        Query.remove(2)
    while 5 in Query:
        Query.remove(5)
    
    if len(Query) == 0:
        return 1
    return 2
    
