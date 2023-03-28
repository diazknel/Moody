import string


class Rover:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def turn_left(self):
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'

    def turn_right(self):
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'W':
            self.direction = 'N'

    def move(self):
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'W':
            self.x -= 1

    def execute(self, commands):
        for c in commands:
            if c == 'L':
                self.turn_left()
            elif c == 'R':
                self.turn_right()
            elif c == 'M':
                self.move()

    def __str__(self):
        return f"{self.x} {self.y} {self.direction}"


# read input
print('Press CMD + D (Unix) or CTRL + Z (Windows) to exit')
upper_right = tuple(map(int, input().split()))
rovers = []
while True:
    try:
        position = input().split()
        commands = input()
        rovers.append(Rover(int(position[0]), int(position[1]), position[2]))
        rovers[-1].execute(commands)
    except:
        break
# print output
print('Final Position')
count = 1
for R in rovers:
    position = str(count)
    print('Rover ' + position + ' in :' + str(R.x), str(R.y), R.direction)
    count = count + 1
