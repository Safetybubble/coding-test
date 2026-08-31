def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    h,m = pos.split(':')
    pos_time = int(h)*60 + int(m)
    
    opstart_h ,opstart_m = op_start.split(':')
    opstart_time = int(opstart_h)*60 + int(opstart_m)
    
    opend_h , opend_m = op_end.split(':')
    opend_time = int(opend_h)*60 + int(opend_m)
    
    video_h , video_m = video_len.split(':')
    video_time = int(video_h)*60 + int(video_m)
    
    if pos_time >=opstart_time and pos_time <= opend_time:
        pos_time = opend_time
        
    for i in commands:
        if i == 'next':
            pos_time+=10
            if pos_time >= video_time:
                pos_time = video_time
        elif (i == "prev") and pos_time < 10:
            pos_time = 0
        else:
            pos_time-=10
            if pos_time<=0:
                pos_time = 0
        if pos_time>=opstart_time and pos_time<=opend_time:
            pos_time = opend_time
    
            
    result_h , result_m = str(pos_time//60) , str(pos_time%60) 
    
    if len(result_h) < 2:
        result_h = '0'+str(result_h)
    if len(result_m) < 2:
        result_m = '0'+str(result_m)
        
    return (f"{result_h}:{result_m}")