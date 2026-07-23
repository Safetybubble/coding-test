def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        check = str(bin(i|j)[2:])
        if len(check)!=n:
            while len(check)!=n:
                check = '0'+check
        box = ''
        for k in check:
            if k == '1':
                box+='#'
            else:
                box+=' '
        answer.append(box)
    return answer