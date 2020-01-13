
def partitioner(n,l):
    global partitions
    for x in range(0,n):
        list = [x]
        if (n-x)/l % 1 == 0:
            for j in range(l):
                list.append(int((n-x)/l))
            if sorted(list) not in partitions:
                if x != 0 and (n-x)/l != 0:
                    partitions.append(sorted(list))

def part(n):
    global partitions
    partitions = [[n]]

    for x in range(0,n):
        partitioner(n,n-x)


    return (partitions)


print(part(6))





