def solution(score):
    average = [i+j for i , j in score]
    result = []
    for r in average:
        result.append(sorted(average, reverse=True).index(r)+1)
    return result