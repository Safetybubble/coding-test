def solution(arr):
    count = 0
    while 1:
        before_arr = arr.copy()
        for i in range(len(arr)):
            if arr[i]>=50 and arr[i]%2==0:
                arr[i]//=2
            elif arr[i]< 50 and arr[i]%2==1:
                arr[i] = arr[i]*2+1
        if before_arr == arr:
            return count
        count+=1