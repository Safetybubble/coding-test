def solution(strArr):
    check_len = [0]*31
    answer = 0
    for i in range(len(strArr)):
        check_len[len(strArr[i])]+=1
    return max(check_len)