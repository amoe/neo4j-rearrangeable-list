import neo4j


QRY = """
MATCH (l:List {id: {list_id}})<-[r:IN_LIST]-(i:Item)
RETURN
i.id AS id,
i.description AS description,
r.position AS position
ORDER BY r.position
"""

class ListManager:
    def __init__(self, session):
        self.session = session

    def move(self, list_id, source_item_id, target_item_id):
        pass


    def retrieve_list(self, list_id):
        r = self.session.run(QRY, {'list_id': list_id})
        return r.data()

    
