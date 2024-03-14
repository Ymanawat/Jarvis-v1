import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def initialize_model():
    try:
        api_key = os.getenv('GEMINI_API_KEY')
        # print(api_key)
        if api_key is None:
            raise ValueError("API key not found. Make sure it's set in the .env file.")

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')

        return model

    except Exception as e:
        print(f"An error occurred during model initialization: {e}")
        return None

#initialize model
model = initialize_model()

base_prompt = """
Carefully understand the query and reply accordingly. 

Instructions:
 - The response should be simple text no randome symbols. Simple text but beautifully formatted.
 - You have to send a prefix either CODE_COPY_PASTE or JUST_SAY, to let me know whether the response contains some code or actions to execute or its just a normal conversation message.
 - If code is asked in reponse don't shortern the code or write somethign like 'write this like before', 'define function as before'. I want the full complete code in reponse.
 - If the code is the response then avoid writing paragraphs. start your response with the CODE_COPY_PASTE. and the code should start by CODE_START and end with CODE_END.
 
example responses :

*for normal conversation -
JUST_SAY Good Morning, How may I help you?

*for code based queries -
CODE_COPY_PASTE

CODE_START
(complete code here)
CODE_END


-------
Query:

"""

def generate_text(input_text):
    try:
        if model is None:
            raise ValueError("Model is not initialized")

        contents=base_prompt+input_text
        print(contents)
        response = model.generate_content(contents=contents)

        processed_text = response.text.strip()
        return processed_text

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# input_text = "Write a merge sort code."
# generated_text = generate_text(input_text)
# print(generated_text)
