# Written by Conrad Weiland, this program accepts links from a file, goes to those links, and scrapes the reviews off the Ebay website. 
# The program then writes all those reviews in a text file, with a unique one for each product tested. 
# python C:/Users/KimJo/project3/CWP4.py C:/Users/KimJo/project3/links.txt
import CWP4F1
from CWP4F1 import response
import requests 
import argparse
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np

class Reviews:
    def __init__(self,deviceName,numDevice):
        self.numPos = [0] * numDevice
        self.numNeg = [0] * numDevice
        self.numNeu = [0] * numDevice
        self.deviceName = ["Not Given"] * numDevice
    def Pos(self,numDevice,numPos):
        self.numPos[numDevice - 1] = numPos
    def Neg(self,numDevice,numNeg):
        self.numNeg[numDevice - 1] = numNeg
    def Neu(self,numDevice,numNeu):
        self.numNeu[numDevice - 1] = numNeu
    def deviceName(self,numDevice):
        self.deviceName[numDevice - 1] = "Samsung" + str(numDevice)
def getReview(file,content):
    f = open(file, "a", encoding='utf-8')
            # This gets the content from the website and boils it down to just the reviews, which then writes it into a text file. 
    res = requests.get(content)
    soup = BeautifulSoup(res.content, "html.parser")
    review = soup.find(id ='reviewContentSection')
    results = review.find_all('p', class_='review-item-content rvw-wrap-spaces')
    for review in results:
        f.write(review.text)
        f.write('\n')
    f.close()

def makePlot(numPos, numNeg, numNeu):
    deviceName = ("Samsung1", "Samsung2", "Samsung3", "Samsung4", "Samsung5")
    device_info = {
        'Positive': (numPos[0], numPos[1], numPos[2], numPos[3], numPos[4]),
        'Negative': (numNeg[0],numNeg[1],numNeg[2],numNeg[3],numNeg[4]),
        'Neutral': (numNeu[0],numNeu[1],numNeu[2],numNeu[3],numNeu[4]),
    }

    x = np.arange(len(deviceName))
    width = 0.25
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')

    for attribute, measurement in device_info.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Num Reviews')
    ax.set_title('Device Review Chart')
    ax.set_xticks(x + width, deviceName)
    ax.legend(loc='upper left', ncols=3)
    ax.set_ylim(0, 50)

    plt.show()


numRev = 1
numRevs = 1

parser = argparse.ArgumentParser()

parser.add_argument(help="Enter the full path of the file that contains the links.", dest='lFile', type=str)

args = parser.parse_args()

lFile = args.lFile

# Opens a review file, creates one if one is not already created.

##C:/Users/KimJo/project2/links.txt
file = open('c:/Users/KimJo/project3/links.txt')
#While the file has links, it will read a new link. With a blank line being considered a new product.

obj = Reviews('Samsung1',5)
content = file.readline()
while content:
    if content =='\n':
        # 'c:/Users/KimJo/project3/review' + str(numRev) + '.txt'
        fileName = 'c:/Users/KimJo/project3/review' + str(numRev) + '.txt'
        a = response(fileName, numRev)
        obj.Pos(numRev,a[0])
        obj.Neg(numRev,a[1])
        obj.Neu(numRev,a[2])

        numRev += 1
        content = file.readline()
    else :
        # This gets the content from the website and boils it down to just the reviews, which then writes it into a text file. 
        getReview('c:/Users/KimJo/project3/review' + str(numRev) + '.txt',content)
        content = file.readline()
fileName = 'c:/Users/KimJo/project3/review' + str(numRev) + '.txt'
a = response(fileName, numRev)
obj.Pos(numRev,a[0])
obj.Neg(numRev,a[1])
obj.Neu(numRev,a[2])
#print(numPos)
#print(numNeg)
#print(numNeu)
#f.close()
file.close()

#print(obj.numPos)
#print(obj.numNeg)
#print(obj.numNeu)
makePlot(obj.numPos,obj.numNeg,obj.numNeu)

