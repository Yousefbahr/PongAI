
class Pong:
    def __init__(self, body, direction = (0,0)):
        self.direction = direction
        self.body = body

    def move(self, width):
        for i, coord in enumerate(self.body):
            if i == 0 and self.body[-1][1] == width - 1 and self.direction[1] == 1:
                break
            if i == 0 and self.body[0][1] == 0 and self.direction[1] == -1:
                break
            self.body[i] = (coord[0] + self.direction[0], coord[1] + self.direction[1])
        self.direction = (0, 0)

    def __str__(self):
        return f"{self.body}"


