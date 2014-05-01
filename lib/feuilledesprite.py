#!/usr/bin/env python
# -*- coding: utf-8 -*-

#############
#--Imports--#
#############

import pygame


#############
#--Classes--#
#############

#inspiré par http://programarcadegames.com/python_examples/sprite_sheets/

class FeuilledeSprite():
    """ Permet de recuperer une image en particulier,
    dans une feuille de sprite de plusieures images"""
    feuille_de_sprite = None

    def __init__(self, nom_image):
        """ Constructeur """

        #Recupère la feuille de sprite
        self.feuille_de_sprite = pygame.image.load(nom_image).convert()

    def decouperImage(self, x, y, largeur_image, hauteur_image):
        """Découpe l'image désirée et la retourne
           prend en entrée les coordonnées et les dimensions
           du sprite désiré"""

        #crée une nouvelle surface
        image = pygame.Surface([largeur_image, hauteur_image]).convert()

        #Colle le sprite découpé sur la surface
        image.blit(self.feuille_de_sprite, (0, 0), (x, y, largeur_image, hauteur_image) )

        #Rend le noir transparent
        image.set_colorkey(BLACK)

        return image
