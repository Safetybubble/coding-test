def solution(s):
    answer = ''
    check = [_ for _ in s]
    First = False
    for i in check:
        if i==' ':
            First = False
            answer+=i
            continue
        if i.isdigit():
            First = True
            answer+=i
            continue
        if First == True:
            answer+=i.lower()
        if First == False:
            answer+=i.upper()
            First = True
    return answer