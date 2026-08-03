def solution(N, stages):
    answer = []
    people = len(stages)
    persent = []
    sty_p = [0]*(N+1)
    idx = [_ for _ in range(1,N+1)]
    for i in stages:
        sty_p[i-1] += 1
    sty_p = sty_p[:N]
    for j in sty_p:
        if people == 0:
            persent.append(0)
        else:
            persent.append(j / people)
        people -= j
    total = dict(zip(idx,persent))
    result = sorted(total, key=lambda x: total[x], reverse=True)
    return result