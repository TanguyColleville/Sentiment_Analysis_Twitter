# Partie Base de donn�e du projet 

Oscar Vogler

## Introduction 
Le stockage des tweets dans une base de donn�es r�pond � 2 besoins :
    - Avoir suffisament de donn�es  pour entrainer le mod�le de d�termination des sentiments
    - Permettre le filtrage des requ�tes par nom d'utilisateur, mot cl�, date et methode 


## Structure 

- Bdd 
- |--gestion_bdd.py
- |--acces_bdd.py
- |--test_acces_bdd.py
- |--test_gestion_bdd.py

La gestion de la base de donn�e a �t� r�partie entre 2 modules : 
    - acces_bdd permettant de cr�er la base de donn�e ainsi que la table associ�e aux donn�es des tweets aisni que d'ajouter les donn�es dans cette table � partir d'un dataframe
    - gestion_bdd permettant de retourner un dataframe pandas en fonction de la requete qui peut prendre plusieurs arguments :
    une chaine de caract�re avec un ou plusieurs mots cl�s s�par�s par OR ou AND et/ou un nom d'utilisateur, la date et la m�thode (tweet,retweet,r�ponse � un tweet)

## Impl�mentation et probl�mes renconntr�s :

gestion_bdd cr�� la bdd ainsi que la table. Il a fallu inclure dans la fonction ajout_tweet la gestion de l'erreur qui survenait
lorsqu'on essayait de rajouter un tweet dans la base de donn�e qui �tait d�j� pr�sent (car l'ID qui est la cl� primaire doit �tre unique)
car cela bloquait l'�criture des tweets d'apr�s.
La fonction req_tweet utilis�e pour renvoyer le dataframe correspondant � la req�te � d'abord �t� impl�ment� en cr�ant des dataFrame correspondant
� chaque requ�te puis en r�cup�rant l'intersection ou l'union de ces dataframes. Lorsque le nombre de filtre est devenu
trop important et pour all�ger le nombre de requ�tes r�alis�es � la base de donn�e (pour acc�l�rer la fonction), la fonction req_tweet
� �t� modifi�e pour cr�er une seule requ�te sous forme de chaine de caract�res modulable en fonction des param�tres d'entr�e. 
La date des tweets est ensuite compar�e � l'aide de la fonction compare_date.
        

## Conclusion et perspectives de developpement 
La base de donn�e remplie les objectifs qui lui ont �t� fix�s.
D'autres fonctionnalit�s peuvent encore �tre rajout�es pour notamment prendre en charge des mts cl�s avec des OR et des AND, 
pour avoir une comparaison de date plus fine, pour ne retourner qu'un certain nombre de tweets, ...