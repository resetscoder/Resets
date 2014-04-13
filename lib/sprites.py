import pygame
from pygame.locals import *

#####################################
#--Fonctions de création de sprite--#
#####################################

class Bloc(pygame.sprite.Sprite):
    """Création d'un sprite plateforme"""

    def __init__(self, image, x, y, width, height):
        """Construction"""
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image).convert_alpha()

        #Faire une fonction qui redimmensionne les images !!!
        #Il faut donc utiliser des images carrées !!
        #w = self.image.get_width()
        #prodcroix = etc...
        #self.image = pygame.transform.scale(self.image,(

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        
