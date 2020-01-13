number_of_states = 0


def rolldice_sum_prob(sum_, dice_amount):
    global number_of_states
    total_states = 6 ** dice_amount
    summation(sum_, dice_amount, 1, 0)
    x = number_of_states
    number_of_states = 0
    return x / total_states


def summation(sum_, dice_amount, iteration, total):
    global number_of_states
    for x in range(1,7):
        if iteration < dice_amount:
            summation(sum_, dice_amount, iteration + 1, total + x)
        if iteration == dice_amount:
            if total + x == sum_:
                number_of_states += 1
                break



print(rolldice_sum_prob(8, 2))

