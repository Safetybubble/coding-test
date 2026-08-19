def solution(s):
    answer = []
    count_zero = 0
    count = 0
    while s!='1':
        check = ''
        for i in s:
            if i == '0':
                count_zero+=1
                continue
            check+=i
        s = bin(len(check))[2:]
        count+=1
    return [count, count_zero]