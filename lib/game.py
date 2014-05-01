#!/usr/bin/env python
# -*- coding: utf-8 -*-

#############
#--Imports--#
#############

import sys #import des fonctions système
import os #import des fonctions os

import pygame #import de la biblioteque SDL: pygame
from pygame.locals import * #pour faciliter la lecture import des fonctions sans le pygame.*

from constantes import *
import levelmap
from player import *
import Menu


#############
#--Classes--#
#############

class Game():

    # Listes des sprites
    bloc_liste = None
    ennemies_liste = None
    tous_sprites_liste = None
    player = None
    retourmenu = False
    
    def __init__(self,num_niveau):

        #création des listes de sprites
        self.bloc_liste = pygame.sprite.Group()
        self.tous_sprites_liste = pygame.sprite.Group()
        self.ennemies_liste = pygame.sprite.Group()

        #ajout des sprites

        niveau = levelmap.RGBlevelmap()
        niveau.bloc_level(self.bloc_liste,self.ennemies_liste,self.tous_sprites_liste)

        #creation du personnage
        self.player = Player(num_niveau,self.bloc_liste,self.tous_sprites_liste)
        self.player.rect.x = 95
        self.player.rect.y = HAUTEUR - self.player.rect.height
        self.tous_sprites_liste.add(self.player)

    def events(self):
        """teste les évenements à l'aide
        de la fonction event.get de pygame"""
        for event in pygame.event.get():                                #parcours la liste des evenements

            if event.type == QUIT:                                      #si bouton quitter :
                pygame.quit()                                           #sortir du jeu et du script
                sys.exit()

            if event.type == KEYDOWN:                                   #si une touche est enfoncée:                                                                           #si une touche est enfoncée:
                if event.key == K_ESCAPE:                               #si bouton echap :
                    self.retourmenu = True
                if event.key == K_SPACE:
                    self.player.saut()
                if event.key == K_a:
                    self.player.aller_gauche()
                if event.key == K_d:
                    self.player.aller_droite()
                if event.key == K_a and event.key == K_LSHIFT:
                    self.player.aller_gauche()
                if event.key == K_d and event.key == K_LSHIFT:
                    self.player.aller_droite()

            if event.type == KEYUP:
                if event.key == K_a:
                    self.player.stop()
                if event.key == K_d:
                    self.player.stop()

    def scroll_niveau(self, deplacement):
        """En developpement,
            ajouter une limite definie pour le niveau
            pour ne pas scroller a l'infini """
        for sprites in self.bloc_liste:
            sprites.rect.x += deplacement
    
    def scrolling(self):
        """En developpement"""
        # si le joueur va du coté droit:
        lim = int(LARGEUR*(2/3))
        if self.player.rect.x >= lim:
            difference = self.player.rect.x - lim
            self.player.rect.x = lim
            self.scroll_niveau(-difference)
    
        # si le joueur va du coté gauche
        lim1 = int(LARGEUR*(1/6))
        if self.player.rect.x <= lim1:
            difference = lim1 - self.player.rect.x
            self.player.rect.x = lim1
            self.scroll_niveau(difference)
    

    def affichage(self, fenetre):
        self.player.update()

        self.scrolling()

        fenetre.fill(( 0, 0, 0))

        self.tous_sprites_liste.draw(fenetre)

        pygame.display.flip()
