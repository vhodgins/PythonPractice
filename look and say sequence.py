

a = [1, 11, 21, 1211, 111221]
b = [111, 113]
c = []
d = '1211'

for x in range(0, 27):
    o = 1
    for h in range(0, len(d)):

        if h < len(d)-1:
            if d[h] == d[h+1]:
                o += 1
            else:
                c.append(str(o) + str(d[h]))
                o = 1
        else:
            c.append(str(o)+str(d[h]))

    d = ''.join(c)
    c = []
    print(d)
print(len(d))