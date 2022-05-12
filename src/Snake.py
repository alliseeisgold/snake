class Snake:

    def __init__(self, body=None, speed=15, color=None, position=None):
        if position is None:
            position = [50, 50]
        if body is None:
            body = [[50, 50], [40, 50], [30, 50]]
        if color is None:
            color = [255, 255, 255]
        self.speed = speed
        self.color = color
        self.body = body
        self.position = position

    def get_color(self):
        """
            Returns snake color
        """
        return self.color

    def get_speed(self):
        """
            Returns snake speed
        """
        return self.speed

    def get_body(self):
        """
            Returns snake body as list of lists
        """
        return self.body

    def get_position(self):
        """
            Returns snake head
        """
        return self.position

    def set_position(self, new_pos: list):
        """
            Changes snake head
        """
        self.position = new_pos

    def set_body(self, new_body: list):
        """
            Changes snake body
        """
        self.body = new_body

    def move(self, direction):
        """
            Moves snake looking at direction
        """
        if direction == 'UP':
            self.position[1] -= 10
        if direction == 'DOWN':
            self.position[1] += 10
        if direction == 'LEFT':
            self.position[0] -= 10
        if direction == 'RIGHT':
            self.position[0] += 10

