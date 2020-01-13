import random

print('Lets play a game of rock paper scissors')
bestof = 3
game = 0
a = 0
your_score = 0
computer_score = 0
d = 0


def win():
    global your_score
    your_score += 1
    print('')
    print('You win!')


def lose():
    global computer_score
    computer_score += 1
    print('')
    print('You lose!')


def tie():
    print('')
    print('Oh, its a tie, try again')


while not bool(game):

    print('type in Rock, Paper, or Scissors')
    a = input()
    b = random.randrange(0, 2)

    if b == 0:
        b = 'Rock'
    elif b == 1:
        b = 'Paper'
    else:
        b = 'Scissors'

    print(b)

    if a == 'Rock':
        if b == 'Paper':
            lose()
        elif b == 'Scissors':
            win()
        else:
            tie()

    if a == 'Paper':
        if b == 'Paper':
            tie()
        elif b == 'Scissors':
            lose()
        else:
            win()

    if a == 'Scissors':
        if b == 'Paper':
            win()
        elif b == 'Scissors':
            tie()
        else:
            lose()

    print('You: ' + str(your_score))
    print('Computer: ' + str(computer_score))
    print('')
    if your_score == bestof:
        game = 'Player'
    if computer_score == bestof:
        game = 'Computer'

if game == 'Player':
    print('oh you won nice')

if game == 'Computer':
    print('haha i beat you asshole')

while True:
    's'
