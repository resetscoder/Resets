import pygame
from pygame.locals import *

import sprites 
import tiles
import main

#######################################
#---Fonctions de creation de niveau---#
#######################################

def RGBlevelmap(num_niveau):
    #penser à l'arrière plan !
    del plateformes[:], ennemis[:]    												#effacer les anciens sprites
    img_niveau = pygame.image.load('Level_%s.png'%(num_niveau)).convert_alpha()		#recuper le tile
    for x in range(img_niveau.get_width()):											
        for y in range(img_niveau.get_height()):									#parcours du tile pixel par pixel
            color = img_niveau.get_at((x,y))										#recuperation de la couleur
            x = x*(largeur/img_niveau.get_width())
            y = y*(hauteur/img_niveau.get_heigh())
            if color == (,,,):
                Plateform('0_level%s.png'%(num_niveau),x,y)
            if color == (,,,):
                Plateform('1_level%s.png'%(num_niveau),x,y)
            #etc...
