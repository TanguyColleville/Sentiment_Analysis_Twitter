from nltk.corpus import stopwords
import re 
import string
from textblob import TextBlob
from textblob import Word



## dictionnaire des emojis et de leurs émotions associées
emojis = {':)': 'smile', ':-)': 'smile', ';d': 'wink', ':-E': 'vampire', ':(': 'sad', 
          ':-(': 'sad', ':-<': 'sad', ':P': 'raspberry', ':O': 'surprised',
          ':-@': 'shocked', ':@': 'shocked',':-$': 'confused', ':\\': 'annoyed', 
          ':#': 'mute', ':X': 'mute', ':^)': 'smile', ':-&': 'confused', '$_$': 'greedy',
          '@@': 'eyeroll', ':-!': 'confused', ':-D': 'smile', ':-0': 'yell', 'O.o': 'confused',
          '<(-_-)>': 'robot', 'd[-_-]b': 'dj', ":'-)": 'sadsmile', ';)': 'wink', 
          ';-)': 'wink', 'O:-)': 'angel','O*-)': 'angel','(:-D': 'gossip', '=^.^=': 'cat'}
          
def Stop_bin(text):
    """
    Aim : to delete stopwords of a tweet
    =======================================
    Entrie : a tweet (str)
    =======================================
    Return : the tweet without stopwords (str)
    """
    if type(text)==str: 
        Without_stop_word =" ".join(list(word for word in TextBlob(text).words if word not in stopwords.words('english')))#suppression of english stopwords
        return Without_stop_word
    else : 
        print("problème dans l'entrée de stop_bin")
    

def remove_punctuation(text):
    """
    Aim : to delete ponctuation
    =======================================
    Entrie : a tweet (str)
    =======================================
    Return : the tweet without ponctuation (str)
    """
    # replacing the punctuations with no space, 
    # which in effect deletes the punctuation marks 
    if type(text)==str:
        translator = str.maketrans('', '', string.punctuation)
        # return the text stripped of punctuation marks
        return text.translate(translator)
    else : 
        print("problème dans l'entrée de remove_punctuation")


def Prepro_Text(tweet):
    """
    Aim  : split the text by word and delete stopwords
    =====================================
    Entrie : text of the tweet 
    =====================================
    Return : text 

    """
    urlPattern        = r"((http://)[^ ]*|(https://)[^ ]*|( www\.)[^ ]*)"
    userPattern       = '@[^\s]+'
    sequencePattern   = r"(.)\1\1+"
    seqReplacePattern = r"\1\1"
    if type(tweet)==str:
        ##minuscule
        tweet = (tweet.lower())
        
        tweet=remove_punctuation(tweet)
        # Replace all URls with 'URL'
        tweet = re.sub(urlPattern,' URL',tweet)
        # Replace all emojis.
        for emoji in emojis.keys():
            tweet = tweet.replace(emoji, "EMOJI" + emojis[emoji])        
        # Replace @USERNAME to 'USER'.
        tweet = re.sub(userPattern,' USER', tweet)    
        # Replace 3 or more consecutive letters by 2 letter.
        tweet = re.sub(sequencePattern, seqReplacePattern, tweet)
        # Remove stopwords
        tweet=Stop_bin(tweet)
        # if TextBlob(tweet).detect_language()=="fr":
            # tweet=TextBlob(tweet).translate(from_lang="fr",to="en")

        ##Lemmatize the tweet
        tweetwords=str()
        for word in tweet.split():  
            word = Word(word).lemmatize()
            tweetwords += (word+' ')
        return tweetwords ## return the treated tweet
    else : 
        print("Problème dans l'entrée de la fonction traitement_text")

