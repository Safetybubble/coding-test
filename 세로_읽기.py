# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/181904
# m글자씩 가로로, 그 중 c번째 세로줄을 읽는다고 했을때, 슬라이싱 방식으로 m씩 끊는다면 c=0일떄의 값.
# 그렇다면 c=1일때의 값은 출발지에서 +1하고 m의 배수만큼의 값. 즉, 시작점은 C-1(인덱스는0부터시작)이고 m씩 띄어가며 출력 
def solution(my_string, m, c):
    return my_string[c-1::m]
