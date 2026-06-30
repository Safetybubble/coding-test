def solution(arr, query):
    answer = []
    start = 0
    end = len(arr)-1
    for i in range(len(query)):
        if i%2==0:
            end = start + query[i]
            
        else:
            start = start + query[i]
    return arr[start:end+1]