# PYTHON::Plus court chemin//Application au metro parisien
 Implémentation de l'algorithme de Dijkstra 


Vous trouverez dans le fichier metro_complet.txt un graphe construit de la façon suivante : 
- Chaque sommet correspond à une station pour une ligne donnée (par exemple, République [ligne 3] et République [ligne 5] sont deux sommets différents). 
- A chaque sommet est associé la position de la station sur une carte (échelle : 1~25.7m). 
- A chaque sommet est associé le nom de la station (chaîne de caractères). 
-   Deux sommets forment un arc orienté si le métro relie directement les stations correspondantes
 (le graphe n'est pas symétrique à cause de quelques "sens uniques", par exemple du côté de la porte d'Auteuil).
 Cet arc est valué par le temps estimé du trajet en secondes (en prenant pour base une vitesse moyenne de 10m/s, soit 36km/h). 
- Deux sommets forment deux arcs symétriques l'un de l'autre s'il est possible de passer à pied sans changer de billet entre les stations correspondantes.
 Ces arcs sont alors valués par une estimation du temps moyen de trajet et d'attente (120s). 


========>>>>>>Implémentation de l'algorithme de Dijkstra pour calculer le plus court chemin 






------------By Aymen HMAM---------------------------------------