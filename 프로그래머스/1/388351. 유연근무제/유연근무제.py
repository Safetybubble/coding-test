def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):
        count_day = 0
        for j in range(len(timelogs[i])):
            time = schedules[i]
            if ((startday+j-1)%7+1) >= 6 or schedules[i]+10 >= timelogs[i][j]:
                count_day+=1
                continue
            if (((time // 100) * 60 + (time % 100) + 10) // 60) * 100 + ((time // 100) * 60 + (time % 100) + 10) % 60 < timelogs[i][j]:
                break
            count_day+=1
        if count_day==7:
            answer+=1
    return answer