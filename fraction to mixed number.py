def hcfnaive(a,b):
    if(b==0):
        return a
    else:
        return hcfnaive(b,a%b)

def mixed_fraction(s):
    neg = 0
    dividend = ''
    divisor = ''
    for x in range(0,len(s)):
        if s[x] != '/':
            dividend += s[x]
        else:
            lim = x
            break
    for x in range(lim+1, len(s)):
        divisor += s[x]



    dividend = int(dividend.rstrip())
    divisor = int(divisor)

    if int(dividend) * int(divisor) < 0:
        dividend = abs(dividend)
        divisor = abs(divisor)
        neg = 1

    gcd = hcfnaive(dividend, divisor)

    dividend = int(dividend / gcd)
    divisor = int(divisor / gcd)

    whole = dividend // divisor
    frac = dividend%divisor

    if neg == 1 :
        if whole > 0 or frac > 0 :
            whole = whole * -1
        if whole == 0:
            frac = frac * -1

    if whole == 0 and frac == 0:
        return '0'
    if whole == 0 and frac !=0:
        return str(frac) + '/' + str(divisor)
    if whole != 0 and frac == 0:
        return str(whole)
    if whole !=0 and frac != 0:
        return str(whole) + ' ' + str(frac) + '/' + str(divisor)



