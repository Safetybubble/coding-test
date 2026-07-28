def solution(progresses, speeds):
    answer = []
    Need_day = [(100 - progresses[i]+speeds[i]-1)//speeds[i] for i in range(len(progresses))]
    
    start = Need_day[0]
    complete = 0
    
    for j in range(len(Need_day)):
        if start >= Need_day[j]:
            complete+=1
        else:
            answer.append(complete)
            start = Need_day[j]
            complete=1
    answer.append(complete)
    
    return answer