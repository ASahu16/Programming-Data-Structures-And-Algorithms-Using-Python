def addpoly(p1, p2):
    result = list()
    for i in range(len(p1)):
        swap = False
        for j in range(len(p2)):
            if p1[i][1] == p2[j][1]:
                swap = True
                if p1[i][0] + p2[j][0] != 0:
                    result.append((p1[i][0] + p2[j][0], p1[i][1]))
                p2.pop(j)
                break
        if swap == False:
            result.append((p1[i][0], p1[i][1]))
    result = result + p2
    result = sorted(result, key=lambda tup: tup[1], reverse=True)
    return result


def multpoly(p1, p2):
    result = [[],[]]
    for i in range(len(p1)):
        for j in range(len(p2)):
            result[i].append((p1[i][0] * p2[j][0], p1[i][1] + p2[j][1]))
    return addpoly(result[0], result[1])

print(addpoly([(4,3),(3,0)],[(-4,3),(2,1)]))
print(addpoly([(2,1)],[(-2,1)]))
print(multpoly([(1,1),(-1,0)],[(1,2),(1,1),(1,0)]))