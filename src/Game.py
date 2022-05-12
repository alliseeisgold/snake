import pygame
import time
from src.Fruits import generate_fruit
from src.Field import Field
from src.Platform import Platform
from src.Snake import Snake
from src.Maps import Maps
from pygame import mixer


# Parent class for game levels' classes: Easy, Medium, Hard


class Game:
    """
        Game class is the main class where implemented the logic of the game.
    """

    def __init__(self, snake_color, snake_speed, level):
        field = Field(background='imgs/easy_level_grass.xcf')
        self.background_img = field.get_background()
        self.snake_color = snake_color
        self.snake_speed = snake_speed
        self.screen = pygame.display.set_mode((field.get_length(),
                                               field.get_height()))
        self.sound = 'sounds/apple_bite.mp3'
        self.screen.blit(pygame.image.load(self.background_img), (0, 0))
        self.snake = Snake(speed=self.snake_speed, body=[[100, 50],
                                                         [90, 50],
                                                         [80, 50],
                                                         [70, 50]
                                                         ], position=[100, 50])
        self.level = level
        if self.level == 'Easy':
            self.level_map = Maps.easy_map
        else:
            self.level_map = Maps.hard_map

    def play(self):
        """
            Function of playing.
        """
        pygame.display.set_caption(self.level)
        fruit = Game.get_fruit(False, self.level_map)
        fruit_position = fruit.get_coords()
        fruit_spawn = True
        pineapple_time = False
        cnt = 0
        direction = 'RIGHT'
        fps = pygame.time.Clock()
        score = 0
        mixer.init()

        def show_score(color, font, size):
            """
                Shows the current score in the Field.
            """
            show = Game.score(score, color, font, size)
            self.screen.blit(show[0], show[1])

        def game_over():
            """
                Shows game over message.
            """
            over = Game.game_over(score)
            self.screen.blit(over[0], over[1])
            pygame.display.flip()
            time.sleep(1.2)
            pygame.quit()
            quit()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    direction = Game.changing_dir(event, direction)
                if event.type == pygame.QUIT:
                    game_over()
            self.snake.move(direction)
            xx = self.snake.get_position()[0]
            yy = self.snake.get_position()[1]
            r = self.snake.get_body()
            r.insert(0, list(self.snake.get_position()))
            self.snake.set_body(r)
            if Game.check(fruit_position, xx, yy, self.snake.get_position()):
                mixer.Sound.play(mixer.Sound(self.sound))
                score += 5 + 5 * pineapple_time
                pineapple_time = False
                fruit_spawn = False
            else:
                self.snake.get_body().pop()
            if not fruit_spawn:
                cnt += 1
                if cnt == 5:
                    cnt = 0
                    pineapple_time = True
                    self.snake_speed += 40
                fruit = Game.get_fruit(pineapple_time, self.level_map)
                fruit_position = fruit.get_coords()
            fruit_spawn = True
            self.screen.blit(pygame.image.load(self.background_img),
                             (0, 0))
            for items in Game.draw_map(self.level_map):
                self.screen.blit(items[0].image, (items[1], items[2]))
            for pos in self.snake.get_body():
                pygame.draw.rect(self.screen,
                                 self.snake_color,
                                 pygame.Rect(pos[0], pos[1], 10, 10))
            if Game.is_collide_with_wall(self.snake.get_position(),
                                         self.level_map) or \
                    Game.is_collide_with_itself(self.snake.get_position(),
                                                self.snake.get_body()):
                mixer.Sound.play(mixer.Sound('sounds/loser.mp3'))
                game_over()
            pygame.draw.circle(self.screen, fruit.get_color(),
                               (fruit_position[0], fruit_position[1]),
                               fruit.get_radius())
            self.snake.set_position(Game.is_in_field(self.snake.get_position()))
            show_score('white', 'rasa', 20)
            pygame.display.update()
            fps.tick(self.snake.speed)

    @staticmethod
    def draw_map(level_map: list):
        """
            This function is for getting walls rectangles and other platform datas.
        """
        x = y = 0
        platforms = []
        for row in level_map:
            for col in row:
                if col == "-":
                    pf = Platform(x, y)
                    platforms.append([pf, x, y, pf.get_rect()])
                x += 28.67
            y += 23.67
            x = 0
        return platforms

    @staticmethod
    def is_collide_with_wall(head: list, level_map: list):
        """
            Returns True if there is collision between snake and walls.
        """
        collision = False
        walls = Game.draw_map(level_map)
        for items in walls:
            if pygame.Rect.colliderect(pygame.Rect(head[0], head[1], 10, 10),
                                       items[3]):
                collision = True
        return collision

    @staticmethod
    def is_collide_with_itself(head: list, body: list):
        """
            Returns True if there is collision between snake and itself.
        """
        collision = False
        for block in body[1:]:
            if head[0] == block[0] and head[1] == block[1]:
                collision = True
                break
        return collision

    @staticmethod
    def check(fruit_position: list, x: int, y: int, snake_position: list):
        """
            Returns True if snake eats the fruit
        """
        flag = False
        if (pow(x - fruit_position[0], 2) + pow(y - fruit_position[1], 2)) < 49:
            flag = True
        elif (pow(snake_position[0] - fruit_position[0], 2) +
              pow(snake_position[1] + 10 - fruit_position[1], 2)) < 49:
            flag = True
        elif (pow(snake_position[0] - 10 - fruit_position[0], 2) +
              pow(snake_position[1] - fruit_position[1], 2)) < 49:
            flag = True
        elif (pow(snake_position[0] + 10 - fruit_position[0], 2) +
              pow(snake_position[1] - fruit_position[1], 2)) < 49:
            flag = True
        return flag

    @staticmethod
    def get_fruit(flag_time: bool, level_map: list):
        """
            Return fruit coordinates if there is no collision with walls.
        """
        if flag_time:
            what_fruit = 'Pineapple'
        else:
            what_fruit = 'Apple'
        while True:
            fruit = generate_fruit(what_fruit)
            rad = fruit.get_radius()
            coord = fruit.get_coords()
            walls = Game.draw_map(level_map)
            flag = False
            for items in walls:
                if pygame.Rect.colliderect(
                        pygame.Rect(coord[0] - rad, coord[1] - rad, rad, rad),
                        items[3]):
                    flag = True
            if not flag:
                break
        return fruit

    @staticmethod
    def is_in_field(snake_position: list):
        """
            Returns position of the snake after module to length and height of the Field.
        """
        pos = snake_position
        if snake_position[0] < 0:
            pos[0] = 715
        elif snake_position[0] > 720:
            pos[0] = 0
        if snake_position[1] < 0:
            pos[1] = 475
        elif snake_position[1] > 480:
            pos[1] = 0
        return pos

    @staticmethod
    def score(score: int, color: str, font: str, size: int):
        """
            Returns current score as message.
        """
        score_font = pygame.font.SysFont(font,
                                         size,
                                         bold=pygame.font.Font.bold)
        score_surface = score_font.render('Score : ' + str(score), True, color)
        score_rect = score_surface.get_rect()
        return [score_surface, score_rect]

    @staticmethod
    def game_over(score: int):
        my_font = pygame.font.SysFont('rasa',
                                      50,
                                      bold=pygame.font.Font.bold)
        game_over_surface = my_font.render(
            'Your Score is : ' + str(score), True, '#FFFFF1')
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (Field().get_length() / 2, Field().get_height() / 4)
        return [game_over_surface, game_over_rect]

    @staticmethod
    def changing_dir(event, direction: str):
        """
            Changes directions looking at what key have you pressed.
        """
        change_to = ''
        if event.key == pygame.K_UP or \
                event.key == pygame.K_w:
            change_to = 'UP'
        if event.key == pygame.K_DOWN or \
                event.key == pygame.K_s:
            change_to = 'DOWN'
        if event.key == pygame.K_LEFT or \
                event.key == pygame.K_a:
            change_to = 'LEFT'
        if event.key == pygame.K_RIGHT or \
                event.key == pygame.K_d:
            change_to = 'RIGHT'
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'
        return direction
