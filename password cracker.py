import random , time
password = ''
def password_generate():
    x = 0
    print('Welcome to the password generator')
    print('How many digits do you want your password to be?')
    x = int(input())
    '''
    print('Would you like a weak, medium, or strong password?')
    type1 = input()
    type1 = type1.lower()
    '''

    alphlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    alphlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    '''
    if type1 == 'weak':
        x = 5
    elif type1 == 'medium':
        x = 24
    elif type1 == 'strong':
        x = 36
    '''
    for x in range(0, x):
        global password
        password = password + alphlist[random.randrange(0, len(alphlist))]


password_generate()
print(password)

input("Press Enter To Try and crack")
t1 = time.time()
crack = 0
p = 0
g = 0
while p == 0:
    crack = int(crack)
    crack += 1
    crack = str(crack)
    while len(crack) < len(password):
        crack = '0' + crack
    if crack == password:
        p = 1
    print(crack)
    g += 1



print("Password: " + str(crack) + ' cracked, in ' + str(g) + ' guesses and ' + str(time.time()-t1) + ' seconds')
