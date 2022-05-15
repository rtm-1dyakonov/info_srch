from nlp_part.preprocess_text import normalization, init as nlp_init

def transform(texts):
    nlp_init()
    text_to_norm = {}
    index = {}
    for text_name in texts:
        eng_stand = normalization(texts[text_name])
        text_to_norm[text_name] = eng_stand
        for token in eng_stand.split(' '):
            if token in index:
                if text_name not in index[token]:
                    index[token].append(text_name)
            else:
                index[token] = [text_name]
    return text_to_norm, index
