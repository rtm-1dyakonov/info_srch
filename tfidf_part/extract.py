import os
from bs4 import BeautifulSoup
from cv_part.xcept import classify 

def extract(src):
    files_content = {}
    listdir = os.listdir(src)
    for i, html_filename in enumerate(listdir):
        print("in progress...\n")
        with open(src + html_filename, 'r', encoding='utf-8') as f:
            html = f.read()
            soup = BeautifulSoup(html, features="html.parser")
            for script in soup(["script", "style"]):
                script.extract()
            text = soup.get_text()
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = '\n'.join(chunk for chunk in chunks if chunk)
            for img in soup.findAll('img'):
                text += (" " + classify('https:' + img.get('src')) + " ")
            files_content[html_filename] = text
        os.system('cls')
        print('Done ' + str(round(100*i/len(listdir),2)) + '%')
    return files_content
    