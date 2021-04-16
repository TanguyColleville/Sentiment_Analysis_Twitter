import NLP.Traitement_text as TT 

def test_trait_text():
    text="Hi, my name is Tanguy :). I would like to test the module Traitement text !"
    Preprocessed_text=TT.Prepro_Text(text)
    assert type(Preprocessed_text)==str ## on vérifie qu'on renvoie bien un format str 
    assert ":)" not in Preprocessed_text ## on vérifie que le smiley n'est plus dans le texte traité --> smiley bien enlevé
    assert "." not in Preprocessed_text ## on vérifie que le point n'est plus dans le texte traité --> ponctuation bien enlevé
    assert "the" not in Preprocessed_text ## on vérifie que le the n'est plus dans le texte traité --> stop word bien enlevé
    assert "is" not in Preprocessed_text ## on vérifie que le is n'est plus dans le texte traité --> phrase lemmatisée