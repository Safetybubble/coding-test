def solution(lottos, win_nums):
    answer = []
    win_count=0
    cant_see = 0
    
    for i in lottos:
        if i in win_nums:
            win_count+=1
        elif i == 0:
            cant_see += 1
            
    High_rank = 7-(win_count+cant_see)
    Low_rank = 7-win_count
    
    if High_rank > 6:
        answer.append(6)
    else:
        answer.append(High_rank)
    if Low_rank > 6:
        answer.append(6)
    else:
        answer.append(Low_rank)
    
    return answer