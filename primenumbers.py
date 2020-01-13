x = 0

while True:
    x +=1
    p = 0
    for c in range(1,x):
        if x % c == 0:
            p += 1
    if p < 2:
        print(x)