import pygame
from pygame.locals import *

import sprites
import tiles

#######################################
#---Fonctions de creation de niveau---#
#######################################

def RGBlevelmap(num_niveau):
    #penser à l'arrière plan !
    #del bloc_liste[:], tous_sprites_liste[:]
    #effacer les anciens sprites

    affiliation_tile = {'(51, 204, 51, 255)': '0','(1,1,1,1)': '1'}
    
    info_ecran = pygame.display.Info()
    LARGEUR = info_ecran.current_w
    HAUTEUR = info_ecran.current_h

    img_niveau = pygame.image.load('Level_%s.png'%(num_niveau))		#recuper le tile
    for x in range(img_niveau.get_width()):
        for y in range(img_niveau.get_height()):                        #parcours du tile pixel par pixel
            color = img_niveau.get_at((x,y))										#recuperation de la couleur
            X = x*(1300/img_niveau.get_width())
            Y = y*(560/img_niveau.get_height())
            if not color == (0,0,0,255):
                tile = affiliation_tile[str(color)]
                image = 'image1_' + tile + '.png'
                sprites.Bloc(image,X,Y)
            #etc...
