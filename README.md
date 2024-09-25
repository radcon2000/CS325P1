## Tutorial
This tutorial will take you through the steps to communicate with a LLM locally

## Miniconda
You will need to use miniconda in order to download and format the specific environment required.
Download miniconda from here (https://docs.anaconda.com/miniconda/miniconda-install/).

## Ollama
First you will need to install Ollama, which you can install through this link (https://ollama.com/download).
After that, launch ollama and download phi3.

```bash

ollama run phi3

```

## Environment
After that you will need to clone the environment. Download the requirment.yaml file then create an environment using the
yaml file which you can do by typing this in your miniconda prompt.

```bash

conda create --name yourName --file requirement.yaml

```

This will download all the dependencies you need to run this program, python and openAI. 

## Program
Once that is done you can launch the program where fullPathHere is the the full path of where the program is located,
pathOfQuestions is the path of the questions that want to be asked and pathOutput is where you want the output to be 
stored. 

```bash

python fullPathHere pathOfQuestion pathOutput

```
