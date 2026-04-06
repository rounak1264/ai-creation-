import openai
import os

# Initialize the OpenAI client with API key from environment variable
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def main():
    print("AI Chatbot using OpenAI API")
    print("Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            break
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}]
            )
            print("AI:", response.choices[0].message.content)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main() 

