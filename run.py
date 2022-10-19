import pygame

class Run :
    def __init__(self) -> None:
        pygame.init()
        self.active = False
        self.screen = pygame.display.set_mode((300,720))
        self.background = pygame.image.load('background/background.jpg')
        self.background_rect = self.background.get_rect()

    def blit(self) :
        self.screen.fill((225,0,0))
        pygame.display.update()
