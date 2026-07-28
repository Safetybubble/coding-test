def solution(priorities, location):
    answer = 0
    idx = [q for q in range(len(priorities))]
    arr = list(zip(priorities,idx))
    count = 0

    while len(arr):
        if arr[0][0] == max([w[0] for w in arr]):
            check_pop = arr.pop(0)
            count+=1
            if check_pop[1] == location:
                return count
        else:
            arr.append(arr.pop(0))