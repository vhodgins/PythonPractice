def sum_for_list(lst):

    primefactors = []
    p= 0
    zeta = []
    for j in lst:
        factors = []
        if j > 0:
            for c in range(1,j):
                if abs(j) % abs(c) == 0:
                    factors.append(c)
            for h in factors:
                p = 0
                for c in range(1,h):
                    if abs(h) % abs(c) == 0:
                        p += 1
                if p < 2:
                    if h > 1:
                        primefactors.append(h)
        else:
            for c in range(j,-1):
                if abs(j) % abs(c) == 0:
                    factors.append(c)
            for h in factors:
                p = 0
                for c in range(1,h):
                    if h % c == 0:
                        p += 1
                if p < 2:
                    if h < -1:
                        primefactors.append(h)
    primes = sorted(list(set(primefactors)))

    for j in primes:
        p =[]
        b = 0
        for x in lst:
            if x % j == 0:
                b += x

        p.append(j)
        p.append(b)
        zeta.append(p)

    return zeta
print(sum_for_list([12,15]))