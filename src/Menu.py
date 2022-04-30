from src.Button import Button
import pygame
from src.Easy import Easy

pygame.init()


class Menu:
    def __init__(self):
        self.screen = pygame.display.set_mode((720, 480))
        self.title = 'Snake Game'
        self.FONT = "font/font.ttf"
        self.BUTTONS_BACKGROUND = "imgs/Buttons_bg.xcf"
        self.BACKGROUND = "imgs/menu_background.jpg"
        self.MENU_TEXT_FONT_SIZE = 50
        self.VARIANT_TEXT_SIZE = 30
        self.BUTTONS_SIZE = 40
        self.CHOOSE = pygame.font.Font(self.FONT, self.VARIANT_TEXT_SIZE)
        self.MENU_TEXT = pygame.font.Font(self.FONT, self.MENU_TEXT_FONT_SIZE)
        self.EASY = Button(pygame.image.load(self.BUTTONS_BACKGROUND), (360, 200),
                           "EASY", pygame.font.Font(self.FONT, self.VARIANT_TEXT_SIZE), "#378300", "Black")
        self.MEDIUM = Button(pygame.image.load(self.BUTTONS_BACKGROUND), (360, 300),
                             "MEDIUM", pygame.font.Font(self.FONT, self.VARIANT_TEXT_SIZE), "#FFE900", "Black")
        self.HARD = Button(pygame.image.load(self.BUTTONS_BACKGROUND), (360, 400),
                           "HARD", pygame.font.Font(self.FONT, self.VARIANT_TEXT_SIZE), "#FF0300",
                           'Black')

    def show_menu(self):
        pygame.display.set_caption(self.title)
        self.screen.blit(pygame.image.load(self.BACKGROUND), (0, 0))
        self.MENU_TEXT = self.MENU_TEXT.render('MAIN MENU', False, "#000000")
        self.CHOOSE = self.CHOOSE.render('Choose game level', False, pygame.color.Color(3, 99, 5))
        self.screen.blit(self.MENU_TEXT, self.MENU_TEXT.get_rect(center=(350, 50)))
        self.screen.blit(self.CHOOSE, self.CHOOSE.get_rect(center=(340, 100)))
        run = True
        while run:
            mouse = pygame.mouse
            for button in [self.EASY, self.MEDIUM, self.HARD]:
                button.changeColor(mouse.get_pos())
                button.update(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.EASY.checkForInput(mouse.get_pos()):
                        b = Easy()
                        b.play()
                    elif self.MEDIUM.checkForInput(mouse.get_pos()):
                        pass
                    elif self.HARD.checkForInput(mouse.get_pos()):
                        pass
                    else:
                        continue
            pygame.display.update()
