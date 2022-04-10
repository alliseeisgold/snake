# from src.Menu import Menu
# from src.Button import Button
# import pygame
#
# from src import Game
#
# pygame.init()
#
#
# class Show:
#     def __init__(self):
#         self.screen = pygame.display.set_mode((720, 480))
#         self.title = 'Snake Game'
#         self.menu_background = Menu.BACKGROUND
#         self.menu_font = Menu.FONT
#         self.variant_font_size = Menu.VARIANT_TEXT_SIZE
#         self.button_font_size = Menu.BUTTONS_SIZE
#         self.menu_text_font_size = Menu.MENU_TEXT_FONT_SIZE
#         self.menu_text = pygame.font.Font(Menu.FONT, Menu.MENU_TEXT_FONT_SIZE)
#         self.choose = pygame.font.Font(Menu.FONT, Menu.VARIANT_TEXT_SIZE)
#         self.easy = Button(pygame.image.load(Menu.BUTTONS_BACKGROUND), (360, 200),
#                            "EASY", pygame.font.Font(Menu.FONT, Menu.VARIANT_TEXT_SIZE), "#378300", "Black")
#         self.medium = Button(pygame.image.load(Menu.BUTTONS_BACKGROUND), (360, 300),
#                              "MEDIUM", pygame.font.Font(Menu.FONT, Menu.VARIANT_TEXT_SIZE), "#FFE900", "Black")
#         self.hard = Button(pygame.image.load(Menu.BUTTONS_BACKGROUND), (360, 400),
#                            "HARD", pygame.font.Font(Menu.FONT, Menu.VARIANT_TEXT_SIZE), "#FF0300",
#                            'Black')
#
#     def show_menu(self):
#         pygame.display.set_caption(self.title)
#         self.screen.blit(pygame.image.load(self.menu_background), (0, 0))
#         self.menu_text = self.menu_text.render(Menu.MENU_TEXT, False, "#000000")
#         self.choose = self.choose.render(Menu.VARIANT, False, pygame.color.Color(3, 99, 5))
#         self.screen.blit(self.menu_text, self.menu_text.get_rect(center=(350, 50)))
#         self.screen.blit(self.choose, self.choose.get_rect(center=(340, 100)))
#         run = True
#         while run:
#             mouse = pygame.mouse
#             for button in [self.easy, self.medium, self.hard]:
#                 button.changeColor(mouse.get_pos())
#                 button.update(self.screen)
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     run = False
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     if self.easy.checkForInput(mouse.get_pos()):
#                         Game.game()
#                         run = False
#             pygame.display.update()
