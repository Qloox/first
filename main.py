import pygame
from main_menu import Main_menu
from skin import Skin
from run import Run
from game_over import Game_over

class Game :

    def __init__(self) -> None:
        self.caption = pygame.display.set_caption('Star Shooter')
        self.clock = pygame.time.Clock()
        self.skin = Skin()
        self.main_menu = Main_menu()
        self.run = Run()
        self.game_over = Game_over()

while __name__ == '__main__' :
    game = Game()
    if game.main_menu.active :
        game.main_menu.blit()
        game.main_menu.my_control(game.run, game.skin)
        game.clock.tick(60)
    if game.run.active :
        game.run.blit()
        game.clock.tick(60)
        