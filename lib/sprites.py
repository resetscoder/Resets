import pygame
from pygame.locals import *

#####################################
#--Fonctions de crÃ©ation de sprite--#
#####################################

class Bloc(pygame.sprite.Sprite):
    """CrÃ©ation d'un sprite plateforme"""

    def __init__(self, image, x, y):
        """Construction"""
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.bloc_liste.add(self)
        self.tous_sprites_liste.add(self)
        
