def solution(lottos, win_nums):
    answer = []
    basic_rank = len(set(lottos)&set(win_nums))
    print(basic_rank)
    return answer