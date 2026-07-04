def solution(strArr):
    result = strArr.copy()
    for i in range(len(strArr)):
        if i%2==0:
            result[i] = strArr[i].lower()
        else:
            result[i] = strArr[i].upper()
    return result