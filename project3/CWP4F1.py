import openai

class numReview:
    def __init__(self):
      #  self.name = name
        self.numPos = 0
        self.numNeg = 0
        self.numNeu = 0
        self.numRev = 0

    def addSent(self,response):
        if response.choices[0].message.content == "Positive":
            self.numPos += 1
        elif response.choices[0].message.content == "Negative":
            self.numNeg += 1
        else:
            self.numNeu += 1


def response(fileName,  numFile):
    # file = open("C:/Users/KimJo/project2/review1.txt")
    obj = numReview()
    numPos = 0
    numNeg = 0
    numNeu = 0
    file = open(fileName, encoding="utf8")
    client = openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="nokeyneeded",
)
    i = 1
    f = open(f'c:/Users/KimJo/project3/output{numFile}.txt', "w", encoding='utf-8')
    for line in file:
    # Extracts the first line from the text file, which is the first question
        content1 = line
        prompt = "Please give only a one word response to the following review that is negative, positive or neutral. Remember only respond with ONE word" 
    
    # Creates a response from the ollama phi3 LLM, with content being the question
    # gotten from the text file
        response = client.chat.completions.create(
            model="phi3",
            n=1,
            temperature = 0,
            messages=[
      
                {"role": "user", "content": prompt + content1},
        
    ],
)
        if response.choices[0].message.content == "Positive":
            numPos += 1
        elif response.choices[0].message.content == "Negative":
            numNeg += 1
        else:
            numNeu += 1
        obj.addSent(response)


        # print(response.choices[0].message.content[0])
        f.write(response.choices[0].message.content)
        f.write("\n")
    
    f.close()
    return [obj.numPos,obj.numNeg,obj.numNeu]

