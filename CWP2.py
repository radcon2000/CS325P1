import requests 
import argparse
from bs4 import BeautifulSoup

numRev = 1
numRevs = 1

parser = argparse.ArgumentParser()

parser.add_argument(help="Enter the full path of the file that contains the links.", dest='lFile', type=str)

args = parser.parse_args()

lFile = args.lFile

f = open(f'c:/Users/KimJo/project2/review{numRev}.txt', "w", encoding='utf-8')

##C:/Users/KimJo/project2/links.txt
file = open(lFile)
content = file.readline()
while content:
    if content =='\n':
        numRev += 1
        f.close()
        f = open(f'c:/Users/KimJo/project2/review{numRev}.txt', "w", encoding='utf-8')
        content = file.readline()
    else :
        res = requests.get(content)
        soup = BeautifulSoup(res.content, "html.parser")
        review = soup.find(id ='reviewContentSection')
        results = review.find_all('p', class_='review-item-content rvw-wrap-spaces')
        for review in results:
            strRev = str(numRevs)
            f.write("Review Number ")
            f.write(strRev)
            f.write(": ")
            f.write(review.text)
            f.write('\n')
            f.write('\n')
            numRevs += 1
        content = file.readline()

f.close()
file.close()