def solution(myString, pat):
    answer=myString.rindex(pat)
    return myString[:answer+len(pat)]