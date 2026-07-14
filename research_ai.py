import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "gemma3:latest"

def research_assistant(text):

    prompt = f"""
You are an AI Research Assistant.

Research Text:
{text}

Provide:

1. Summary
2. Key Points
3. Explain difficult concepts
4. Possible applications

Keep the answer short and easy to understand.
"""

    try:

        response = requests.post(

            OLLAMA_URL,

            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            }

        )

        return response.json()["response"]

    except:

        return "Unable to connect to Ollama."