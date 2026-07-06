def solution(babbling):
    answer = 0
    can_say = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in can_say:
            i=i.replace(j,' ')
        if i.replace(' ', '') == '':
            answer += 1
    
    return answer