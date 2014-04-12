import pygame
from pygame.locals import *

import sprites
import tiles

#######################################
#---Fonctions de creation de niveau---#
#######################################


class RGBlevelmap():

    #penser à l'arrière plan !
    #del bloc_liste[:], tous_sprites_liste[:]
    #effacer les anciens sprites
    
    def __init__(self):
        
        self.affiliation_tile = {'(51, 204, 51, 255)': '0','(1,1,1,1)': '1'}
        self.img_niveau = pygame.image.load('Level_%s.png'%('1'))

    def bloc_level(self,LARGEUR,HAUTEUR,bloc_liste,tous_sprites_liste):
        width = self.img_niveau.get_width()
        height = self.img_niveau.get_height()
        for x in range(width):
            for y in range(height):                        #parcours du tile pixel par pixel
                color = self.img_niveau.get_at((x,y))										#recuperation de la couleur
                X = x*(1300/width)
                Y = y*(560/height)
                if not color == (0,0,0,255):
                    tile = self.affiliation_tile[str(color)]
                    image = 'image1_' + tile + '.png'
                    bloc = sprites.Bloc(image,X,Y)
                    bloc_liste.add(bloc)
                    tous_sprites_liste.add(bloc)
                #etc...
        
