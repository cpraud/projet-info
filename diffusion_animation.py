# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 13:46:25 2017

@author: apelosse
"""
import numpy as np
import matplotlib.pyplot as plt
import random as rd
from pylab import *


# courbe initiale

def distribution_initiale_xenon(N,L):
    """
    Retourne la position des N particules présentes à l'état initial dans la matrice de taille NxN
    La distribution des position est aléatoire.
    Deux atomes peuvent être au même endroit.
    
    Exemple :
        
    >>> distribution_initiale_Xenon(2,10)
    [array([0, 5]), array([6, 2])]

    """
    n=[0]*N
    for i in range(N):
        n[i]=[randint(0,L-1),0,1] #modification de l'abscisse par rapport au code précédent
    return n
    


def affichage_initial(Xe):
    m_instant=np.zeros((L,L))
    
    for i in range(N):
        p=Xe[i]
        m_instant[p[0]][p[1]] =1
        
    plt.imshow(m_instant,cmap='Spectral')
    plt.show()

def desintegration(tau,k):
    '''fonction modélisant la desintegration  nucleaire à la kème étape. Retourne False
    si la particule n'est pas désintegrer, retourne True sinon'''
    p = random()
    return(p>np.exp(-np.log(2)*k/tau)) #modélisation de la loi de decroissance nucleaire

'''Code animation diffusion'''

# Paramètre
L=10                  #Taile de la matrice 
N=3                  #Nombres de particules initialement 
Nbre_Etapes=5      #Nombres d'instants dans l'expérience
tau1 = 5*np.log(2)
tau2 = 10*np.log(2)

#initialisation
ion() # mode interaction on
image=plt.figure()
Xe=distribution_initiale_xenon(N,L)
nb_particules=len(Xe)
m_instant=np.zeros((L,L)) #Matrice qui va indiquer la postion des particules       

                 
for t in range(Nbre_Etapes):
    p=rd.randint(0,nb_particules-1)
    (x,y,k)=Xe[p]
    if k!= None :
        if desintegration(tau1,k) : #desintegration en Cesium
            Xe[p].remove
            test = True
            nb_particules += -1
        elif desintegration(tau2,k) : #desintegration en Xenon stable
            Xe[p][2] = None
    if not test :
        (a,b)=(rd.random(),rd.random())
        if a<1./3 :               #Probabilité 1/3 de reculer de 1 selon x
            if x>0.:                #Vérification que la particule peut reculer, dans le cas contraire, elle ne bouge pas
                x-=1                              
        elif a>2./3 :             #Probabilité 1/3 d'avancer de 1 selon x
            if x<L-1:             #Vérification que la particule peut avancer, dans le cas contraire, elle ne bouge pas
                x+=1              #Pour a entre 1/3 et 2/3 on ne bouge pas selon x
        if b<1./3:                #Même process selon y
            if y>0.:
                y-=1
        elif b>2./3 :
            if y<L-1:
                y+=1
        if k != None :
            Xe[p]=[x,y,k+1]    #les coordonnées de la particule p sont mises à jours dans Xe
        else :
            Xe[p]=[x,y,k] 
    test = False
    m_instant=np.zeros((L,L))
    for i in range(nb_particules):  #on met à jour la matrice représentant les particules
        m_instant[Xe[i][0],Xe[i][1]] +=1    
    plt.imshow(m_instant,cmap='Spectral')
    plt.title('$Etape\,{}$'.format(t))
    draw() # force le dessin de la figure
    show()
    pause(0.001)

ioff() # mode interaction off

    
    
'''il y a un problème si il n'y a plus aucune particule'''
''' il faudrait pouvoir afficher les deux isotopes du Xenon avec 2couleurs differentes ! Plus facile pour tester si les codes fonctionnenent'''
    
    
    
