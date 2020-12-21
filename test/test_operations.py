from neo4j_rearrangeable_list import ListManager
import pprint

INITIAL_EXPECTED_STATE = [
    {'description': 'Fry', 'id': 'a', 'position': 0},
    {'description': 'Bender', 'id': 'b', 'position': 1},
    {'description': 'Leela', 'id': 'c', 'position': 2}
]

def test_sanity(session):
    manager = ListManager(session)
    r = manager.retrieve_list(42)
    assert r == INITIAL_EXPECTED_STATE
    
