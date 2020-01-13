print('Welcome to the Caesar Cipher, enter a sentence to be ciphered')
string = str(input()).lower()
print('And how many spaces you want to cipher it')
cipherconstant = int(input())

# string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
# cipherconstant = 2
alphabet = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 12,
    'n': 13,
    'o': 14,
    'p': 15,
    'q': 16,
    'r': 17,
    's': 18,
    't': 19,
    'u': 20,
    'v': 21,
    'w': 22,
    'x': 23,
    'y': 24,
    'z': 25

}
alphabet1 = {v: k for k, v in alphabet.items()}
list1 = []
list2 = []
list3 = []
string2 = ''
for c in string:
    if c not in alphabet:
        list1.append(c)
    else:
        list1.append('{}'.format(alphabet[c]))

for c in list1:
    if c.isdigit() == False:
        list2.append(str(c))
    else:
        if int(c) + cipherconstant > 25:
            list2.append(str(int(c) + cipherconstant -26))
        else:
            list2.append(str(int(c) + cipherconstant))

for c in list2:
    if c.isdigit() == False:
        list3.append(c)
    else:
        list3.append('{}'.format(alphabet1[int(c)]))


ciphered = ''.join(list3)

print(ciphered)
