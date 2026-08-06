def solution(keymap, targets):
    answer = []
    total = []
    d_final = {}
    count=0
    for i in range(len(keymap)):
        idx = []
        for j in keymap[i]:
            idx.append(keymap[i].index(j)+1)
        total.append(dict(zip(keymap[i],idx)))
    for w in total:
            for e,r in w.items():
                if e not in d_final or r < d_final[e]:
                    d_final[e] = r
    print(d_final)
    for t in range(len(targets)):
        dddy = 0
        for y in targets[t]:
            if y not in d_final:
                dddy = -1
                break
            dddy+=d_final[y]
        answer.append(dddy)
    return answer