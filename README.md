# Athena's Asylum

Athena's Asylum is a document-aware AI assistant that uses the power of Claude 3.5 Sonnet to provide intelligent responses based on the context of a given PDF document.

## Project Description

This project creates a chatbot that can read and understand the contents of a PDF file, and then engage in a conversation with users based on that information. The bot uses the Anthropic API to leverage the Claude 3.5 Sonnet model for natural language processing and generation.

Key features:
- PDF text extraction and preprocessing
- Integration with Anthropic's Claude 3.5 Sonnet model
- Interactive chat interface
- Context-aware responses
- Witty and charming personality

## Requirements

- Python 3.7+
- `anthropic` library
- `pypdf` library

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/Athenas-Asylum.git
   cd Athenas-Asylum
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

Before running the bot, you need to set up two important variables in the `bot.py` file:

1. Set your Anthropic API key:
   ```python
   claude_api_key = "your_api_key_here"
   ```

2. Update the path to your PDF file:
   ```python
   pdf_path = "path/to/your/document.pdf"
   ```

## Usage

To run the chatbot, execute the following command in your terminal:

```
python bot.py
```

The bot will start by providing an icebreaker. You can then engage in a conversation by typing your messages. The bot will respond based on the context of the provided PDF document.

To end the conversation, simply type a message that indicates you want to terminate the chat (e.g., "goodbye", "exit", etc.). The bot will respond with a witty farewell message and end the session.