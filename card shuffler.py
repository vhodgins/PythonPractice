import random


cards = []

def new_deck():
    for x in range(1,14):
        cards.append(str(x) + ' of diamonds')
    for x in range(1,14):
        cards.append(str(x) + ' of hearts')
    for x in range(1,14):
        cards.append(str(x) + ' of clubs')
    for x in range(1,14):
        cards.append(str(x) + ' of spades')


new_deck()
shuffle = []
tries = []
a = 0

def shuffler():
    a = random.randrange(0, len(cards))
    if a not in tries:
        shuffle.append(cards[a])
        tries.append(a)
    else:
        shuffler()

for i in range(0, len(cards)):
    a = random.randrange(0, len(cards))
    if a not in tries:
        shuffle.append(cards[a])
        tries.append(a)
    else:
        shuffler()
print(shuffle)

file = open('c:\\Users\\v3hod\\Desktop\\cards.txt', 'w')

for i in shuffle:
    file.write(i + ' \n')

file.close()



