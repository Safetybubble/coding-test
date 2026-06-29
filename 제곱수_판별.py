# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/120909
# 소수점 뒷자리가 0이 아니라면 제곱수가 아니므로 소수점 뒷자리 판별을 하기위해 1로 나누었을때 나머지가 0인지 아닌지 확인.
# 0이라면 제곱수, 아니라면 제곱수가 아님. 즉 0이면 1, 아니면 2를 반환.
def solution(n):
    return 1 if n**0.5%1==0 else 2
