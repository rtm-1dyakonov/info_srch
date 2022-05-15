from vectorization.algo import save_model, DocsDictinaryTfIdfVectorizer

def load(clean_texts, index):
    tf_idf = DocsDictinaryTfIdfVectorizer(max_df = 0.5, docsDict=clean_texts, index=index)
    tf_idf.fit_transform(clean_texts.values())
    save_model(tf_idf)
