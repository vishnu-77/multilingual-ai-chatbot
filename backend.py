# backend.py - Minimal LLM Backend
from groq import Groq

class MultilingualChatbot:
    def __init__(self):
        self.client = Groq(api_key="API_KEY")
    
    def chat(self, message, language="English", history=[]):
        # Add system message for language
        messages = [
            {"role": "system", "content": f"Reply in {language}"}
        ]
        
        # Add chat history
        messages.extend(history)
        
        # Add current message
        messages.append({"role": "user", "content": message})
        
        # Get response from Groq
        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7
        )
        
        return response.choices[0].message.content