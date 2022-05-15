import sys
from tfidf_part.extract import extract
from tfidf_part.transform import transform
from tfidf_part.load import load

def main():
    html_storage_location = sys.argv[1]
    extracted = extract(html_storage_location)
    transformed, index = transform(extracted)
    load(transformed, index)