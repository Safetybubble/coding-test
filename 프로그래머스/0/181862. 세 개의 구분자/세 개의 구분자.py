def solution(myStr):
    answer = myStr.replace('a',' ').replace('b',' ').replace('c',' ').split()
    if len(answer) == 0:
        answer.append("EMPTY")
    return answer