dictionary = {
    'fox': -1,
    'goose': -1,
    'farmer': -1,
    'grain': -1,
    'none': 0
}

lose = 0
fitness = 0

# If the goose and fox are on the same bank without the farmer, lose. Likewise with the grain and goose. Only two states
# can be changed per transformation, one always being the farmer. The farmer's state change much match the state change
# of the other object


def inp(item):
    if item not in dictionary:
        return print("that doesn't exist in this scenario")
    else:
        if item == 'none':
            dictionary['farmer'] = dictionary["farmer"] * -1
        else:
            if dictionary[item] != dictionary['farmer']:
                return print("the farmer isnt with that item")
            else:
                dictionary[item] = dictionary[item] * -1
                dictionary["farmer"] = dictionary["farmer"] * -1


while True:
    while True:
        fitness += 1
        if dictionary["fox"] != 1 or dictionary["goose"] != 1 or dictionary["farmer"] != 1 or dictionary["grain"] != 1:
            if dictionary["fox"] == dictionary["goose"] and dictionary["fox"] != dictionary["farmer"]:
                lose = 1
                break
            if dictionary["goose"] == dictionary["grain"] and dictionary["goose"] != dictionary["farmer"]:
                lose = 2

                break

            print("pick an item to change river banks")
            item = input().lower().rstrip()
            inp(item)
        else:
            lose = -1
            break

    if lose == -1:
        print("you won")

    elif lose == 1:
        print("the fox ate the goose")
    elif lose == 2:
        print("the goose ate the grain")

    print(" . . . . . . . . . . . . ")

    print("Would You like to play again? Y/N")
    case = input().lower().rstrip()

    if case == 'n':
        break

    if case == 'y':
        dictionary = {
            'fox': -1,
            'goose': -1,
            'farmer': -1,
            'grain': -1,
            'none': 0
        }
        pass
