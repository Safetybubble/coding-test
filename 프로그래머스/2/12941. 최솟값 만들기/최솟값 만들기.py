def solution(A,B):
    answer = 0

    st_A = sorted(A)
    st_B = sorted(B, reverse = True)
    for i in range(len(A)):
        answer+=st_A[i]*st_B[i]

    return answer