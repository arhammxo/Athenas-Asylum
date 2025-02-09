from neo4j import GraphDatabase
import spacy

class KnowledgeGraph:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.nlp = spacy.load("en_core_web_sm")
        
    def create_entities(self, text):
        doc = self.nlp(text)
        with self.driver.session() as session:
            for ent in doc.ents:
                session.execute_write(
                    self._create_entity, ent.text, ent.label_
                )
    
    @staticmethod
    def _create_entity(tx, text, label):
        query = (
            "MERGE (e:Entity {text: $text}) "
            "SET e.label = $label "
            "RETURN e"
        )
        tx.run(query, text=text, label=label)
    
    def query_related_entities(self, query):
        with self.driver.session() as session:
            result = session.execute_read(
                self._get_related_entities, query
            )
            return [record["entity"] for record in result]
    
    @staticmethod
    def _get_related_entities(tx, query):
        result = tx.run(
            "MATCH (e:Entity) WHERE toLower(e.text) CONTAINS toLower($query) RETURN e.text AS entity",
            parameters={"query": query}
        )
        return list(result) 