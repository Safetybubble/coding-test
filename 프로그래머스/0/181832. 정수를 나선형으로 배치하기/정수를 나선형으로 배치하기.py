def solution(n):
    arr = [[0]*n for _ in range(n)]
    move = {'right':(0,1), 'down':(1,0), 'left':(0,-1), 'up':(-1,0)}
    position = (0,0)
    curr_dir = 'right'
    for a in range(1,len(arr)*len(arr[0])+1):
        arr[position[0]][position[1]]=a
        if a == len(arr)*len(arr[0]):
            break
        j = move[curr_dir]
        Next = (position[0] + j[0], position[1] + j[1])
        if (Next[0]<0 or Next[0]>=len(arr) or Next[1]<0 or Next[1]>=len(arr)) or arr[Next[0]][Next[1]] != 0:
            if curr_dir == 'right':
                curr_dir = 'down'
            elif curr_dir == 'down':
                curr_dir = 'left'
            elif curr_dir == 'left':
                curr_dir = 'up'
            elif curr_dir == 'up':
                curr_dir = 'right'
            j = move[curr_dir]
            Next = (position[0] + j[0], position[1] + j[1])
        position = Next
    return arr