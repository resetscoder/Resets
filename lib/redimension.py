#!/usr/bin/env python
# -*- coding: utf-8 -*-

#############
#--Imports--#
#############

import pygame
from pygame.locals import *
from constantes import *

##############################
#--Fonction de redimmension--#
##############################

def redimensionnement(image, largeur, hauteur):
    """toutes les textures ou images sont construites 
    pour une resolution de 1366*768, retourne l'image 
    redimensionnée pour la resolution d'écran de l'ordinateur"""
    
    #Recupere les dimmensions de l'image
    width, height = image.get_size()
    
    #Calcule les facteur d'homothetie
    facteur_largeur = largeur/1366
    facteur_hauteur = hauteur/768
    
    #retourne l'image redimmensionnée
    return pygame.transform.smoothscale(image, (int(facteur_largeur*width), int(height*facteur_hauteur)))
    
