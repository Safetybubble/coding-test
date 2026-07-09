def solution(n, m):
    a,b = n,m
    while m>0:
        n,m = m, n%m
    return [n,a*b//n]