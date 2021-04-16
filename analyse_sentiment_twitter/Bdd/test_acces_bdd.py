from sqlite3 import *
from Bdd.gestion_bdd import *
from Bdd.test_gestion_bdd import *
from Bdd.acces_bdd import *

def test_acces_bdd():
    data = {'Date' : "18-Nov-2020",'Heure' : "08:11:45", 'ID' : 1.328974158395564e+18,\
            'followers' : 358.0,'is_user_verified':0.0,'lenght':140.0,'like':123.0,\
            'location': "Paris",'methode': 1,'name': "testeuuuur", 'retweets': 1267.0,\
            'source': "Twitter for iPhone" ,'tweet':"Zalyxiqua test ignopalyzx",'text_traite':"test test",\
            'Sentiment' : 1.3, 'Sentiment_IA' : "joie"}
    df = pd.DataFrame(data,index = [0])
    test_ajout_tweet()
    ajout_tweet(df)
    connection = sqlite3.connect("BDD.db")
    assert (req_tweet("testeuuuur").size != 0 and req_tweet("testeuuuur").values[0][12] == "Zalyxiqua test ignopalyzx")
    assert (req_tweet("testeuuuur").size != 0 and req_tweet(req="Zalyxiqua").values[0][12] == "Zalyxiqua test ignopalyzx")
    assert (req_tweet("testeuuuur").size != 0 and req_tweet(req="Zalyxiqua OR ignopalyzx").values[0][12] == "Zalyxiqua test ignopalyzx")
    assert (req_tweet("testeuuuur").size != 0 and req_tweet(req="Zalyxiqua AND ignopalyzx AND test").values[0][12] == "Zalyxiqua test ignopalyzx")
    assert (req_tweet("testeuuuur").size != 0 and req_tweet("testeur",req="ignopalyzx OR ignopalyzx").values[0][12] == "Zalyxiqua test ignopalyzx")
    assert req_tweet(req="Zalyxiqua AND globule").size == 0
    assert req_tweet("Aucun","Aucuns").size == 0
    