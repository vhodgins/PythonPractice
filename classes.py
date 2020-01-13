class Things:
    pass


class Inanimate(Things):
    pass


class Animate(Things):
    pass


class Sidewalks(Inanimate):
    pass


class Animals(Animate):
    def breathe(self):
        print('Breathes')

    def move(self):
        print('Moves')

    def eat(self):
        print('Eats')


class Mammals(Animals):
    def feed_young(self):
        print('Feeds Young')


class Giraffes(Mammals):
    def eat_leaves(self):
        print('Eats Leaves')
    def __init__(self, spots):
        self.giraffe_spots = spots


Reginald = Giraffes(203)
Harold = Giraffes(12)

Reginald.move()
Harold.eat_leaves()

print(Reginald.giraffe_spots)
