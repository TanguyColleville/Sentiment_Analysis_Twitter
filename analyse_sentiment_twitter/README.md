# Projet TweetFeeling

## Introduction : 

Ce projet a pour but de produire une interface visuelle permettant de choisir : un compte twitter, des mots-clés contenus dans le tweet et de produire une analyse graphique des sentiments qui en ressortent.
L'idée est d'utiliser le machine learning pour analyser le plus finement possible les sentiments. On cherchera à y associer des mots pour produire un nuage de mots.
Le programme s'utilise via une interface graphique utilisateur simple sur le web.

## Membres de l'équipe :

- Tanguy Colleville : tanguy.colleville@student-cs.fr
- Oscar Vogler : oscar.vogler@student-cs.fr
- Louis Moser : louis.moser@student-cs.fr
- Ghislain Flichy : ghislain.flichy@student-cs.fr

## Vidéos de démonstration 

https://drive.google.com/file/d/1b4JUPx7yr0vL6FZ_WDmffCK0C_kZB1Hx/view?usp=sharing

https://drive.google.com/file/d/13CsEMX4uEfVEXMa7z0ZW7zSMaWjNKcax/view?usp=sharing

## Instruction pour l'installation

On commence, pour travailler sur le projet ou le tester, par créer une copie locale avec " git clone https://gitlab-cw2.centralesupelec.fr/ghislain.flichy/analyse_sentiment_twitter.git".
Ensuite, afin d'importer les modules nécessaires pour faire fonctionner correctement les programmes, il faut, dans une console Python, taper la requête " pip install -r requirements.txt " et simplement appuyer sur "entrée".
Parmi les modules installés, on a, notamment, les versions : 3.9.0 de tweepy, 6.1.2 de pytest et 0.15.3 de textblob.

## Utilisation : 

Le projet se trouve à cette adresse en public : https://dash-app-tweetfeeling.herokuapp.com/. Son utilisation est rendue ludique par la mise en forme même de cette interface. Si la version en ligne n'est pas disponible, un problème de serveur a pu être rencontré. C'est pourquoi il vous est également rendu possible d'utiliser le projet en local. Pour se faire, 
1. Ouvrir le programme app.py et lancer le. 
2. Ouvrir votre navigateur et taper :  http://127.0.0.1:8050/ 
3. Enjoy
Par ailleurs vous trouverez un mode d'emploi en pdf. 

## Liens pour la construction du projet :

- Lien vers le projet en ligne : https://dash-app-tweetfeeling.herokuapp.com/
- Lien vers le Miro pour suivre l'évolution du projet en interne :  https://miro.com/welcomeonboard/fExNozY2WVZLy9lZVWI4cLFbdnMbyC8GMWx2ynJTTQyOZuuKVBMpklPDQg8JK1BZ
- Lien vers le Miro de présentation de la structure de notre projet : https://miro.com/app/board/o9J_leGQZPk=/
- Lien du canal Teams : https://teams.microsoft.com/l/channel/19%3a7b531f03cf1248beadf7b0f9b2128cfd%40thread.tacv2/CW31%2520-%2520Groupe%252018?groupId=fa476ef7-f6fa-463c-837a-879c84aaa838&tenantId=61f3e3b8-9b52-433a-a4eb-c67334ce54d5

## Solution envisagée 

L'architecture du projet est détaillée sur Miro. Nous sommes partis sur une séance de création afin d'obtenir une première ébauche du résultat final que nous souhaiterions obtenir. Nous avons ainsi pu définir plusieurs entités dans le projet et spécifier les besoins de chaque partie. On notera que les parties en pointillée sont des améliorations possibles du MVP.
- API : Dans cette partie nous allons utiliser l'API de Twitter afin d'extraire des données avec 3 méthodes différentes. Les données extraites de l'API subissent un léger pré-traitement afin d'être envoyées sous forme de dataframe pandas au programme de traitement et prédiction de sentiments. 
- IA : Dans cette partie les tweetts stockés dans la dataframe subiront un traitement de texte (lemmatisation, suppression des stop-words etc.) et également une prédiction du sentiment : 
        - Une première méthode, un peu naïve, avec une utilisation simple de la méthode polarity du module Textblob afin de savoir s'il s'agit plutôt d'un sentiment positif, neutre ou négatif. Résultat stocké dans la colonne ["Sentiment] de type [int]
        - Une seconde méthode, un peu plus complexe, qui permet de déterminer le sentiment qui ressort parmi les suivants : angry, fear, disgust, happy, sad, surprise. Cette dernière repose sur un modèle de RandomForest et du bag of words pour la transcription des strings en données interprétables par un modèle de machine learning. Résultat stocké dans la colonne ["Sentiment_IA"] de type [str]
