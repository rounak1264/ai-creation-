# AI Chatbot using OpenAI API

This is a simple AI chatbot built using Python and the OpenAI API.

## Prerequisites

- Python 3.7 or higher
- An OpenAI API key

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Set your OpenAI API key as an environment variable:
   - On Windows: `set OPENAI_API_KEY=your_api_key_here`
   - Or create a `.env` file in the project root with `OPENAI_API_KEY=your_api_key_here` and use python-dotenv.

## Usage

Run the chatbot:
```
python python/main.py
```

Type your messages and press Enter. The AI will respond. Type 'quit' to exit.

## Troubleshooting

- Ensure your API key is set correctly.
- Check your OpenAI account for usage limits.
- If you get import errors, make sure dependencies are installed.