def solution(sizes):
    answer = 0
    for i in range(len(sizes)):
        if sizes[i][0]<sizes[i][1]: sizes[i][0] , sizes[i][1] = sizes[i][1] , sizes[i][0]
    return max([sizes[i][0] for i in range(len(sizes))]) * max([sizes[i][1] for i in range(len(sizes))])