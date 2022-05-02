from .Field import Field


class Snake:
    x = Field.lengthX // 2
    y = Field.heightY // 2

    def __init__(self, body=[[x, y], [x - 10, y], [x - 20, y]], speed=15, color=[255, 255, 255], position=[x, y]):
        self.speed = speed
        self.color = color
        self.body = body
        self.position = position

    def getColor(self):
        return self.color

    def getSpeed(self):
        return self.speed

    def getBody(self):
        return self.body

    def getPosition(self):
        return self.position

    def move(self, direction):
        if direction == 'R':
            self.position[0] += 10
        elif direction == 'L':
            self.position[0] -= 10
        elif direction == 'U':
            self.position[1] -= 10
        elif direction == 'D':
            self.position[1] += 10
        return self.position