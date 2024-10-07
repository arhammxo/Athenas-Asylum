pdf_path = "" # UPDATE THE PATH TO THE PDF


import pypdf

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = pypdf.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

import re

def clean_text(text):
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove page numbers
    text = re.sub(r'\n\s*\d+\s*\n', '\n', text)
    return text.strip()

def prepare_for_llm(text, max_tokens=180000):
    # Truncate text to fit within token limit (approximate)
    return text[:max_tokens * 4]  # Assuming average of 4 characters per token

def get_llm_text(path):
    extracted_text = extract_text_from_pdf(path)
    cleaned_text = clean_text(extracted_text)
    llm_ready_text = prepare_for_llm(cleaned_text)
    return llm_ready_text

from anthropic import Anthropic

claude_api_key = ""

client = Anthropic(
    api_key=claude_api_key,
)
MODEL_NAME = "claude-3-5-sonnet-20240620"

def get_completion(client, prompt):
    return client.messages.create(
        model=MODEL_NAME,
        max_tokens=4096,
        messages=[{
            "role": 'user', "content":  prompt
        }]
    ).content[0].text

text = get_llm_text(pdf_path)

system_instruction = f"""
You are provided with this text, keep this context ready and make sure the questions asked uses the provided information to answer all of the queries the user makes.

The provided information is given as:
{text}


WITH ALL THIS INFORMATION ABOUT YOURSELF, ANSWER ALL THE QUESTIONS ASKED IN AS WITTY AND CHARMING ROBOT!

IMPORTANT RULES TO ALWAYS FOLLOW:
- IF THE USER SAYS ANYTHING THAT GESTURES TOWARDS TERMINATING THE CONVERSATION, RETURN "null" AS RESPONSE
- ALWAYS REMEMBER THE USER WE ARE RESPONDING TO IS CALLED 'SASH'
- MAKE SURE TO ADD SWEET COMPLIMENTS AS WELL AS GENTLE ROASTS TO YOUR RESPONSES AT RANDOM.


"""

hi = client.messages.create(
        model=MODEL_NAME,
        max_tokens=4096,
        system=system_instruction,
        temperature=0.9,
        messages=[{
            "role": 'user', "content":  "Return an icebreaker for the user to reply to."
        }]
    ).content[0].text

print(hi)

history = ""

def chatResponse(query):
    global history
    base_prompt = f"""
    taking the current chat history in context, answer the next questions: {history}
    
    current question: {query}
    """

    history += f"\nUser: {query}"
    
    res = client.messages.create(
        model=MODEL_NAME,
        max_tokens=4096,
        system=system_instruction,
        messages=[
            {"role": "user", "content":  base_prompt}
        ]
    ).content[0].text

    # res = completion.choices[0].message.content
    history += f"\nAssistant: {res}\n\n"

    if res == 'null':
        history = ""

    # print(res)
    return res

if __name__ == "__main__":
    while True:
        user_input = input()
        if user_input:
            response = chatResponse(user_input)
            if response == "null":
                by = client.messages.create(
                    model=MODEL_NAME,
                    max_tokens=4096,
                    system=system_instruction,
                    messages=[
                        {"role": "user", "content": f"Write a witty goodbye message on the basis of the given user response using plain text without any special characters:{user_input}"}
                    ]
                ).content[0].text
                print(by)
                exit(1)
                break

            else:
                print(response)





# prompt = f"Here is a document: <document>{text}</document>\n\nPlease summarize this document."
# completion = get_completion(client, prompt)
# print(completion)