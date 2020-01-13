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

    def dance(self):
        self.breathe()
        self.move()


Reginald = Giraffes()
Harold = Giraffes()

Reginald.dance()
#   print(Reginald.giraffe_spots)
