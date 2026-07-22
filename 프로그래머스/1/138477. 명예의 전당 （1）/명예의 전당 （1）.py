def solution(k, score):
    answer = []
    box = []
    for i in score:
        if len(box)<k:
            box.append(i)
            answer.append(min(box))
            continue
        box.sort(reverse=True)
        if i>=max(box) or (min(box)<=i and max(box)>=i):
            box.insert(0,i)
            box.pop()
        answer.append(min(box))
        
    return answer