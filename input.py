import sys

def agejoke():
    print('How old are you')
    age = int(sys.stdin.readline())
    if age == 17:
        print('nice')
    else:
        print('dumb')


agejoke()