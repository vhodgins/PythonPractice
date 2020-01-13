import random

password = ''


def password_generate():
    x = 0
    print('Welcome to the password generator')
    print('Would you like a weak, medium, or strong password?')
    type1 = input()
    type1 = type1.lower()

    alphlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    if type1 == 'weak':
        x = 12
    elif type1 == 'medium':
        x = 24
    elif type1 == 'strong':
        x = 36

    for x in range(0, x):
        global password
        password = password + alphlist[random.randrange(0, len(alphlist))]
