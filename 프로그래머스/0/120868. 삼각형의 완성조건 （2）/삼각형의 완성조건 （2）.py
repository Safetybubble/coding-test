def solution(sides):
    return len([i for i in range(max(sides[0],sides[1])-min(sides[0],sides[1])+1,sides[0]+sides[1])])