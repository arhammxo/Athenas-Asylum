from pdf_processor import get_llm_text, chunk_text
from vector_store import create_vector_store
from knowledge_graph import KnowledgeGraph
from llm_client import LLMClient
import os

def main():
    # Initialize components
    pdf_path = "path_to_pdf.pdf"
    text = get_llm_text(pdf_path)
    chunks = chunk_text(text)
    
    # Create vector store
    vector_store = create_vector_store(chunks)
    
    # Initialize knowledge graph
    kg = KnowledgeGraph(
        uri="bolt://localhost:7687",
        user="neo4j",
        password=os.getenv("NEO4J_PASSWORD")
    )
    
    # Add temporary connection test (remove after verification)
    try:
        kg.driver.verify_connectivity()
        print("✅ Successfully connected to Neo4j database")
    except Exception as e:
        print(f"❌ Connection failed: {str(e)}")
        exit(1)
    
    kg.create_entities(text)  # Existing code
    
    # Initialize LLM client
    llm_client = LLMClient()
    
    # Chat loop
    history = ""
    while True:
        user_input = input("You: ")
        if not user_input:
            continue
            
        # Retrieve context
        docs = vector_store.similarity_search(user_input, k=3)
        context = "\n".join([d.page_content for d in docs])
        entities = kg.query_related_entities(user_input)
        
        # Get response
        response = llm_client.get_response(
            prompt=user_input,
            history=history,
            context=f"Document Context: {context}\nRelated Entities: {entities}"
        )
        
        print(f"Assistant: {response}")
        history += f"\nUser: {user_input}\nAssistant: {response}"
        
        if response.lower() == "null":
            print("Assistant: Until next time! 😊")
            break

if __name__ == "__main__":
    main() 