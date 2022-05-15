from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import nltk
from string import punctuation

stemmer = SnowballStemmer("english")
stopwords_eng = stopwords.words("english")

def init():
    nltk.download("stopwords")

def normalization(text): 
    text_upd = text.lower().replace("\n", "").split(" ")
    tokens = [stemmer.stem(word) for word in text_upd]
    norm_text = " ".join([token.translate(str.maketrans('', '', punctuation)) for token in tokens if token not in stopwords_eng and token != " "])
    return norm_text
