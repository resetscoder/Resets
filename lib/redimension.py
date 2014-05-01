#!/usr/bin/env python
# -*- coding: utf-8 -*-

#############
#--Imports--#
#############

import pygame
from pygame.locals import *
from constantes import *

def redimensionnement(image, largeur, hauteur):
    width, height = image.get_size()
    facteur_largeur = largeur/1366
    facteur_hauteur = hauteur/768
    return pygame.transform.smoothscale(image, (int(facteur_largeur*width), int(height*facteur_hauteur)))
    
