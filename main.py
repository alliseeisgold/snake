import pygame
import time
from src.Field import Field
from src.Snake import Snake
import src.Fruits as fruits


def show():
    pygame.init()
    pygame.display.set_caption('Snake')
    window = pygame.display.set_mode((Field.lengthX, Field.heightY))
    snake = Snake(color=[100, 200, 250])


if __name__ == "__main__":
    show()

    # snake = Snake(color=[100, 200, 250])
    # a = Field.background
    # b = snake.getColor()
    # field_background_color = pygame.Color(a[0], a[1], a[2])
    # snake_color = pygame.Color(b[0], b[1], b[2])
    # pygame.display.set_caption('Snake')
    # window = pygame.display.set_mode((Field.lengthX, Field.heightY))
    # window.fill(field_background_color)
    # flag = True
    # while flag:
    #     change_to = ''
    #     for event in pygame.event.get():
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_UP:
    #                 change_to = 'UP'
    #             if event.key == pygame.K_DOWN:
    #                 change_to = 'DOWN'
    #             if event.key == pygame.K_LEFT:
    #                 change_to = 'LEFT'
    #             if event.key == pygame.K_RIGHT:
    #                 change_to = 'RIGHT'
    #         if event.type == pygame.QUIT:
    #             break
    #     for item in snake.getBody():
    #         pygame.draw.rect(window, snake_color, pygame.Rect(item[0], item[1], 10, 10))
    #     snake.move(change_to)
    #     apple = fruits.generate_fruit('Apple')
    #     pineapple = fruits.generate_fruit('Pineapple')
    #     pygame.draw.circle(window, apple.getColor(), apple.getCoords(), 5, 5)
    #     pygame.draw.rect(window, pineapple.getColor(),
    #                      pygame.Rect(pineapple.getCoords()[0], pineapple.getCoords()[1], 10, 15),
    #                      border_radius=2)
    #     pygame.display.update()
    # fps = pygame.time.Clock()
    # fps.tick(snake.getSpeed())