# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 09:27:06 2020

@author: HMAM Aymen 
"""

import numpy as TAB
import re


 
dataset = open("metro_complet.txt", "r")
line_dataset = dataset.readlines()
list_arcs_graphe = []
dataset.close()
#________________________________extraction les arcs de notre graphe de fichier .txt ___________________________ 
#________________________________Remarque: les arcs sont stockés dans des tuples ___________________________ 
def Extraction_ARCs_graphe():   
    
    #Creating our dictionary by loading our dataset (.txt)
    for i in range(len(line_dataset) - 1): 
        if not re.match(r'([\d]+)', line_dataset[i]):
            line_temp = i

    for i in range(line_temp + 1, len(line_dataset) - 1):#xrange
        list_arcs_graphe.append((int(line_dataset[i].strip().split(" ")[0]), int(line_dataset[i].strip().split(" ")[1]),
                                     float(line_dataset[i].strip().split(" ")[2])))
#______________________________________________________________________________________________________
        
     
#________________________________extraction les dictionnaires des noms de sommets de graphe _____________________ 
def Dictionnaire_des_stations():
    # local variable for our dataset
    sourceFileName = 'metro_complet.txt'
    f = open(sourceFileName, 'r')
    my_l = []
    Dictionnaire_des_stations = {}
    for unit in f.readlines()[1:]:
        if unit.strip() != '[Edges]':
            

            my_l.append(unit[5:])
        else:
            break
    for i in range(len(my_l)):
        Dictionnaire_des_stations[i-1] = my_l[i]

    return Dictionnaire_des_stations            
#___________________________________________________________________________________________________________        
        

#________________________________création de la matrice d'ajscence ___________________________           
def Calcul_Matrix_Adjscence(): 
    nb_sommet=int(line_dataset[0][0:3])
    Matrice_adj=TAB.zeros((nb_sommet,nb_sommet))
    n=len(list_arcs_graphe)
    
    for i in range(0,n):
        Matrice_adj[list_arcs_graphe[i][0]][list_arcs_graphe[i][1]]=list_arcs_graphe[i][2]
    
    return (Matrice_adj)

#______________________________________________________________________________________________     

def ligneInit(Graphe,depart) :
    """ Renvoie la première ligne du tableau """
    L = []
    # nombre de lignes de Graphe donc nombre de sommets
    n = len(Graphe)
    for j in range(n) :
        poids = Graphe[depart][j]
        if poids :
            # si l’arête est présente
            L.append([ poids, depart ])
        else :
            L.append(False)
    return (L)

def SommetSuivant(T, S_marques) :
    """ En considérant un tableau et un ensemble de sommets marqués,
    détermine le prochain sommet marqué. """
    L = T[-1]
    n = len(L)
    # minimum des longueurs, initialisation
    min = False
    for i in range(n) :
        if not(i in S_marques) :
            # si le sommet d’indice i n’est pas marqué
            if L[i]:
                if not(min) or L[i][0] < min :
                    # on trouve un nouveau minimum
                    # ou si le minimum n’est pas défini
                    min = L[i][0]
                    marque = i
                   
    return(marque)

def ajout_ligne(T,S_marques,Graphe) :
    """ Ajoute une ligne supplémentaire au tableau """
    L = T[-1]
    n = len(L)
    # La prochaine ligne est une copie de la précédente,
    # dont on va modifier quelques valeurs.
    Lnew = L.copy()
    # sommet dont on va étudier les voisins
    S = S_marques[-1]
    # la longueur du (plus court) chemin associé
    long = L[S][0]
    for j in range(n) :
        if j not in S_marques:
            poids = Graphe[S][j]
            if poids :
                # si l’arète (S,j) est présente
                if not(L[j]) : # L[j] = False
                    Lnew[j] = [ long + poids, S ]
                else :
                    if long + poids < L[j][0] :
                        Lnew[j] = [ long + poids, S ]
    T.append(Lnew)
    # Calcul du prochain sommet marqué
    S_marques.append(SommetSuivant(T, S_marques))
    return T, S_marques   

    
def calcule_tableau(Graphe, depart) :
    """ Calcule le tableau de l’algorithme de Dijkstra """
    n = len(Graphe)
        # Initialisation de la première ligne du tableau
        # Avec ces valeurs, le premier appel à ajout_ligne
        # fera le vrai travail d’initialisation
    T=[[False] *n]
    T[0][depart] = [depart, 0]

    # liste de sommets marques
    S_marques = [ depart ]
    while len(S_marques) < n :
        T, S_marques = ajout_ligne(T, S_marques, Graphe)
    return T

def plus_court_chemin(Graphe, depart, arrivee) :
    """ Détermine le plus court chemin entre depart et arrivee dans le Graphe"""
   
    # calcul du tableau de Dijkstra
    T = calcule_tableau (Graphe,depart)
    # liste qui contiendra le chemin le plus court, on place l’arrivée
    C = [ arrivee ]
    while C[-1] != depart :
        C.append( T[-1][ C[-1] ][1] )
        # Renverse C, pour qu’elle soit plus lisible
    C.reverse()
    return C  

#__________________Calculer la durée de trajet en format HH:MM:SS __________________
def calcul_duree_chemin(liste,Matrix):
    s=0
    for i in range(0,len(liste)-1):
        s=s+Matrix[liste[i]][liste[i+1]]
    
    hh=int((s//60)//60)
    mm=int(((s-hh*3600)//60 ))
    ss=int((s-hh*60)%60)
    return(hh,mm,ss)  
#____________________________________________________________________________________________          
    

        
if __name__ == "__main__":
    
    
    Extraction_ARCs_graphe()
    Matrice_adj=Calcul_Matrix_Adjscence()
    Dictionnaire_des_stations=Dictionnaire_des_stations()
    station_depart=int(input("Taper la reference de station de depart: "))
    station_arrivé=int(input("Taper la reference de station d'arrivé: "))
    Nom_SD=Dictionnaire_des_stations[station_depart]
    Nom_SA=Dictionnaire_des_stations[station_arrivé]
    print('\n')
    L=plus_court_chemin(Matrice_adj, station_depart, station_arrivé) 
    duree=calcul_duree_chemin(L,Matrice_adj)
   
  
      
    print('====> Votre plus court chemin\n est la suivante: ',L)
    print('\n')
    print('---------------------------------------------------------------')
    print('Station départ: {}'.format(Nom_SD))
   
    n=len(L)
    for i in range(1,n-1):
        print('Station N°[{}]: {}'.format(i,Dictionnaire_des_stations[L[i]]))   
    print('Station d\'arrivée: {}'.format(Nom_SA))
    print('---------------------------------------------------------------')
    
    print('le trajet a pour durée: {} HH:{} MM:{} SS'.format(duree[0],duree[1],duree[2]))
      
  
 
 
    
