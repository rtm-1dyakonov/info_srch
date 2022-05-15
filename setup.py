from setuptools import setup, find_packages

setup(name= 'info_srch', packages=['cv_part', 'tfidf_part', 'nlp_part', 'vectorization'], install_requires=['nltk', 'bs4', 'keras', 'translate'],entry_points={'console_scripts':['tfidf = tfidf_part.run:main', 'request = vectorization.run:main', 'quality = calc_quality.run:main']})