def solution(arr):
    answer = []
    n=1
    if (len(arr)&(len(arr)-1)) == 0:
        return arr
    else:
        while 1:
            if 2**n<len(arr) and len(arr)<2**(n+1):
                for i in range(2**(n+1)-len(arr)):
                    arr.append(0)
                break
            n+=1
    return arr