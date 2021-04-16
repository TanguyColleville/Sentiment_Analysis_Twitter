# Partie NLP du projet 

## Réalisé par 
Tanguy Colleville 

## Introduction 
Nous nous sommes fixés deux objectifs dans notre analyse de sentiments sur les tweets. 
1. Le premier, élémentaire, est d'avoir une idée de la polarité des tweets et ainsi d'obtenir une représentation graphique de ces dernières
2. Le second, plus complexe, il s'agit d'obtenir la répartition des émotions concernant le sujet étudié. 
Le NLP, pour natural langage processing, consiste en l'analyse de données textuelles. 

## Structure 

- NLP 
- |--__init__.py
- |--.gitignore
- |--README.md
- |--Analyse_Emotion.py
- |--Traitement_Text.py
- |--R&D_IA.ipynb 
- |--test_Analyse_Emotion.py
- |--test_traitement_text.py
- |--test_model_ia.py

- my_models 
- |--Label_Encoder.pickle
- |--My_models.pickle
- |--PipeLine.pickle

## Méthode 
La méthode mise en place va suivre les étapes suivantes : 

1. Définir un objectif mesurable : obtenir une précision et un recall supérieur à 80%.

2. Connaitre nos données et le dataset qui va nous servir pour entrainer notre modèle. Phase d'exploration des données. Je me suis rendu compte que le dataset des émotions était desequilibre. C'est pourquoi j'ai mis en oeuvre une méthode d'over_sampling pour l'équilibrer. 

3. Avoir un preprocessing efficient et propre. Mise en place d'une fonction de preprocessing du texte, qui permet notamment de remplacer les emojis par les émotions qui leurs correspondent, enlever les stop words, lemmatiser le texte etc. Cette fonction se trouve dans le module Traitement_text.py qui permet de la partie traitement de texte du preprocessing. Dans le préprocessing il y a également une encodage des différentes émotions pour que ces dernières constituent des classes interprétables par la machine. Enfin il y a le transformateur qui permet de rendre les twitts interprétables par la machine. Nous parlerons du transformateur ci-dessous.

4. Choisir un bon transformateur de données afin d'obtenir une traduction des twitts en format interprétable par la machine. J'ai alors utiliser le transformateur TfidfVectorizer qui permet, à partir d'un ensemble de mots de transformer les twitts en vecteurs. 
La dimension de ces vecteurs est dépendante de la richesse du vocabulaire de l'ensemble de mots fournis en entrée ce qui impliquera des limitations lors de l'utilisation de la prédiction d'émotion sur des twitts.

5. Choisir un modèle de machine learning approprié. Pour se faire, je me suis appuyé sur mes connaissances ainsi que sur la machine learning map de scikit-learn. (url : https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html). J'ai ainsi testé plusieurs modèles. Dans le notebook il ne reste la trace que des ensembles classifiers qui semblaient être les plus efficaces parmi ceux entrainé au préalable. J'ai défini une méthode qui permet d'evaluer un modèle et réaliser une boucle pour tenter de voir lequel parmi les ensembles classifier semblait le plus pertinent.

6. Vérifier que le modèle a bien appris. J'ai ensuite vérifié que le modèle ne présentait pas de problème d'apprentissage tel que de l'overfitting ou bien de l'underfitting. L'avantage du randomforest est qu'il compense les problèmes d'overfitting souvent rencontrés sur un seul arbre. Ici, au vu de la learning curve du modèle retenu, il semblerait que nous ne rencontrions pas de problème de ce genre. La learning curve nous indique simplement que le modèle aurait de meilleure performance si nous disposions de plus de données.

7. Améliorer le modèle, par l'optimisation d'hyperparamètres. Pour se faire j'ai utilisé un gridsearchCV qui permet de retenir les meilleurs hyperparamètres d'un dictionnaire fournis. J'ai ensuite réalisé une sorte de dichotomie sur le paramètre en question, il s'agit du n_estimators, ce dernier représente le nombre d'arbre dans la forêt. J'ai initialisé ma recherche n_estimator=sqrt(nb_features) dans notre cas le nombre de features est donné par le TidfVectorizer qui est 1100. On obtient ainsi le n_estimator optimal de 188. 

8. Enregistement de l'encoder, de la pipeline, et du modèle afin de pouvoir les charger pour faire des prédictions en temps voulu.



## Solution envisagée

Après étude des différents modèles de machine learning, il semblerait que dans notre cas, le modèle le plus approprié soit celui du RandomForest. J'ai ainsi entrainé le modèle à partir d'un dataset Kaggle. Les traces de l'enregistrement de l'encoder, de la pipeline et du modèle se trouvent dans le jupyternotebook R&D_IA. Nous pourrons à présent charger l'encoder, la pipeline et le modèle dans le module Analyse_emotion.py. Dans ce dernier nous pouvons ainsi utiliser notre modèle pré-entrainé pour prédire l'émotion d'un twitt.
Ainsi le jupyternotebook m'a permis de réaliser mon travail d'investigation ainsi que de générer les modèles.


## Conclusion

Pour conclure, il semblerait que le modèle soit plutôt efficace, mais très largement perfectible. En effet avec plus de temps et une base de données plus étoffée il aurait été possible de faire du KNN pour labeliser les twitts de la base de données et entrainer notre modèle avec beaucoup plus de données, car comme nous pouvons le voir avec les learnings curves, l'augmentation du nombre de données contribue très largement à l'amélioration du modèle. Cependant ma tentative n'a pas été concluante comme on peut le voir à la fin du notebook R&D_IA.ipynb. De plus il semblerait qu'il y ait un léger biais sur l'émotion happy qui est sur-représentée, non pas que je doute du bonheur de la collectivité étant donné la conjoncture actuelle.
Aussi, des méthodes de boosting ainsi on prendrait plusieurs ensemble classifier faibles avec un jeu de données équilibre mais en udersampling (on prend n=min(n,n2,n3...n6) ni représentant le nombre d'élement dans la classe i) mais qui, par assemblage de leurs prédictions compensent mutuellement leurs erreurs. 
Cependant nous avons rempli les objectifs pour le MVP. Le champ des possibilités d'amélioration est considérable mais avec des contraintes temporelles moindre. 