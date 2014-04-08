import pygame
from pygame.locals import *

#####################################
#-----Fonction joueur principal-----#
#####################################

class Player():
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()

    def gravite(self):
        """Actualise la position du personnage
        lors d'un saut en fonction de la gravité"""
        g = 9.81
        pi = 3.14

        t = 0

        v_init = vitesse_x
        angle_init = pi/3

        v_x = cos(angle_init)*v_init
        v_y = sin(angle_init)*v_init

        position_relative_x = (int)(v_x*t);
        position_relative_y = (int)((v_y*t)-((g*t*t)/2000))

        self.image.rect.x = self.image.rect.x + position_relative_x
        self.image.rect.y = self.image.rect.y - position_relative_y

        t += 10

