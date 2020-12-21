from neo4j_rearrangeable_list import ListManager
import neo4j
import pprint

driver = neo4j.GraphDatabase.driver("bolt://localhost:7687", auth=('neo4j', 'password'))
with driver.session() as session:
    manager = ListManager(session)
    pprint.pprint(manager.retrieve_list(42))

            
