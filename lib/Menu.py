#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from constantes import *
from main import *

class Menu():
    """Crée un menu de demarrage avec le choix des niveaux,
        les credits, peut-être des paramètres ..."""  
    
    def __init__(self):
        #Ouvrir une fenêtre
        self.fenetre = pygame.display.set_mode((LARGEUR,HAUTEUR),FULLSCREEN, 32)
        pygame.display.set_caption("Resets")

        #creation d'une police:
        self.police = pygame.font.Font(os.path.join(DOSSIER_DATA,"Dosis-Medium.ttf"), 60)

        #Chargement et affichage de la fenêtre et de l'icône
        self.accueil = pygame.image.load(os.path.join(DOSSIER_DATA,"accueil.png")).convert()

        self.logo = pygame.image.load(os.path.join(DOSSIER_DATA,"logo.png")).convert_alpha()

        #numero de la ligne du menu selectionnée
        self.menuligne = 1

        self.time = 1
        self.transition = False
        
    def texte(self,texte,couleur):
        """crée un texte avec une couleur définie"""
        return self.police.render(texte, 1, couleur)

    def nouveaumenu(self,couleur):
        #création de "Nouvelle Partie"
        nouveau = self.texte("Nouvelle Partie",couleur)
        nouveau_pos = nouveau.get_rect()
        nouveau_pos.x = self.fenetre.get_rect().centerx
        nouveau_pos.y = self.fenetre.get_rect().centery
        self.fenetre.blit(nouveau, nouveau_pos)

    def chargerpartie(self,couleur):
        #création de "Charger une partie"
        charger = self.texte("Charger une partie",couleur)
        charger_pos = charger.get_rect()
        charger_pos.x = self.fenetre.get_rect().centerx
        charger_pos.y = self.fenetre.get_rect().centery + 100
        self.fenetre.blit(charger, charger_pos)

    def quitterpartie(self,couleur):
        #création de "Quitter"
        quitter = self.texte("Quitter",couleur)
        quitter_pos = quitter.get_rect()
        quitter_pos.x = self.fenetre.get_rect().centerx
        quitter_pos.y = self.fenetre.get_rect().centery + 200
        self.fenetre.blit(quitter, quitter_pos)

    def evenementsmenu(self):
        for event in pygame.event.get():
            if event.type == QUIT:                                      #si bouton quitter :
                pygame.quit()                                           #sortir du jeu et du script
                sys.exit()

            if event.type == KEYDOWN:                                   #si une touche est enfoncée:
                if event.key == K_RETURN and self.menuligne == 3:       #si cliquer sur quitter :
                    pygame.quit()                                       #sortir du jeu et du script
                    sys.exit()
                if event.key == K_RETURN and self.menuligne == 1:
                    self.transition = True
            #déplacement dans le menu
                if event.key == K_DOWN:
                    self.menuligne += 1 
                if event.key == K_UP:
                    self.menuligne -= 1


    def bouclemenu(self):
        
        
        #ajouter la fonction redimmension ici <-- 
        self.fenetre.blit(self.accueil,(0,0))

        self.fenetre.blit(self.logo,(self.fenetre.get_rect().centerx - (self.logo.get_rect().width)/2,50))

        self.evenementsmenu()
        if self.menuligne == 4 or self.menuligne <= 0:
            self.menuligne = 1
            
        self.nouveaumenu(BLANC)
        self.chargerpartie(BLANC)
        self.quitterpartie(BLANC)
        
        if self.menuligne == 1:
            self.nouveaumenu(ROUGE)
        elif self.menuligne == 2:
            self.chargerpartie(ROUGE)
        elif self.menuligne == 3:
            self.quitterpartie(ROUGE)

        if self.transition == True:
            self.fenetre.blit(self.accueil,(0,0))
            self.logo = pygame.transform.smoothscale(self.logo, (int(511*self.time),int(142*self.time)))
            self.fenetre.blit(self.logo,(self.fenetre.get_rect().centerx - (self.logo.get_rect().width)/2,50))
            self.time += .1
            if self.time > 4:
                self.time = 1
                self.transition = False
                self.logo = pygame.image.load(os.path.join(DOSSIER_DATA,"logo.png")).convert_alpha()
                resets()
                

        #Rafraichissement
        pygame.time.Clock().tick(60)
        pygame.display.flip()

def main():
    menu = Menu()
    while 1:
        menu.bouclemenu()
        
if __name__ == '__main__':
    main()



        
    
    
