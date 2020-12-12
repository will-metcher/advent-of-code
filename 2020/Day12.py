import utils

headings = {0: "N", 90: "E", 180: "S", 270: "W"}
directions = utils.read_file("day12").split("\n")


class Object:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.heading = 90

    def move(self, direction, amount):
        if direction == "N":
            self.y -= amount
        elif direction == "S":
            self.y += amount
        elif direction == "E":
            self.x += amount
        elif direction == "F":
            self.move(headings[self.heading], amount)
        else:
            self.x -= amount

    def turn(self, direction, amount):
        if direction == "L":
            self.heading -= amount
        else:
            self.heading += amount

        if self.heading >= 360:
            self.heading -= 360
        elif self.heading < 0:
            self.heading += 360

    def move_to_waypoint(self, waypoint, amount):
        self.x += waypoint.x * amount
        self.y += waypoint.y * amount


class Waypoint(Object):
    def __init__(self):
        super().__init__()
        self.x = 10
        self.y = -1

    def rotate(self, direction, amount, ship):
        turns = int(amount / 90)
        for i in range(turns):
            temp = self.x
            self.x = self.y
            self.y = temp
            if direction == "R":
                self.x *= -1
            else:
                self.y *= -1


def part_1():
    ship = Object()
    for d in directions:
        command = d[0]
        amount = int(d[1:])
        if command == "L" or command == "R":
            ship.turn(command, amount)
        else:
            ship.move(command, amount)

    print(utils.manhatten_distance(0, 0, ship.x, ship.y))


def part_2():
    ship = Object()
    waypoint = Waypoint()
    for d in directions:
        command = d[0]
        amount = int(d[1:])
        if command in headings.values():
            waypoint.move(command, amount)
        elif command == "L" or command == "R":
            waypoint.rotate(command, amount, ship)
        else:
            ship.move_to_waypoint(waypoint, amount)

    print(utils.manhatten_distance(0,0,ship.x, ship.y))


part_1()
part_2()
