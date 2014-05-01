#!/usr/bin/env python
# -*- coding: utf-8 -*-

#############
#--Imports--#
#############

import os
import sys

from constantes import *
from feuilledesprite import *
from math import cos
from math import sin
from redimension import *

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
    position_relative_x = 0
    position_relative_y = 0

    #liste donctenant les differentes positions de l'image du player
    animation_gauche = []
    animation_droite = []

    #direction dans laquelle va le joueur
    direction = 'droite'

    #nombre de pixel dont le niveau s'est déplacé
    scrolling = 0

    newton = False

    t = 1

    def __init__(self,num_niveau,bloc_liste,tous_sprites_liste):
        """Construction"""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(DOSSIER_DATA,'image1_1.png')).convert_alpha()
        self.image = redimensionnement(self.image, LARGEUR, HAUTEUR)

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

    def loi_newton(self):
        """Actualise la position du personnage
        lors d'un saut en fonction de la gravité
        non fonctionelle pour l'instant"""
        #constantes physiques
        g = 9.81
        pi = 3.14
        
        #constantes d'intégration
        v_init = self.derive_x
        if self.derive_x == 0:
            angle_init = 0
        else:
            angle_init = pi/3 #A VOIR : gestion de l'angle fonction de v_init

        v_x = cos(angle_init)*v_init
        v_y = abs(sin(angle_init)*v_init)

        #Integration 
        self.position_relative_x = int(v_x*self.t);
        self.position_relative_y = -int(v_y*self.t-(g*self.t*self.t/2000))*2

        #avancement du temps
        self.t += 10

    def saut(self):

        self.rect.y += 2
        collision_liste = pygame.sprite.spritecollide(self, self.bloc, False)
        self.rect.y -= 2

        if len(collision_liste) > 0 or self.rect.bottom >= HAUTEUR:
            self.derive_y = -10/5
            
    def gravite(self):
        """effet de la force d'attraction gravitationnelle"""
        if self.newton == False:
            if self.derive_y == 0:
                self.derive_y = 1/20
            else:
                self.derive_y += 0.35/20


            if self.rect.bottom >= HAUTEUR and self.derive_y >= 0:
                self.derive_y = 0
                self.rect.bottom = HAUTEUR
                self.t = 1
                
    def aller_droite(self):
        self.derive_x = 1
        self.direction = "droite"
        
    def aller_gauche(self):
        self.derive_x = -1
        self.direction = "gauche"

    def stop(self):
        self.derive_x = 0
        
    def update(self):
        """deplace le joueur"""

        self.gravite()

        self.rect.x += self.derive_x
        self.rect.x += self.position_relative_x

        collision_liste = pygame.sprite.spritecollide(self, self.bloc, False)
        for bloc in collision_liste:
            # Si on se déplace vers la droite, 
            if self.derive_x > 0:
                self.rect.right = bloc.rect.left
            elif self.derive_x < 0:
                self.rect.left = bloc.rect.right

        self.rect.y += self.derive_y
        self.rect.y += self.position_relative_y

        collision_liste = pygame.sprite.spritecollide(self, self.bloc, False)
        for bloc in collision_liste:
            if self.derive_y > 0:
                self.rect.bottom = bloc.rect.top
            elif self.derive_y < 0:
                self.rect.top = bloc.rect.bottom

            self.derive_y = 0
            self.t = 1
            self.newton = False
