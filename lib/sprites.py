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

    def __init__(self, image, x, y, width, height):
        """Construction"""
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(image).convert_alpha()
        self.image = redimensionnement(self.image, LARGEUR, HAUTEUR)

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

