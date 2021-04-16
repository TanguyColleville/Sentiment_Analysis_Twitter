import datetime

import sqlite3
import pandas as pd



def compare_date (date):
    """
    Param : prend en entrée la date du df du tweet
    Output : True si la date correspond a la plage entre la date actuelle et cette même date 
    moins 7 jours, False sinon
    """
    today = datetime.date.today() #date d'aujourd'hui (de type datetime.date)
    ds = datetime.datetime.strptime(date, '%d-%b-%Y') #converti la chaine de caractere en date (type datetime.datetime)
    delta = today - datetime.timedelta(weeks = 1) #date de aujourd'hui - 7 jours 
    if ds >= (datetime.datetime.combine(delta,datetime.time(0,0))) : #converti le datetime.date en datetime.datetime pour la comparaison
        return True
    else :
        return False
    
def req_all (tt = 0):
    """
    Param : tt :    si = 0 renvoie tous les tweets de la base de donnée datant au maximum de 7 jours
                    si = 1 renvoie tous les tweets de la base de donnée
    """
    try : 
        connection = sqlite3.connect("BDD.db")
        df = pd.read_sql_query('SELECT * FROM tweet_table', connection)
        if tt == 0 :
            liste=[]
            for i in df.index :
                liste.append(compare_date(df['Date'][i])) #créé une liste de True ou False indiquant si le tweet de la dataframe date d'il y a plus de 7 jours ou non
        connection.close()
        return df[liste] #on ne garde que les tweets datant au maximum d'une semaine
    except Exception as e:
        print ("[ERREUR]", e)
        return False
    
def req_tweet(name = "Aucun",req="Aucuns",methode = 1,tt = 0):
    """
    Param : 
    name : nom de l'utilisateur,
    req = string contenant les mots clés à rechercher séparés par OR ou AND, 
    methode : indique si on cherche à récupérer un tweet, un retweet ou une réponse
    tt : paramètre indiquant par défaut que l'on veut les tweets datés d'une 
    semaine au plus et si tt=1: récupère tous les tweets de la bdd quelque soit la date
    DESCRIPTION : recupère les tweets de la table tweet qui correspondent à un ou plusieurs des critères si dessous
    Returns : la dataframe demandée ou False si erreur
    """
    try :
        connection = sqlite3.connect("BDD.db")
        
        ### Création d'un string contenant la requete sql en fonctions des différents critères en entrée          
        if (name == "Aucun" and req =="Aucuns"):
            return pd.DataFrame()              
        sql = "SELECT * FROM tweet_table"
        if (methode == 1 or methode == 2 or methode == 3) :
            sql = sql + " WHERE methode = " + str(methode) + " AND "
        else :
            print("[ERREUR] Le paramètre methode doit être égal à 1,2 ou 3")
        if (name != "ucun"):
            sql = sql + "name = '{}'".format(str(name))
            if (req != "Aucuns") :
                sql += " AND "
        if (req != "Aucuns") :
            sql = sql + "tweet LIKE '%"
            cpt = 1
            if "AND" in req :
                req_split = req.split(' AND ')
                for mot in req_split :
                    if cpt != len(req_split) :
                        sql = sql +mot+"%' AND tweet LIKE '%"
                    else :
                        sql = sql +mot+"%'"
                    cpt+=1
            elif "OR" in req :
                req_split = req.split(' OR ')
                for mot in req_split :
                    if cpt != len(req_split) :
                        sql = sql +mot+ "%' OR tweet LIKE '%"
                    else :
                        sql = sql +mot+"%'"
                    cpt+=1
            else :
                sql= sql+req+"%'"
        ### Requete sql 
        print(sql)
        df = pd.read_sql_query(sql,connection)
        
        ### Selection de la date dans le dataframe créé
        if tt == 0 :
            liste=[]
            for i in df.index :
                liste.append(compare_date(df['Date'][i]))
        return df[liste]
    except Exception as e:
        print ("[ERREUR]", e)
        return False
    finally : 
        connection.close()