import NLP.Analyse_emotion as AE    
import pandas as pd 

def test_ana_emo():
    df=pd.read_csv(r"Data\Bdd_test_global.csv")
    df=AE.creation_sentiment(df)
    assert "Sentiment" in df.keys()
    assert "Sentiment_IA" in df.keys()