def solution(polynomial):
    # 결과값은 무조건 ax+b 형태
    answer = ''
    P = polynomial.split()
    a = 0
    b = 0
    for i in P:
        if i.isdigit():
            b+=int(i)
        elif i == '+':
            continue
        else:
            if i.replace('x','') == '':
                a+=1
            else:
                a+=int(i.replace('x',''))
    
    if a==0:return str(b)

    if a==1 and b==0: return 'x'
    elif a==1 and b!=0: return f"x + {b}"
    elif a!=1 and b==0: return f"{a}x"
    else: return f"{a}x + {b}"