def solution(my_string):
    answer=0
    a = "".join([i if i.isdigit() else ' 'for i in my_string])
    return sum(map(int, a.split()))