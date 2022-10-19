import pygame
import control
class Main_menu :
    
    def __init__(self) -> None:
        pygame.init()
        self.active = True
        self.screen = pygame.display.set_mode((300,720))
        self.title = pygame.transform.scale(pygame.image.load('TITLE.png'),(270,75))
        self.background = pygame.image.load('background/background.jpg')
        self.background_rect = self.background.get_rect()
        self.play_button = pygame.transform.scale(pygame.image.load('button/play.png'),(75,75))
        self.play_button_rect = self.play_button.get_rect()
        self.skin_button = pygame.transform.scale(pygame.image.load('button/skin.png'),(75,75))
        self.skin_button_rect = self.skin_button.get_rect()

    def blit(self) :
        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.title, (15,100))
        self.screen.blit(self.play_button, (112,200))
        self.screen.blit(self.skin_button, (112,300))
        pygame.display.update()

    def my_control(self,run,skin) :
        control.Main_control().control(run,skin)