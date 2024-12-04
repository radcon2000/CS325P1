## Tutorial to Scrape Reviews Off Ebay Then Have an AI Get The Sentiment of Reviews.
This tutorial will take you through the steps to scrape any reviews off of Ebay and put it into a textfile. The textfile will then be passed through a LLM,
 which will give the sentiment of the review, which is either positive, negative or neutral. 

 ## Dependencies 
You will need to use miniconda in order to download and format the specific environment required.
Download miniconda from here (https://docs.anaconda.com/miniconda/miniconda-install/).

After that you will need to install Ollama, which you can install through this link (https://ollama.com/download).
After that, launch ollama and download phi3.

```bash

ollama run phi3

```

## Environment
Once that is completed you will need to clone the environment. Download the requirment.yaml file then create an environment using the
yaml file which you can do by typing this in your miniconda prompt. 

```bash

conda create --name yourName --file requirement.yaml

```
This will download all the dependencies you need to run this program in that environment, specifically openAI, beautifulsoup, matplotlib etc. 

## Text File
The program will output several different text files, one for each product you input. Put all links of products that you want to be reviewed into a single text file,
and put a newline between each new product. ie

```bash

https://www.ebay.com/urw/Samsung-Galaxy-S21-5G-128-GB-Gray-Unlocked-/product-reviews/28043687656?pgn=1

https://www.ebay.com/urw/Samsung-Galaxy-S20-5G-128-GB-Gray-Unlocked-/product-reviews/20036893230?pgn=1
```
The program will consider these two unique products and will create a different review file for each one. This currently also only scrapes the first pages of reviews for each item,
to add more you will need to add one to the page number for each item.

```bash
https://www.ebay.com/urw/Samsung-Galaxy-S21-5G-128-GB-Gray-Unlocked-/product-reviews/28043687656?pgn=1
https://www.ebay.com/urw/Samsung-Galaxy-S21-5G-128-GB-Gray-Unlocked-/product-reviews/28043687656?pgn=2

https://www.ebay.com/urw/Samsung-Galaxy-S20-5G-128-GB-Gray-Unlocked-/product-reviews/20036893230?pgn=1
https://www.ebay.com/urw/Samsung-Galaxy-S20-5G-128-GB-Gray-Unlocked-/product-reviews/20036893230?pgn=2
```
This will get the first two pages of reviews of each item, adding more links will further the pages the program will scrape. 

## Sentiment
The program will automatically pass the review files into an LLM which will ask the LLM to give the sentiment of the review.
Once the sentiment is given, it will store that sentiment into a text file called "output", one for each product given. 
Finally, once all the sentiments are stored the program will create a graph of the different products and the number
of each type of review and the numbers of each one. Below is a what an example graph might look like. 

![image](https://github.com/user-attachments/assets/0e4758e2-6eab-4d46-8c26-4c70662fbde8)


## Program

Finally you can launch the program where fullPathHere is the full path of where the program is located, pathOfLinks is the path of where the links are located.
```bash

python fullPathHere pathOfQuestion

```
The program will output several different files, a review file and sentiment file, one for each product that was given. 
