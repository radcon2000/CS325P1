# Written by Conrad Weiland, this file creates a connection to ollama phi3 LLM through the openAI server endpoint, reads questions
# from a text file then asks that question to phi3, and saves the response to a differenttext file. 

import openai
import argparse


parser = argparse.ArgumentParser()

parser.add_argument(help="Enter the full path of the file that contains the questions.", dest='qFile', type=str)
parser.add_argument(help="Enter the full path of the file that you want to write the data to.", dest='wFile', type=str)

args = parser.parse_args()

qFile = args.qFile
wFile = args.wFile

# Creates a connection to openai ollama, which is ran locally.
client = openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="nokeyneeded",
)


# Opens the text file that contains the questions
file = open(qFile)

# Opens/Creates a text file to store phi3's response
f = open(wFile, "w+", encoding='utf-8')

# Repeats the loop three times, one for each question
for i in range(1,4):

    # Extracts the first line from the text file, which is the first question
    content = file.readline()
   
    
    # Creates a response from the ollama phi3 LLM, with content being the question
    # gotten from the text file
    response = client.chat.completions.create(
        model="phi3",
        n=1,
        messages=[
      
            {"role": "user", "content": content},
        
    ],
)
    # Writes the response to a new text file
    f.write("Question {}: ".format(i) )
    f.write(response.choices[0].message.content)
    f.write("\n")
    f.write("\n")



# Closes the files that were opened
file.close()
f.close()