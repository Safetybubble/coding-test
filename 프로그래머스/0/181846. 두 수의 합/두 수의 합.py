def solution(a, b):
    answer = []
    a_list = list(a)[::-1]
    b_list = list(b)[::-1]
    up = 0
    i=0
    while i<len(a_list) or i<len(b_list):
        a_value = int(a_list[i]) if i<len(a_list) else 0
        b_value = int(b_list[i]) if i<len(b_list) else 0
        answer.append(str((a_value+b_value+up)%10))
        up = (a_value+b_value+up)//10
        i+=1
    if up:
        answer.append(str(up))
    return "".join(answer[::-1])