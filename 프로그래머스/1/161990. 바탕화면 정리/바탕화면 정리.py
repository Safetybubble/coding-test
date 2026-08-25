def solution(wallpaper):
    check = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                check.append([i,j])
    pos = list(zip(*check))
    answer = ([min(pos[0],default = 0), min(pos[1],default = 0), max(pos[0],default = 0)+1, max(pos[1],default = 0)+1])      
    return answer