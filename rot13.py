import string
from codecs import encode as _dont_use_this_


def rot13(message):
    newlist = []
    translated = []
    for x in message:
        for j in x:
            if x.isalpha():
                newlist.append(ord(j))
            else:
                newlist.append(str(j))
    for x in newlist:
        if type(x) == int:
            if x >= 97:
                x += 13
                if x > 122:
                    x -= 26
            if x <= 90:
                x += 13
                if x > 90:
                    x -= 26
            translated.append(chr(x))
        else:
            translated.append(x)
    h = ''.join(translated)
    return h



print(rot13('Te8st'))