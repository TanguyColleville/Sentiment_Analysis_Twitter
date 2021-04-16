# Interface Graphique 

## Réalisé par

Ghislain Flichy 

## Utilisation 

- Lancer le fichier app.py 
- Dans un navigateur internet se rendre à l'adresse : http://127.0.0.1:8050

## Fonctionnement : 

Le fichier est structuré en trois parties principales : 
- la première contient les modules présents dans l'interfaces graphiques et leurs caractéristiques (Position, taille, et autre attributs spécifiques .. ).
- La seconde mais en ordre l'affichage des différents modules sur la page Web.
- La dernière partie contient les fonctions qui permet d'actualiser les propriétés des différents objets en fonction des interactions de l'utilisateur avec la page Web. Ses fonctions sont précédé d'un callback qui définit les inputs et les outputs à mettre à jour actualiser. Un callback est associé à une fonction qui est directement écrite après celui-ci. Cette fonction prends en entrée (et dans le même ordre) les éléments des inputs et renvoie les éléments des Outputs dans le même ordre que celui précisé dans le callback.

Les callback permettent en autre de masquer ou non des graphiques en focntion de l'entrée de l'utilisateur et de la possibilité de traiter avec l'IA les données. Par exemple si un DataFrame ne contient pas la colonne sentiment_IA parce qu'il n'y a pas assez de tweets pour l'analiser, alors on renvoit un gtaphique vide (on ne peut pas renvoyer un objet différent qu'un graphique) et l'information disabled pour son contenant html.Div pour le masquer.  

Le callback permet également de lancer un compteur lorsque l'utilisateur selectionne l'onglet streaming pour incrementer la màj du graphique et l'appel du thread streaming dans StreamTwitt. 
Le callback pour mettre à jour le graphique du streaming est appelé toute les 4 secondes et le thread de streaming dure 2 secondes pour synchroniser les deux.

Le fichier Nltk.txt et Prockfile permettent la mise en ligne sur l'interface Heroku.
Nous avons pu mettre en ligne notre application jusqu'à l'implémentation du streaming qui à nécessité un base de donnée rapidement trop importante pour le serveur en version gratuite. 

## Améliorations

-  Il serait judicieux de travailler sur la mise en place de deux thread parallèle en sachant que toute l'interface dash doit se trouver dans un unique thread. 
- Il faut masquer les options qui ne doivent pas être disponible dans le streaming (utilisateurs et méthodes). 
