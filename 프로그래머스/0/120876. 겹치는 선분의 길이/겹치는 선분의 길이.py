def solution(lines):
    AP = []
    for i in lines:
        lines_x = i[0]
        lines_y = i[1]
        AP.append((i[0],1))
        AP.append((i[1],-1))
        
    AP.sort()
    
    total_events = 0
    before_length = 0
    dp_lines_length = 0
    
    for position,event in AP:
        if total_events>=2:
            dp_lines_length += (position-before_length)
        total_events+=event
        before_length = position
    return dp_lines_length
        