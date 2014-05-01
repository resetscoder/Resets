#!/usr/bin/env python
# -*- coding: utf-8 -*-

#############
#--Imports--#
#############

import pygame
from pygame.locals import *
from constantes import *
from redimension import *

#####################################
#--Fonctions de création de sprite--#
#####################################

class Bloc(pygame.sprite.Sprite):
    """Création d'un sprite plateforme"""

    def __init__(self, image, x, y):
        """Construction"""
        
        #Initialise le module Sprite
        pygame.sprite.Sprite.__init__(self)

        #Charge l'image
        self.image = pygame.image.load(image).convert_alpha()
        self.image = redimensionnement(self.image, LARGEUR, HAUTEUR)

        #Affilie l'image a un rect
        self.rect = self.image.get_rect()
        
        #Le positionne sur l'écran
        self.rect.x = x
        self.rect.y = y

