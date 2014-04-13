import sys #import des fonctions système
import os #import des fonctions os

import pygame #import de la biblioteque SDL: pygame
from pygame.locals import * #pour faciliter la lecture import des fonctions sans le pygame.*


DOSSIER_COURRANT = os.path.dirname(os.path.realpath(__file__)) #recupère le chemin courant
DOSSIER_DATA = os.path.join(os.path.dirname(DOSSIER_COURRANT), 'data')#recupere le dossier parent et le join a data
sys.path.append(DOSSIER_DATA) #ajoute le dossier data au python path

pygame.init()
info_ecran = pygame.display.Info()
LARGEUR = info_ecran.current_w
HAUTEUR = info_ecran.current_h
