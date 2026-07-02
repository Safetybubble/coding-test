def solution(board):
    answer = 0
    move = {'up':(0,1),'down':(0,-1),'left':(1,0),'right':(-1,0),'upleft':(-1,1), 'upright':(1,1), 'downleft':(-1,-1), 'downright':(1,-1)}
    bomb_position = []
    peaceful_position = 0
    for i in range(len(board)): # 폭탄 위치 찾기
        for j in range(len(board[0])):
            if board[i][j] == 1:
                bomb_position.append((i,j))
    
    for L,R in bomb_position: # 폭탄 주변 위치 위험지역으로 만들기
        for q,c in move.values():
            danger_x = L+q
            danger_y = R+c
            
            # 위험구역 지정중 칸 바깥에 나가지 않도록 제한
            if 0<=danger_x<len(board) and 0<=danger_y<len(board[0]): 
                board[danger_x][danger_y] = 1
                
    for w in board: # 안전 구역 갯수 세기
        peaceful_position += w.count(0)
        
    return peaceful_position