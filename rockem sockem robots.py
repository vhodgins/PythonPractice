def fight(robot_1, robot_2, tactics):
    class Robot:
        def __init__(self, name, health, speed, tactics):
            self.name = name
            self.health = health
            self.speed = speed
            self.tactics = tactics

    r1 = Robot(robot_1["name"], robot_1["health"], robot_1["speed"], robot_1["tactics"])
    r2 = Robot(robot_2["name"], robot_2["health"], robot_2["speed"], robot_2["tactics"])
    tac = tactics
    time = 0

    if bool(r1.tactics) == False and bool(r2.tactics) == False:
        return "The fight was a draw."
    if bool(r1.tactics) == False:
        return r2.name + " has won the fight."
    if bool(r2.tactics) == False:
        return r1.name + " has won the fight."

    while r1.health > 0 or r2.health > 0:

        if r1.speed >= r2.speed:

            r2.health -= tac[r1.tactics[time]]

            if r2.health <= 0:
                return r1.name + " has won the fight."

            r1.health -= tac[r2.tactics[time]]

            if r1.health <= 0:
                return r2.name + " has won the fight."

        elif r1.speed < r2.speed:

            r1.health -= tac[r2.tactics[time]]
            if r1.health <= 0:
                return r2.name + " has won the fight."

            r2.health -= tac[r1.tactics[time]]
            if r2.health <= 0:
                return r1.name + " has won the fight."

        time += 1

        if time > len(r1.tactics) - 1 and time > len(r2.tactics) - 1:
            if r1.health == r2.health:
                return "The fight was a draw."
            elif r1.health > r2.health:
                return r1.name + " has won the fight."
            else:
                return r2.name + " has won the fight."

