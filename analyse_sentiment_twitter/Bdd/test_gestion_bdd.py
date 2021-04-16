import pandas as pd
from sqlite3 import *

from Bdd.gestion_bdd import *

def test_ajout_tweet():
    data = {'Date' : "18-Nov-2020",'Heure' : "08:11:45", 'ID' : 1.328974158395564e+18,\
            'followers' : 358.0,'is_user_verified':0.0,'lenght':140.0,'like':123.0,\
            'location': "Paris",'methode': 1,'name': "testeuuuur", 'retweets': 1267.0,\
            'source': "Twitter for iPhone" ,'tweet':"Zalyxiqua test ignopalyzx",'text_traite':"test test",\
            'Sentiment' : 1.3, 'Sentiment_IA' : "joie"}
    df = pd.DataFrame(data,index = [0])
    ajout_tweet(df)
    connection = sqlite3.connect("BDD.db")
    res = pd.read_sql_query('SELECT * from tweet_table WHERE ID = 1.328974158395564e+18',connection)
    for x in df:
        assert df['{}'.format(x)][0] ==res['{}'.format(x)][0]