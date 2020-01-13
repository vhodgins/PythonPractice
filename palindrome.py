
while True:
    print('See if a word is a palindrome:')
    string = input()
    string = string.lower()
    base = []
    pali = []
    for c in string:
        base.append(c)

    for x in range(1,len(base)+1):
        pali.append(base[len(base)-x])

    if pali == base:
        print('palindrome')
    else:
        print('nah its not a palindrome')
