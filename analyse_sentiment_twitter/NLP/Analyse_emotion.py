import pickle5 as pickle
from textblob import TextBlob

import NLP.Traitement_text as TT



def Opinion(tweet):
    """
    Aim : Get the sentiment polarity of a tweet
    ====================================================

    Entrie : mytweet : a str representing the tweet we want to be analysed

    ====================================================

    Return : the polarity of the tweet E [-1,1] which represents the "Sentiment" [int]
    """
    if tweet is not None :
        return TextBlob(tweet).sentiment.polarity
    else : 
        print("problème dans l'entrée de Opinion fonction")


def analyse_tweet(mytweet):
    """
    Aim : Get a column Sentiment which represents sentiment polarity
    ====================================================

    Entrie : mytweet : DataFrame panda with les tweets

    ====================================================

    Return : initial DataFrame with a new column "Sentiment" [int]
    """
    if "treaty_text" not in mytweet.keys():  # if text is not already traited then preprocess it
        mytweet["treaty_text"] = mytweet["tweet"].map(TT.Prepro_Text)
    # using map to apply Opinon on the treaty_text column
    mytweet["Sentiment"] = mytweet["treaty_text"].map(Opinion)
    return mytweet  # return the entire dataframe


def load_models():
    """
    Aim : To load the encoder, the pipeline, the model of our IA 
    ====================================================

    Entrie : None

    ====================================================

    Return : the encoder, the pipeline, the model
    """
    try: 
        file = open('my_models/Label_Encoder.pickle',
                    'rb')  # to open the file
        Label_encod = pickle.load(file)  # to load it in a variable
        file.close()  # to close it once we've loaded it

        file = open('my_models/PipeLine.pickle', 'rb')
        pipe = pickle.load(file)
        file.close()

        file = open('my_models/My_Model_test.pickle', 'rb')
        model = pickle.load(file)
        file.close()
    except : 
        print("problème dans le chargement des outils de machine learning")
    # returning the 3 variables that contain our sklearn features
    return Label_encod, pipe, model


def IA_tweet(mytweet):
    """
    Aim : Get a sentiment for each tweet. There are only 6 sentiments --> angry, disgust,fear,happy,sad,surprise
    ====================================================

    Entrie : mytweet : DataFrame panda with tweets

    ====================================================

    Return : initial DataFrame with a new column "Sentiment_IA" [string]
    """
    if "treaty_text" not in mytweet.keys():  # if text is not already traited then preprocess it
        mytweet["treaty_text"] = mytweet["tweet"].map(TT.Prepro_Text)
    # get the encoder,the pipeline and the model trained
    Label_encod, pipe, model = load_models()
    # creating a new column Sentiment_IA
    # first using pipeline to transform data in the right way to be used be the model to do the prediction
    
    to_be_predicted = pipe.fit_transform(mytweet["treaty_text"])
    # second model do the prediction
    # then we use the encoder to return the emotion properly and not the number associate to this emotion
    try:## on met ici un try car comme on l'a vu dans le readme si la richesse lexicale du jeu de données est trop faible 
        #le TidfVectorizer n'est pas fonctionnel car j'ai imposé une dimension d=1100 afin d'obtenir des résultats plus satisfaisant.
        mytweet["Sentiment_IA"] = Label_encod.inverse_transform(
            model.predict(to_be_predicted))
        return mytweet
    except:
        mytweet["Sentiment_IA"] = [None]*len(mytweet)## permet de la robustesse pour toujours pouvoir enregistrer dans la base de données
        print("Vous devez prendre plus de tweet en compte")## previens que l'étude des émotions sera dès lors impossible
        return mytweet  # returning the entire dataframe


def creation_sentiment(df):
    """
    Aim : To have both Sentiment_IA and polarity sentiment in our dataframe
    ====================================================

    Entrie : df : DataFrame panda with tweets

    ====================================================

    Return : initial DataFrame with 2 news columns Sentiment [int] and Sentiment_IA [string]


    """
    if df is not None:
        df = IA_tweet(df)
        df = analyse_tweet(df)
    return df
