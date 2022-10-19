import sys
import pygame

class Normal_control :
    def __init__(self) -> None:
        pygame.init()

    def control(self) :
        for ev in pygame.event.get() :
            if ev.type == pygame.QUIT :
                sys.exit()

class Main_control(Normal_control) :
    def control(self,run,skin) :
        Normal_control.control(self)
        for ev in pygame.event.get() :
            if ev.type == pygame.MOUSEBUTTONDOWN :
                if self.play_button_rect.collidepoint(ev.pos) :
                    self.active = False
                    run.active = True
                elif self.skin_button_rect.collidepoint(ev.pos) :
                    self.active = False
                    skin.active = True
