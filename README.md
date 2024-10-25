## Tutorial to Scrape Reviews Off Ebay
This tutorial will take you through the steps to scrape any reviews off of Ebay and put it into a textfile.

## Miniconda
You will need to use miniconda in order to download and format the specific environment required.
Download miniconda from here (https://docs.anaconda.com/miniconda/miniconda-install/).

## Environment
After that you will need to clone the environment. Download the requirment.yaml file then create an environment using the
yaml file which you can do by typing this in your miniconda prompt.

```bash

conda create --name yourName --file requirement.yaml

```

This will download all the dependencies you need to run this program, specifically beautifulsoup.

## Text File
The program will output several different text files, one for each product you input. Put all links of products that you want to be reviewed into a single text file,
and put a newline between each new product. ie

```bash

https://www.ebay.com/urw/Samsung-Galaxy-S21-5G-128-GB-Gray-Unlocked-/product-reviews/28043687656?pgn=1

https://www.ebay.com/urw/Samsung-Galaxy-S20-5G-128-GB-Gray-Unlocked-/product-reviews/20036893230?pgn=1
```
The program will consider these unique products and will create a different review file for each one. This currently also only scrapes the first pages of reviews for each item,
to add more you will need to add one to the page number for each item.

```bash

https://www.ebay.com/urw/Samsung-Galaxy-S21-5G-128-GB-Gray-Unlocked-/product-reviews/28043687656?pgn=1
https://www.ebay.com/urw/Samsung-Galaxy-S21-5G-128-GB-Gray-Unlocked-/product-reviews/28043687656?pgn=2

https://www.ebay.com/urw/Samsung-Galaxy-S20-5G-128-GB-Gray-Unlocked-/product-reviews/20036893230?pgn=1
https://www.ebay.com/urw/Samsung-Galaxy-S20-5G-128-GB-Gray-Unlocked-/product-reviews/20036893230?pgn=2
```
This will get the first two pages of reviews of each item, adding more links will further the pages the program will scrape. 

## Program

Finally you can launch the program where fullPathHere is the full path of where the program is located, pathOfLinks is the path of where the links are located.
```bash

python fullPathHere pathOfQuestion pathOutput

```
The program will output a file called review one for each product in the links file.
