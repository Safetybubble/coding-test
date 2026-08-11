def solution(ingredient):
    burger_stack = []
    count = 0
    for i in ingredient:
        burger_stack.append(i)
        if burger_stack[-4:] == [1,2,3,1]:
            count+=1
            del burger_stack[-4:]
    return count