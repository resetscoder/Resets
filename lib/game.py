import sys #import des fonctions système
import os #import des fonctions os

import pygame #import de la biblioteque SDL: pygame
from pygame.locals import * #pour faciliter la lecture import des fonctions sans le pygame.*

from constantes import *
import levelmap
from player import *


class Game():

    # Listes des sprites
    bloc_liste = None
    tous_sprites_liste = None
    player = None


    def __init__(self,num_niveau,level):

        #création des listes de sprites
        self.bloc_liste = pygame.sprite.Group()
        self.tous_sprites_liste = pygame.sprite.Group()

        #ajout des sprites

        if level == False:
            niveau = levelmap.RGBlevelmap()
            niveau.bloc_level(self.bloc_liste,self.tous_sprites_liste)

        #creation du personnage
        self.player = Player(num_niveau,self.bloc_liste,self.tous_sprites_liste)
        self.tous_sprites_liste.add(self.player)

    def events(self):
        """teste les évenements à l'aide
        de la fonction event.get de pygame"""
        for event in pygame.event.get():                                #parcours la liste des evenements
            if event.type == QUIT:                                      #si bouton quitter :
                pygame.quit()                                           #sortir du jeu et du script
                sys.exit()
            if event.type == KEYDOWN:                                   #si une touche est enfoncée:
                if event.key == K_ESCAPE:                               #si bouton echap :
                    pygame.quit()                                       #sortir du jeu et du script
                    sys.exit()
                if event.key == K_SPACE:
                    if self.player.falling == False:
                        self.player.gravite_newton()
                if event.key == K_q:
                    self.player.aller_gauche()
                if event.key == K_d:
                    self.player.aller_droite()
                if event.key == K_q and event.key == K_LSHIFT:
                    self.player.aller_gauche()
                if event.key == K_d and event.key == K_LSHIFT:
                    self.player.aller_droite()

    def affichage(self, fenetre):
        self.player.update()

        fenetre.fill(( 0, 0, 0))

        self.tous_sprites_liste.draw(fenetre)

        pygame.display.flip()
