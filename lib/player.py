import pygame
from pygame.locals import *

#####################################
#-----Fonction joueur principal-----#
#####################################

class Player(pygame.sprite.Sprite):
    """Création d'un sprite player"""

    #Attributs

    change_x = 0
    change_y = 0

    animation_gauche = []
    animation_droite = []

    direction = 'R'

    scrolling = 0

    def __init__(self,num_niveau):
        """Construction"""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('image1_1.png').convert_alpha()

        #feuille = feuille_de_sprite('image1_1anim.png')
        #image = feuille.decouper(0, 0, 66, 90)
        #self.animation_droite.append(image)

        #image = feuille.decouper(0, 0, 66, 90)
        #image = pygame.transform.flip(image,True,False)
        #self.animation_gauche.append(image)

        #self.image = self.animation_droite[0]
        
        self.rect = self.image.get_rect()

    #def saut(self):
        

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

    def aller_droite(self):
        self.change_x = 6
        self.direction = "R"
        
    def aller_gauche(self):
        self.change_x = -6
        self.direction = "L"

    def stop(self):
        self.change_x = 0
        

