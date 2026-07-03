def solution(spell, dic):
    answer = 0
    for i in range(len(dic)):
        count=0
        for j in range(len(spell)):
            if spell[j] in dic[i]:
                count+=1
                if count==len(spell):
                    return 1
    return 2