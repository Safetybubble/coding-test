def solution(cards1, cards2, goal):
    answer = ''
    used_cards1=[]
    used_cards2=[]
    for i in goal:
        if cards1 and i == cards1[0]:
            used_cards1.append(cards1[0])
            del cards1[0]
        elif cards2 and i == cards2[0]:
            used_cards2.append(cards2[0])
            del cards2[0]
        else:
            return 'No'
    return 'Yes'