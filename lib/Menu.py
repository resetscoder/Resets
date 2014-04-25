#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from constantes import *


#Ouvrir une fenêtre
fenetre = pygame.display.set_mode((LARGEUR,HAUTEUR))

pygame.display.set_caption("Resets")

continuer = 1
while continuer :
    #Chargement et affichage de la fenêtre et de l'icône
    accueil = pygame.image.load("accueil.png").convert()
    fenetre.blit(accueil,(0,0))

    new = pygame.font.Font(None, 60)
    text = new.render("Nouvelle partie", 1, (0, 0, 0))
    textpos = text.get_rect()
    textpos.x = fenetre.get_rect().centerx
    textpos.y = fenetre.get_rect().centery
    fenetre.blit(text, textpos)

    load = pygame.font.Font(None, 60)
    text0 = load.render("Charger une partie", 1, (0, 0, 0))
    text0pos = text0.get_rect()
    text0pos.x = fenetre.get_rect().centerx
    text0pos.y = fenetre.get_rect().centery + 100
    fenetre.blit(text0, text0pos)
    
    
    #Rafraichissement
    pygame.display.flip()
    
    #Remettre variables à  1
    continuer_accueil = 1
    continuer_jeu = 1
    
    
    #Boucle d'accueil
    while continuer_accueil == 1:
        pygame.time.Clock().tick(30)
        
        #Variable de choix de niveaux
        level = 0
    
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == pygame.K_ESCAPE:
                continuer = 0
                continuer_accueil = 0
                continuer_jeu = 0
        
            #déplacement dans le menu
            if event.type == KEYDOWN:
                if event.key == K_DOWN:
                    level += 1 
                if event.key == K_UP:
                    level -= 1


        
    
    
