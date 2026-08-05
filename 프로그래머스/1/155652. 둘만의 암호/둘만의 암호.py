def solution(s, skip, index):
    answer = ''
    count=0
    for i in s:
        check = i
        count = 0
        while count < index:
            check = chr((ord(check)-97+1)%26+97)
            if check not in skip:
                count+=1
        answer+=check
    return answer

