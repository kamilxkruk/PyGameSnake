import pygame
from pygame.sprite import Sprite
from ustawienia import *

class PunktSprite(Sprite):

    def __init__(self,numerKratkiX,numerKratkiY):
        super().__init__()
        self.image = pygame.Surface((ROZMIAR_GRACZA,ROZMIAR_GRACZA))
        self.image.fill(ZOLTY)
        self.rect = self.image.get_rect()
        self.rect.topleft = ((numerKratkiX-1)*ROZMIAR_GRACZA,(numerKratkiY-1)*ROZMIAR_GRACZA)