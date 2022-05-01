import pygame
import time
from src.Field import Field
from src.Snake import Snake


def show():
    pygame.init()
    snake = Snake(color=[100, 200, 250])
    a = Field.background
    b = snake.getColor()
    field_background_color = pygame.Color(a[0], a[1], a[2])
    snake_color = pygame.Color(b[0], b[1], b[2])
    pygame.display.set_caption('Snake')
    window = pygame.display.set_mode((Field.lengthX, Field.heightY))
    window.fill(field_background_color)
    for item in snake.getBody():
        pygame.draw.rect(window, snake_color, pygame.Rect(item[0], item[1], 10, 10))
    pygame.display.flip()
    fps = pygame.time.Clock()
    fps.tick(snake.getSpeed())
    time.sleep(1)


if __name__ == "__main__":
    show()
