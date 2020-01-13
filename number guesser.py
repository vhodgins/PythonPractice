import sys
import random
import pickle
import time

while True:

    savefile = open('c:\\Users\\v3hod\\PycharmProjects\\helloworld\\save.dat', 'rb')

    times_played = int(pickle.load(savefile))
    savefile.close()


    print('type in a number')
    num = int(sys.stdin.readline())
    number = 1000000000000000
    guesses = ['']
    b = number
    c = 1
    d = 0
    time1 = time.time()

    while num != round(b):
        if b > num:
            b -= number / c
            b = round(b)
            print(b)
            d += 1
        if b < num:
            b += number / c
            b = round(b)
            print(b)
            d += 1
        c = c*2

    time2 = time.time()
    print(str(d) + ' guesses')
    print('in ' + str(time2-time1) + ' seconds')
    times_played += 1
    print(str(times_played) + ' times played')
    savefile = open('c:\\Users\\v3hod\\PycharmProjects\\helloworld\\save.dat', 'wb')
    pickle.dump(times_played, savefile)
    savefile.close()

    print('again?')
    sys.stdin.readline()

