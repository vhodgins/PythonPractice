def convertFracts(lst):
    denomlist = []
    newdenom = 1
    newlist = []
    newlist2 = []
    newlist3 = []
    for x in lst:
        for j in x:
            denomlist.append(j)
    for l in denomlist:
        newdenom = newdenom * l
    for x in lst:
        newlist2.append(round((x[0] / x[1]) * newdenom))
    denomlist = []
    for x in newlist2:
        for i in range(2, x):
            if x % i == 0:
                denomlist.append(i)
    b = set([x for x in denomlist if denomlist.count(x) == len(lst)])
    for x in b:
        newdenom = newdenom / x
    for x in lst:
        newlist.append(round((x[0] / x[1]) * round(newdenom)))
        newlist.append(round(newdenom))
        newlist3.append(newlist)
        newlist = []
    return newlist3


print(convertFracts([[1, 2], [1, 3], [1, 4]]))
