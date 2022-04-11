import pygame


# Parent class for game levels' classes: Easy, Medium, Hard
class Game:
    def __init__(self, background_img, snake_color, snake_speed):
        self.background_img = background_img
        self.snake_color = snake_color
        self.snake_speed = snake_speed
        self.screen = pygame.display.set_mode((720, 480))

