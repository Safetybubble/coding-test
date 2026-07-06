def solution(id_pw, db):
    answer = ''
    for i in db:
        if id_pw == i:
            return 'login'
        elif id_pw[0] in i:
            return 'wrong pw'
    return 'fail'
    