from sklearn.metrics.pairwise import cosine_similarity
from vectorization.algo import load_model
from nlp_part.preprocess_text import normalization, init as nlp_init

VECTORIZER = None

def init_model():
    global VECTORIZER
    nlp_init()
    VECTORIZER = load_model()

def query(search_str):
    clean_search_str = normalization(search_str)
    keywords = [clean_search_str]
    global VECTORIZER
    vectorized_keywords = VECTORIZER.transform(keywords)
    result_dict = {}
    for word in clean_search_str.split(' '):
        if word not in VECTORIZER.index:
            for filename in VECTORIZER.docsDict:
                result_dict[filename] = cosine_similarity(VECTORIZER.transform([VECTORIZER.docsDict[filename]]), vectorized_keywords)[0][0]
        else: 
            for filename in VECTORIZER.index[word]:
                result_dict[filename] = cosine_similarity(VECTORIZER.transform([VECTORIZER.docsDict[filename]]), vectorized_keywords)[0][0]
    return result_dict