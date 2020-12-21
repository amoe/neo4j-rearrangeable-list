import neo4j
import pytest


QRY_FIXTURE = """
CREATE
  (l:List {id: 42, name: "Stuff"}),
  (i1:Item {id: "a", description: "Fry"}),
  (i2:Item {id: "b", description: "Bender"}),
  (i3:Item {id: "c", description: "Leela"}),
  (i1)-[:IN_LIST {position: 0}]->(l),
  (i2)-[:IN_LIST {position: 1}]->(l),
  (i3)-[:IN_LIST {position: 2}]->(l)
"""

@pytest.fixture(scope='module')
def session():
    # load data here
    driver = neo4j.GraphDatabase.driver("bolt://localhost:7687", auth=('neo4j', 'password'))
    with driver.session() as session:
        session.run("MATCH (n) DETACH DELETE n")
        session.run(QRY_FIXTURE)
        yield session

            
