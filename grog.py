from dotenv import load_dotenv
import os
load_dotenv()



import os
from groq import Groq
client =Groq(api_key= os.getenv("GROQ_API"))


response = client.chat.completions.create(model="qwen/qwen3- 32b", messages =[
    {
        "role": "user", 
        "content" :"What is the capital of France."
    }
], temperature= 0.3,
)


print(response.choices[0].message.content)



