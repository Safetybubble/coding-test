def solution(n):
    a=[]
    result=0
    while n>0:
        a.append(n%3)
        n//=3
    for i in range(len(a)):
        result+=a[-1-i]*3**i
    return result