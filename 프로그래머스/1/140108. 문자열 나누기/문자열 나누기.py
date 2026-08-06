def solution(s):
    answer = 0
    same = 0
    not_same = 0
    x = s[0]
    for i in range(len(s)):
        if same == 0 and not_same == 0:
            x = s[i]
        if s[i] == x:
            same +=1
        else:
            not_same +=1
        if same == not_same or i == len(s)-1:
            answer+=1
            same = 0
            not_same = 0
        print(x, same, not_same, answer)
    return answer