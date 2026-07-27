def solution(a, b):
    answer = ''
    month = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    D = b-1
    total_days = sum(days[:a-1]) + D
    return month[total_days%7]