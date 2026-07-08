def solution(A, B):
    check = list(A)
    if A == B: return 0
    for i in range(1,len(A)+1):
        check.insert(0,check[-1])
        check.pop()
        if "".join(check) == B: return i
    return -1