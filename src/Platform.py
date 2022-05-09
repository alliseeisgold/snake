from pygame import *

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32


class Platform(sprite.Sprite):
    """
        Class for platform: walls
    """

    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image = image.load("imgs/platform.png")
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

    def get_rect(self):
        """
            Returns the rectangle where image will be drawn
        """
        return self.rect
