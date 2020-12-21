import neo4j

QRY = """
MATCH (l:List {id: {list_id}})<-[r:IN_LIST]-(i:Item)
RETURN
i.id AS id,
i.description AS description,
r.position AS position
ORDER BY r.position
"""

MOVE_QUERY = """
MATCH (l:List {id: {list_id}}),
      (i1:Item {id: {source_item_id}})-[r1:IN_LIST]->(l),
      (i2:Item {id: {target_item_id}})-[r2:IN_LIST]->(l)
WITH
    r1.position AS oldPosition,
    r2.position AS newPosition,
    r1 AS r1,
    l AS l,
    i1 AS i1,
    CASE
      WHEN r2.position < r1.position THEN 1
      WHEN r2.position > r1.position THEN -1
      ELSE 0
    END AS signum
 MATCH (:Item)-[r3:IN_LIST]->(l)
WHERE
   (newPosition < oldPosition
   AND r3.position >= newPosition AND r3.position < oldPosition)
   OR (newPosition > oldPosition
   AND r3.position > oldPosition AND r3.position <= newPosition)
SET r3.position = r3.position + signum, r1.position = newPosition
RETURN i1
"""

ADD_QUERY = """
MATCH (l:List {id: {list_id}})
OPTIONAL MATCH (l)<-[r:IN_LIST]-(:Item)
WITH
    COALESCE(MAX(r.position) + 1, 0) AS newLast,
    l AS l
CREATE
  (i:Item {description: {new_description}, id: {new_id}}),
  (i)-[:IN_LIST {position: newLast}]->(l)
RETURN i
"""

class ListManager:
    def __init__(self, session):
        self.session = session

    def move(self, list_id, source_item_id, target_item_id):
        r = self.session.run(MOVE_QUERY, {
            'list_id': list_id,
            'source_item_id': source_item_id,
            'target_item_id': target_item_id
        })
        return r.data()

    def retrieve_list(self, list_id):
        r = self.session.run(QRY, {'list_id': list_id})
        return r.data()

    def add_item(self, list_id, new_id, new_description):
        r = self.session.run(
            ADD_QUERY,
            {'list_id': list_id,
             'new_description': new_description,
             'new_id': new_id}
        )
        return r.data()
