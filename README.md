# Athena's Asylum 🤖📚

A context-aware AI assistant that combines document understanding, knowledge graphs, and witty personality to deliver intelligent responses.

## Features ✨

- **PDF Context Processing**: Extracts and analyzes text from PDF documents
- **Knowledge Graph Integration**: Stores entities and relationships in Neo4j
- **Vector Search**: FAISS-based semantic search for document context
- **Hybrid Reasoning**: Combines LLM capabilities with structured knowledge
- **Personality-infused Responses**: Witty and charming interaction style

## Technologies 🛠️

- **Natural Language Processing**: spaCy (en_core_web_sm)
- **Knowledge Graph**: Neo4j
- **LLMs**: Anthropic Claude 3 Sonnet & OpenAI Embeddings
- **Vector Store**: FAISS
- **Document Processing**: PyPDF, LangChain

## Installation ⚙️

1. Clone repository:
   ```bash
   git clone https://github.com/yourusername/athenas-asylum.git
   cd athenas-asylum
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```
3. Set up services:
- Install and run Neo4j locally
- Obtain API keys for Anthropic and OpenAI

## Configuration 🔧

1. Replace hardcoded credentials in:
- `llm_client.py` (Anthropic & OpenAI API keys)
- `vector_store.py` (OpenAI API key)
- `main.py` (Neo4j connection details)

2. Recommended security practice:
   ```bash
   # Replace hardcoded keys with environment variables:
   os.getenv("ANTHROPIC_API_KEY")
   os.getenv("OPENAI_API_KEY")
   ```

3. Place your PDF document in the project root as `r.pdf` or modify path in `main.py`

## Usage 🚀

```bash
python main.py
```

Example Interaction:
```bash
You: What's the main topic of the document?
Assistant: The document focuses on AI ethics - though I must say, 
          your choice of questions is as sharp as Athena's owl! 🦉
```

## Project Structure 🗂️

| File                | Purpose                                                                 | Key Components                          |
|---------------------|-------------------------------------------------------------------------|-----------------------------------------|
| `main.py`           | Entry point for application flow and user interaction                  | - Initializes all components<br>- Chat loop logic<br>- Context aggregation |
| `knowledge_graph.py`| Manages Neo4j knowledge graph operations                               | - Entity extraction with spaCy<br>- Cypher query execution<br>- Relationship mapping |
| `llm_client.py`     | Handles AI model interactions and response generation                  | - Claude-3 Sonnet integration<br>- OpenAI embeddings<br>- Personality system prompts |
| `pdf_processor.py`  | Processes PDF documents for text extraction and preparation            | - PyPDF text extraction<br>- Text cleaning<br>- Recursive chunking |
| `vector_store.py`   | Implements semantic search capabilities                                | - FAISS vector database<br>- OpenAI embeddings integration<br>- Context retrieval |
| `requirements.txt`  | Lists all project dependencies                                         | - NLP libraries<br>- Database drivers<br>- AI service SDKs |

## Development Requirements 🔨

**Core Prerequisites**
- Python 3.9+ with pip package manager
- Neo4j Desktop (v4.4+) running locally
- 4GB+ RAM for optimal performance

**API Access**
- ✅ Valid Anthropic API key (Claude-3 access)
- ✅ OpenAI API key (text-embedding-3-small model)
- Active internet connection for LLM services

**Recommended Setup**
1. Create virtual environment:
   ```bash
   python -m venv athena_env
   source athena_env/bin/activate  # Linux/Mac
   ```
2. Configure Neo4j:
   ```bash
   neo4j start
   # Set password to 'your_password' or update in main.py
   ```

## License & Attribution 📜
MIT License - Full text available in LICENSE file

### Third-Party Services

- Anthropic Claude-3 Sonnet (Terms)

- OpenAI Embeddings (Policies)

- Neo4j Community Edition (License)

### Hot Tips 🔥

1. For complex PDFs: Pre-process with OCR using pdf_processor.py extensions

2. Visualize knowledge graph: Access Neo4j Browser at http://localhost:7474

3. Try hybrid queries: "Explain Section 2.3 using both document context and knowledge graph entities"

`"Wisdom begins in wonder" - Socrates (Athena's favorite philosopher) 🏛️`