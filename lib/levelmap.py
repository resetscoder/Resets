#!/usr/bin/env python
# -*- coding: utf-8 -*-

#############
#--Imports--#
#############

import os
import sys

import pygame
from pygame.locals import *

from constantes import *
import sprites
from tiles import *


####################################
#---Classe de création de niveau---#
####################################


class RGBlevelmap():
    """dessine un niveau à partir d'un tile
    c'est à dire une image dont un pixel de couleur
    equivaut à une image affiliée à la couleur"""
    
    def __init__(self):
        """Charge l'image du niveau et le dictionnaire d'affiliation"""
        self.affiliation_tile = affiliation_tile
        self.ennemies = ennemies
        self.img_niveau = pygame.image.load(os.path.join(DOSSIER_DATA,('Level_%s.png'%('1'))))

    def bloc_level(self,bloc_liste,ennemies_liste,tous_sprites_liste):
        """Parcours le tile et charge les sprites"""

        width = self.img_niveau.get_width()
        height = self.img_niveau.get_height()
        
        #parcours du tile pixel par pixel
        for x in range(width):
            for y in range(height):
                
                #recuperation de la couleur
                color = self.img_niveau.get_at((x,y))       

                facteur = HAUTEUR/height
                X = x*facteur
                Y = y*facteur
                
                if not color == (0,0,0,255):
                    tile = self.affiliation_tile[str(color)]

                    image = 'image1_' + tile + '.png'
                    bloc = sprites.Bloc(os.path.join(DOSSIER_DATA,image),X,Y)
                    
                    if color in self.ennemies:
                        ennemies_liste.add(bloc)
                    else:
                        bloc_liste.add(bloc)
                    
                    tous_sprites_liste.add(bloc)
        
