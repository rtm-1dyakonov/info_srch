from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import os

FILENAME = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'vectorizer.pk')

class DocsDictinaryTfIdfVectorizer(TfidfVectorizer):
    def __init__(self, max_df, docsDict, index):
        super().__init__(max_df=max_df)
        self.docsDict = docsDict
        self.index = index

def save_model(tf_idf_vectorizer):
    return pickle.dump(tf_idf_vectorizer, open(FILENAME, 'wb'))

def load_model():
    print(FILENAME)
    return pickle.load(open(FILENAME, 'rb'))
