import pygame
from pygame.locals import *

#####################################
#--Fonctions de création de sprite--#
#####################################

class Plateformes(pygame.sprite.Sprite):
    """Création d'un sprite plateforme"""

    def __init__(self, image, x, y):
        """Construction"""
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        
        self.platform_list.add(self)

class Ennemis(pygame.sprite.Sprite):
    """Création d'un sprite ennemie"""

    def __init__(self, image):
        """Construction"""
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        
        self.platform_list.add(self)
