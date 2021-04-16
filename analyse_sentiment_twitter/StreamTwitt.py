import time

import sqlite3
import tweepy
from tweepy.streaming import StreamListener


import Recup_tweet.Twitter_connection_setup as connect
from NLP.Analyse_emotion import Opinion

conn = sqlite3.connect('BDD.db', check_same_thread=False)#connexion à la base de données
c = conn.cursor()## établissement d'un cursor 


def create_table():# fonction de création de table
    try:
        c.execute("DROP TABLE IF EXISTS sentiment")#si la talbe existe on la supprime pour avoir seulement dans la base de données les stream du key words
        c.execute(
            "CREATE TABLE IF NOT EXISTS sentiment(unix REAL, tweet TEXT, sentiment REAL)")#on la crée
        c.execute("CREATE INDEX fast_unix ON sentiment(unix)")# on crée 3 colonnes une pour le time stamps, une pour le tweet, une pour le sentiment
        c.execute("CREATE INDEX fast_tweet ON sentiment(tweet)")
        c.execute("CREATE INDEX fast_sentiment ON sentiment(sentiment)")
        conn.commit()
    except Exception as e: ## on montre l'exception 
        print("create_table Exeption : ", str(e))


class StdOutListener(StreamListener):#création de la classe SdtOUtListener qui hérite de StreamListener 
    def __init__(self, n_tweet=None, dure=None):#création du init avec super pour récupérer les propriétés du init de la classe streamListener
        super().__init__()
        self.cb_tweet_ = 0 #compteur de twitt pour pouvoir arreter le live si on dépasse la limite de n_tweet
        self.n_tweet_ = n_tweet ##limite du nombre de twitt à récupérer sur le live 
        self.time_ = time.time() ## initialisation d'un compteur de temps afin d'imposer une limite temporelle sur le live stream
        self.dure_ = dure ## limite de temps de stream

    def on_status(self, status):# permet de faire plusieurs choses 
        """
        =======================
        Aim 
        =======================
        gérer les limitations de nombres de tweets et le temps depuis le lancement et l'ecriture dans la base de données 

        =======================
        Entries 
        =======================
        le status du twitt

        =======================
        Return
        =======================
        Boolean : True si pas de problème 

        """
        self.cb_tweet_ += 1 # on incrémente le compteur de twitt 

        if self.cb_tweet_ > self.n_tweet_ or time.time()-self.time_ > self.dure_: ##on vérifie que les conditions temporelles et de compteur de twitt ne sont pas excédés
            cleanup()# si c'est le cas on arrête le live stream
        tweet = status.text ## on récupère le texte 
        time_ms = status.created_at #on récupère le timestamp 
        sentiment = Opinion(tweet) #on détermine l'opinion du twitt
        c.execute("INSERT INTO sentiment (unix, tweet, sentiment) VALUES (?, ?, ?)",
                  (time_ms, tweet, sentiment))## on ajoute alors les données à la bdd 
        conn.commit()# on ferme le curseur
        return True ##on renvoie la valeur true

    def on_error(self, status_code):##détection d'erreur 
        if status_code == 420:
            print('limite API')
            # returning False in on_data disconnects the stream
            return False


def cleanup():## fonction pour déconnecter le stream
    stream.disconnect()


def methode_4_extract(key_words, n_tweet, dure=3600):#
    """
    ==========================================
    Aim 
    ==========================================

    Récupérer les twitts en live qui contiennent le(s) key_words dans la limite de n_tweets et dure 

    ==========================================
    Entries :  
    ==========================================

    Key_words : un string de mots clés [str]
    n_tweet : le nombre de mot twitt max à extraire [int]
    dure : durée maximale de la session de twitt [int]

    ==========================================
    Return : 
    ==========================================

    Nothing

    """
    print("===========  méthode 4 lancée  ============= ")

    try:
        connexion = connect.twitter_setup()# on connecte l'api 
        listener = StdOutListener(n_tweet, dure)# création d'un objet de la classe StdOutlistener avec les attributs 
        global stream## déclaration de variable globale pour pouvoir arrêter le stream 
        stream = tweepy.Stream(auth=connexion.auth, listener=listener)# lancement du stream
        stream.filter(track=key_words, languages=["en"])##filtrage sur le stream pour la langue anglaise et le suivi des keywords désirés 

    except Exception as e:
        print("exeption : ", str(e))
        time.sleep(5)


if __name__ == "__main__":
    pass
