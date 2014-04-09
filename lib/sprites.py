import pygame
from pygame.locals import *

#####################################
#--Fonctions de création de sprite--#
#####################################

class Bloc(pygame.sprite.Sprite):
    """Création d'un sprite plateforme"""

    def __init__(self, image):
        """Construction"""
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()

    def dessiner(self):
        self.bloc_liste.add(self)
        self.tous_sprites_liste.add(self)
