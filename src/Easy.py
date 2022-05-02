# Class for implementing easy level

import random
import time

from src.Game import Game
import pygame
import src.Fruits as fruits


class Easy(Game):

    def __init__(self):
        super().__init__('imgs/easy_level_grass.xcf', '#1100FF', 15)

    def play(self):
        pygame.display.set_caption('Easy Level')
        self.screen.blit(pygame.image.load(self.background_img), (0, 0))
        snake_position = [100, 50]
        snake_body = [[100, 50],
                      [90, 50],
                      [80, 50],
                      [70, 50]
                      ]
        fruit_position = [random.randrange(1, (720 // 10)) * 10,
                          random.randrange(1, (480 // 10)) * 10]
        fruit_spawn = True

        # setting default snake direction towards
        # right
        direction = 'RIGHT'
        change_to = direction
        fps = pygame.time.Clock()
        # initial score
        score = 0

        # displaying Score function
        def show_score(choice, color, font, size):
            # creating font object score_font
            score_font = pygame.font.SysFont(font, size)

            # create the display surface object
            # score_surface
            score_surface = score_font.render('Score : ' + str(score), True, color)

            # create a rectangular object for the text
            # surface object
            score_rect = score_surface.get_rect()

            # displaying text
            self.screen.blit(score_surface, score_rect)

        # game over function
        def game_over():
            # creating font object my_font
            my_font = pygame.font.SysFont('times new roman', 50)

            # creating a text surface on which text
            # will be drawn
            game_over_surface = my_font.render(
                'Your Score is : ' + str(score), True, '#FF000C')

            # create a rectangular object for the text
            # surface object
            game_over_rect = game_over_surface.get_rect()

            # setting position of the text
            game_over_rect.midtop = (720 / 2, 480 / 4)

            # blit will draw the text on screen
            self.screen.blit(game_over_surface, game_over_rect)
            pygame.display.flip()

            # after 0.2 seconds we will quit the program
            time.sleep(0.2)

            # deactivating pygame library
            pygame.quit()

            # quit the program
            quit()

        # Main Function
        while True:
            # handling key events
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        change_to = 'UP'
                    if event.key == pygame.K_DOWN:
                        change_to = 'DOWN'
                    if event.key == pygame.K_LEFT:
                        change_to = 'LEFT'
                    if event.key == pygame.K_RIGHT:
                        change_to = 'RIGHT'
                if event.type == pygame.QUIT:
                    game_over()

            # If two keys pressed simultaneously
            # we don't want snake to move into two
            # directions simultaneously
            if change_to == 'UP' and direction != 'DOWN':
                direction = 'UP'
            if change_to == 'DOWN' and direction != 'UP':
                direction = 'DOWN'
            if change_to == 'LEFT' and direction != 'RIGHT':
                direction = 'LEFT'
            if change_to == 'RIGHT' and direction != 'LEFT':
                direction = 'RIGHT'

            # Moving the snake
            if direction == 'UP':
                snake_position[1] -= 10
            if direction == 'DOWN':
                snake_position[1] += 10
            if direction == 'LEFT':
                snake_position[0] -= 10
            if direction == 'RIGHT':
                snake_position[0] += 10

            # Snake body growing mechanism
            # if fruits and snakes collide then scores
            # will be incremented by 10
            xx = snake_position[0]
            yy = snake_position[1]

            snake_body.insert(0, list(snake_position))
            if (pow(xx - fruit_position[0], 2) + pow(yy - fruit_position[1], 2)) < 49:
                score += 10
                fruit_spawn = False
            elif (pow(snake_position[0] - fruit_position[0], 2) + pow(snake_position[1] + 10 - fruit_position[1],
                                                                      2)) < 49:
                score += 10
                fruit_spawn = False
            elif (pow(snake_position[0] - 10 - fruit_position[0], 2) + pow(snake_position[1] - fruit_position[1],
                                                                           2)) < 49:
                score += 10
                fruit_spawn = False
            elif (pow(snake_position[0] + 10 - fruit_position[0], 2) + pow(snake_position[1] - fruit_position[1],
                                                                           2)) < 49:
                score += 10
                fruit_spawn = False
            else:
                snake_body.pop()

            if not fruit_spawn:
                fruit_position = [random.randrange(1, (720 // 10)) * 10,
                                  random.randrange(1, (480 // 10)) * 10]

            fruit_spawn = True

            self.screen.blit(pygame.image.load(self.background_img), (0, 0))

            for pos in snake_body:
                pygame.draw.rect(self.screen, self.snake_color,
                                 pygame.Rect(pos[0], pos[1], 10, 10))

            pygame.draw.circle(self.screen, '#FF0000', (fruit_position[0], fruit_position[1]), 7)

            # pygame.draw.rect(self.screen, '#FF0000', pygame.Rect(
            #    fruit_position[0], fruit_position[1], 10, 10))

            if snake_position[0] < 0:
                snake_position[0] = 715
            elif snake_position[0] > 720:
                snake_position[0] = 0
            if snake_position[1] < 0:
                snake_position[1] = 475
            elif snake_position[1] > 480:
                snake_position[1] = 0

            # Touching the snake body
            for block in snake_body[1:]:
                if snake_position[0] == block[0] and snake_position[1] == block[1]:
                    game_over()

            # displaying score countinuously
            show_score(1, '#F1FFFF', 'times new roman', 20)
            # Refresh game screen
            pygame.display.update()

            # Frame Per Second /Refresh Rate
            fps.tick(self.snake_speed)
