import sys

print('Hello, please give me a number')

num = int(sys.stdin.readline())

if num % 2 == 0:
    print('That number is even')
else:
    print('That number is odd')

if num % 4 == 0:
    print('This number is also a multiple of four')

