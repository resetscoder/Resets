import os
import sys

from constantes import *
from feuilledesprite import *
from math import cos
from math import sin

import pygame
from pygame.locals import *

#####################################
#-----Fonction joueur principal-----#
#####################################

class Player(pygame.sprite.Sprite):
    """Création d'un sprite player"""

    #Attributs

    #vitesse du joueur (de combien il doit se deplacer en un tour de boucle)
    derive_x = 0
    derive_y = 0

    #liste donctenant les differentes positions de l'image du player
    animation_gauche = []
    animation_droite = []

    #direction dans laquelle va le joueur
    direction = 'droite'

    #nombre de pixel dont le niveau s'est déplacé
    scrolling = 0

    falling = False
    newton = False

    def __init__(self,num_niveau,bloc_liste,tous_sprites_liste):
        """Construction"""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(DOSSIER_DATA,'image1_1.png')).convert_alpha()

        #feuille = feuille_de_sprite('image1_1anim.png')
        #image = feuille.decouper(0, 0, 66, 90)
        #self.animation_droite.append(image)

        #image = feuille.decouper(0, 0, 66, 90)
        #image = pygame.transform.flip(image,True,False)
        #self.animation_gauche.append(image)

        #self.image = self.animation_droite[0]
        
        self.rect = self.image.get_rect()

        self.bloc = bloc_liste
        self.tous = tous_sprites_liste


    def gravite_newton(self):
        """Actualise la position du personnage
        lors d'un saut en fonction de la gravité"""
        
        g = 9.81
        pi = 3.14

        t = 0

        v_init = self.derive_x
        if self.derive_x ==0:
            angle_init = 0
        else:
            angle_init = pi/3

        v_x = cos(angle_init)*v_init
        v_y = sin(angle_init)*v_init

        position_relative_x = (int)(v_x*t);
        position_relative_y = (int)((v_y*t)-((g*t*t)/2000))

        self.rect.x = self.rect.x + position_relative_x
        self.rect.y = self.rect.y - position_relative_y

        t += 10
            
    def gravite(self):
        """effet de la force d'attraction gravitationnelle"""
        if self.newton == False:
            if self.derive_y == 0:
                self.derive_y = 1
            else:
                self.derive_y += .35

            #verifier si on a atteint un obstacle
            collision_liste = pygame.sprite.spritecollide(self, self.tous, False)
            for bloc in collision_liste:
                self.falling = False

    def aller_droite(self):
        self.derive_x = 6
        self.direction = "droite"
        
    def aller_gauche(self):
        self.derive_x = -6
        self.direction = "gauche"

    def stop(self):
        self.derive_x = 0
        
    def update(self):
        """deplace le joueur"""

        self.gravite()

        self.rect.x += self.derive_x

        collision_liste = pygame.sprite.spritecollide(self, self.tous, False)
        for bloc in collision_liste:
            # Si on se déplace vers la droite, 
            if self.derive_x > 0:
                self.rect.right = bloc.rect.left
            elif self.derive_x < 0:
                self.rect.left = bloc.rect.right

        self.rect.y += self.derive_y

        collision_liste = pygame.sprite.spritecollide(self, self.tous, False)
        for bloc in collision_liste:
            # Si on se déplace vers la droite, 
            if self.derive_y > 0:
                self.falling = True

            if self.derive_y > 0:
                self.rect.bottom = bloc.rect.top
            elif self.derive_y < 0:
                self.rect.top = bloc.rect.bottom

            self.derive_y = 0
            self.falling = False

        if self.rect.y == HAUTEUR-((self.rect.height)/2):
            self.derive_y = 0
            self.falling = False
