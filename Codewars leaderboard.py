def de_nico(key,msg):
    sortedkey = ''.join(sorted(key))
    numkey = []
    [numkey.append(str(sortedkey.find(x))) for x in key]
    numkey = ''.join(numkey)
    output = []
    msg = msg.rstrip()
    dict = {}
    for x in numkey:
        dict[int(x)] = ''
    for x in range(len(msg)+(len(msg) % (len(numkey)))+10):
        j = ((x + len(numkey)) % len(numkey))
        if x < len(msg):
            dict[j] = dict[j] + msg[x]
        else:
            dict[j] = dict[j] + '?'
    print(dict)
    for h in range(len(dict[0])-1):
        for x in dict:
            output.append(dict[x][h])
    return (''.join(output)).rstrip().replace('?', "").rstrip()


print(de_nico("sprkcfvo","luzcrvzqrdmqce psgdeamrttn"))