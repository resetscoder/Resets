import pygame
from pygame.locals import *

#####################################
#-----Fonction joueur principal-----#
#####################################

class Player(pygame.sprite.Sprite):
    """Création d'un sprite player"""
    def __init__(self):
        """Construction"""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('image1_1.png').convert_alpha()
        self.rect = self.image.get_rect()

    def saut(self):
        

    def gravite_newton(self):
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

        self.rect.x = self.rect.x + position_relative_x
        self.rect.y = self.rect.y - position_relative_y

        t += 10

