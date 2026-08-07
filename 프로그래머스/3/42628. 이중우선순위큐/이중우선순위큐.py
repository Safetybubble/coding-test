def solution(operations):
    answer = []
    table = []
    for i in operations:
        check = i.split()
        for j in check:
            if j == 'I':
                table.append(int(check[1]))
            elif j == 'D' and check[1] == '1' and len(table)!=0:
                table.remove(max(table))
            elif j == 'D' and check[1] == '-1' and len(table)!=0:
                table.remove(min(table))
    if len(table) == 0:
        return [0,0]
    return [max(table),min(table)]