import neo4j

QRY_FIXTURE = """
CREATE
  (l:List {id: 42, name: "Stuff"}),
  (i1:Item {id: "a", description: "Fry"}),
  (i2:Item {id: "b", description: "Bender"}),
  (i3:Item {id: "c", description: "Leela"}),
  (i4:Item {id: "d", description: "Hermes"}),
  (i5:Item {id: "e", description: "Amy"}),
  (i1)-[:IN_LIST {position: 0}]->(l),
  (i2)-[:IN_LIST {position: 1}]->(l),
  (i3)-[:IN_LIST {position: 2}]->(l),
  (i4)-[:IN_LIST {position: 3}]->(l),
  (i5)-[:IN_LIST {position: 4}]->(l)
"""

driver = neo4j.GraphDatabase.driver("bolt://localhost:7687", auth=('neo4j', 'password'))
with driver.session() as session:
    session.run("MATCH (n) DETACH DELETE n")
    session.run(QRY_FIXTURE)
