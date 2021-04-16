
import Recup_tweet.Tweet_collection as TC
import NLP.Analyse_emotion as AE
import Bdd.acces_bdd as Acc
import Bdd.gestion_bdd as Gcc


def main(nb_tweet, tweet_redactor, keyword, selected):
    # nettoyage bdd à inserer
    print(nb_tweet, tweet_redactor, keyword, selected)
    if selected == 1:
        df = AE.creation_sentiment(TC.methode_1_extract(
            nb_tweet, keyword, tweet_redactor))

    elif selected == 2:
        df = AE.creation_sentiment(
            TC.methode_2_extract(nb_tweet, tweet_redactor))

    elif selected == 3:
        df = AE.creation_sentiment(TC.methode_3_extract(nb_tweet,tweet_redactor))
    
    Gcc.ajout_tweet(df)
    df_bdd=Acc.req_tweet(tweet_redactor[1:],keyword,selected) 
    return df


if __name__ == "__main__":
    pass
