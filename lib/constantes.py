import sys #import des fonctions système
import os #import des fonctions os

DOSSIER_COURRANT = os.path.dirname(os.path.realpath(__file__)) #recupère le chemin courant
DOSSIER_DATA = os.path.join(os.path.dirname(DOSSIER_COURRANT), 'data')#recupere le dossier parent et le join a data
sys.path.append(DOSSIER_DATA) #ajoute le dossier data au python path
