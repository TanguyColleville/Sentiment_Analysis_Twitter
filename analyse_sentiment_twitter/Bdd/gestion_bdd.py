import sqlite3

def create_table():
    """
    Créé la base de donnée
    """
    try:
        connection = sqlite3.connect("BDD.db")
        cursor = connection.cursor()
        cursor.execute(''' CREATE TABLE IF NOT EXISTS "tweet_table" (
                                            "Date"    TEXT,
                                            "Heure"    TEXT,
                                            "ID"    FLOAT,
                                            "followers"    INTEGER,
                                            "is_user_verified"    INTEGER,
                                            "lenght"    INTEGER,
                                            "like"    INTEGER,
                                            "location"    TEXT,
                                            "methode" INTEGER,
                                            "name"    TEXT,
                                            "retweets"    INTEGER,
                                            "source"    TEXT,
                                            "tweet"    TEXT,
                                            "text_traite"    TEXT,
                                            "Sentiment"    FLOAT,
                                            "Sentiment_IA"    TEXT,
                                            PRIMARY KEY("ID"))''')
    except:
        print("Erreur de création de la database")
    finally:
        connection.close()
        

def ajout_tweet(df) :
    """
    Param : df : data frame contenant les informations d'un tweet + les sentiments
    DESCRIPTION : ajoute un tweet à la table tweet de la bdd,
    Returns : None
    """
    try :
        connection = sqlite3.connect("BDD.db") #etabli la connexion avec la base de donnée, la créé si elle n'existe pas
        create_table() #créé la table tweet_table si elle n'existe pas
        cursor = connection.cursor()
        liste = df.values.tolist() #converti le dataframe en liste
        for data in liste:
            try :
                cursor.execute('INSERT INTO tweet_table VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)',data) #insert les 16 valeurs de la liste dans la table de la bdd
                connection.commit() #valide la modification
            except Exception as e:
                """
                On recupère l'erreur : si l'erreur correspond a UNIQUE constraint failed, 
                c'est que le tweet est déjà dans la base de donnée, dans ce cas on revient
                au dernier commit et on passe à la donnée suivante dans la boucle
                """
                if str(e) == "UNIQUE constraint failed: tweet_table.ID" :
                    connection.rollback()
                else:
                    print ("[ERREUR]", e)
                    connection.rollback()
                    break
    except Exception as e:
        print ("[ERREUR]", e)
        connection.rollback() # si erreur : revient au dernier commit
    finally :
        connection.close() 