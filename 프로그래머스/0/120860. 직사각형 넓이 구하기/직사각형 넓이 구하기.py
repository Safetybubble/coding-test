def solution(dots):
    answer = 0
    vertical = 0
    horizontal = 0
    point = dots[0]
    for i in range(1,len(dots)):
        if point[0] == dots[i][0]:
            vertical = abs(point[1]-dots[i][1])
        elif point[1] == dots[i][1]:
            horizontal = abs(point[0]-dots[i][0])
    return horizontal*vertical