On renvoie ainsi une dataframe avec une ou deux colonnes supplémentaires.
- Base de données : Dans cette partie, il s'agit de mettre en place une base de données sqlite. Cette dernière permettra de stocker nos données plus proprement et de manière plus efficiente que dans CSV. De plus, elle pourra permettre à terme d'être utilisée afin de développer des méthodes de machine learning plus riches en s'appuyant sur plus de données. Aussi, on pourra extraire de manière plus efficiente les données afin de les afficher dans une interface utilisateur. 
- Interface utilisateur : Dans cette partie, il s'agit de mettre en place une interface utilisateur user friendly pour qu'il puisse jouer avec les différentes fonctionnalités que propose notre outil. Cette dernière est mise en ligne. 

## Répartition du travail
La répartition des tâches s'est faite sur la base du volontariat d'un membre de travailler sur une partie et se résume globalement à :

1. API : pris en charge par Louis Moser
2. IA : pris en charge par Tanguy Colleville
3. Base de données : pris en charge par Oscar Vogler
4. Interface utilisateur : pris en charge par Ghislain Flichy
5. Streaming : pris en charge par Ghislain Flichy et Tanguy Colleville

## Découpage en sprints pour la semaine 
Pour ce qui est du découpage de la progression en sprints, nous sommes tombés d'accord sur : 

- Lundi soir 
1. Avoir une communication simple mais existente entre les différentes parties
2. Avoir des résultats "justes"

- Mercredi soir : 
1. Toutes les fonctions basiques communiquent entre elles, de manière efficiente.
2. La mise en place du streaming doit avoir commencée. 
3. Améliorer le NLP sur le vectorizer. Réfléchir à la mise en place d'une méthode de KNN pour améliorer le dataset d'entrainement. 

- Jeudi soir : 
1. Le code est propre (noms des variables évocateurs, commentaires, fonctions avec des heads, pytest avec rapport HTML, README terminé,structuré en packages, modules et fonctions, le requirement.txt est à jour).
2. Le code fonctionne (l'interface est en ligne et permet l'extraction, le traitement, l'analyse, le stockage et l'illustration des données).
3. La présentation en diaporama est claire, concise et terminée.
4. Tentative d'une démonstration au préalable, voire une vidéo de notre démonstration.
## Problèmes rencontrés 

Au cours de cette semaine de développement, nous avons rencontré quelques problèmes. Parmi ceux-ci, on peut mentionner : 

1. Définition des méthodes : En argument des fonctions API.search, utiliser "rpp" (nombre de tweets retournés par page) ne fonctionne plus sur la version 3.9.0 de l'API (argument valable pour la version 3.5.0). Cet argument doit être remplacé par "count".

2. Traitement des données : Problème notamment lors la vectorisation des mots, la richesse lexicale d'un ensemble de twitts est globalement pauvre ce qui induit des problèmes de dimensions. J'ai par ailleurs entrainé mon modèle sur un dataset déséquilibré et relativement faible, ce qui m'a posé des problèmes. Enfin la conjuguaison de deux méthodes de ML ne s'est pas révélée concluante.

3. Base de données : Concernant la base de données, un manque de compréhension et de communication entre les membres, probablement accentués par le distanciel, ont engendré quelques erreurs et retards.

4. Interface graphique : 
- Des problèmes sont apparus notamment à cause de ceux rencontrés sur l'axe base de données. La mise en ligne du site est devenu impossible à partir du moment où nous avons mis en place la base de données (taille des la base de donnée)
- Mulithread compliqué avec les callback present dans la app.py qui raffraichit les graphiques.
- Saturation trop rapide de l'API gratuite tweeter. 

5. Streaming : Problème avec la mise en place de la conjuguaison des requêtes 1,2 et 3 pour le streaming. Problème au niveau de l'interface graphique notamment afin de passer d'un onglet à un autre, et problème pour réinitialiser la partie de la base de données (déstinée au streaming) lorsqu'un nouveau mot clé est entré. 



## Améliorations


- Mettre un place un streaming qui ne se deconnecte pas et change juste le mot clé de filtrage pour ne pas être limité par l'API.
- Améliorer l'interface graphique pour une meilleur information de l'utilisateur sur ce qui est traité et renvoyé. 
- Travailler sur la mise en ligne de l'application.
- Etoffer les méthodes de machine learning et de text processing afin de les rendre plus efficientes.

## Sources

https://radimrehurek.com/gensim/auto_examples/index.html#documentation

https://textblob.readthedocs.io/en/dev/

https://www.nltk.org/

https://docs.python.org/fr/3/library/re.html

https://scikit-learn.org/stable/index.html

https://www.oreilly.com/library/view/applied-text-analysis/9781491963036/ch04.html

https://stackabuse.com/text-classification-with-python-and-scikit-learn/

https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html

https://www.scipy.org/

http://docs.tweepy.org/en/v3.9.0/api.html

https://dash.plotly.com/basic-callbacks

https://dash-bootstrap-components.opensource.faculty.ai

http://docs.tweepy.org/en/v3.4.0/streaming_how_to.html

https://www.tutorialspoint.com/python/python_multithreading.htm

https://dashboard.heroku.com/apps

https://www.bootstrapcdn.com/

