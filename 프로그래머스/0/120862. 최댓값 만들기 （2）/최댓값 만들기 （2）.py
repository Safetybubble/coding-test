def solution(numbers):
    answer = 0
    sn=sorted(numbers)
    if sn[-1]*sn[-2]>sn[0]*sn[1]:
        return sn[-1]*sn[-2]
    else:
        return sn[0]*sn[1]