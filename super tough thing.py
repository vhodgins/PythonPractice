def longest_consec(strarr, k):
    final = ''
    prev = 0
    a = 0
    b = 0
    if k > len(strarr) or len(strarr) ==0 or k <= 0:
        return ""
    elif k == 1:
        for c in strarr:
            b = len(c)
            if b > prev:
                prev = b
                final = c
        return final
    elif k > 1:
        for x in range(0, len(strarr)-(k-1)):

            for m in range(0,k):
                b = b + len(strarr[m+x])
            if b > prev:
                a = x
                prev = b
            b = 0
        for l in range(a, a+k):
            final = final + strarr[l]
        return final

print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2))















