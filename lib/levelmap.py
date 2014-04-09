import pygame
from pygame.locals import *

import sprites
import tiles

#######################################
#---Fonctions de creation de niveau---#
#######################################

def RGBlevelmap(num_niveau):
    #penser à l'arrière plan !
    #del bloc_liste[:], tous_sprites_liste[:]    												#effacer les anciens sprites
    img_niveau = pygame.image.load('Level_%s.png'%(num_niveau))		#recuper le tile
    for x in range(img_niveau.get_width()):
        for y in range(img_niveau.get_height()):									#parcours du tile pixel par pixel
            color = img_niveau.get_at((x,y))										#recuperation de la couleur
            x = x*(largeur/img_niveau.get_width())
            y = y*(hauteur/img_niveau.get_heigh())
            tile = affiliation_tile[str(color)]
            image = 'image1_' + tile + '.png'
            Bloc(image,x,y)
            #etc...
