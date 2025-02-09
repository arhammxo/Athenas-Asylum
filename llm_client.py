from anthropic import Anthropic
import os
from langchain_openai import OpenAIEmbeddings

class LLMClient:
    def __init__(self):
        self.claude = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        self.openai_embeddings = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))
        self.system_instruction = """
            You are a witty and charming AI assistant. Follow these rules:
            1. Use retrieved context to answer questions
            2. For unknown information, say "I'm not sure, but let me think..."
            3. Maintain conversation history context
            4. Add sweet compliments/gentle roasts randomly
            5. Return "null" for goodbye gestures
        """
    
    def get_response(self, prompt, history, context):
        message = self.claude.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=4096,
            system=self.system_instruction,
            messages=[{
                "role": "user",
                "content": f"Context: {context}\nHistory: {history}\nQuestion: {prompt}"
            }]
        )
        return message.content[0].text 