from neo4j_rearrangeable_list import ListManager
import pprint

INITIAL_EXPECTED_STATE = [
    {'description': 'Fry', 'id': 'a', 'position': 0},
    {'description': 'Bender', 'id': 'b', 'position': 1},
    {'description': 'Leela', 'id': 'c', 'position': 2},
    {'description': 'Hermes', 'id': 'd', 'position': 3},
    {'description': 'Amy', 'id': 'e', 'position': 4}
]


# If Bender is dropped on Hermes, he bumps Hermes up one.
STATE_AFTER_MOVE = [
    {'description': 'Fry', 'id': 'a', 'position': 0},
    {'description': 'Leela', 'id': 'c', 'position': 1},
    {'description': 'Hermes', 'id': 'd', 'position': 2},
    {'description': 'Bender', 'id': 'b', 'position': 3},
    {'description': 'Amy', 'id': 'e', 'position': 4}
]

STATE_AFTER_ADD = [
    {'description': 'Fry', 'id': 'a', 'position': 0},
    {'description': 'Bender', 'id': 'b', 'position': 1},
    {'description': 'Leela', 'id': 'c', 'position': 2},
    {'description': 'Hermes', 'id': 'd', 'position': 3},
    {'description': 'Amy', 'id': 'e', 'position': 4},
    {'description': 'Zoidberg', 'id': 'f', 'position': 5}
]

STATE_AFTER_DELETE = [
    {'description': 'Fry', 'id': 'a', 'position': 0},
    {'description': 'Bender', 'id': 'b', 'position': 1},
    {'description': 'Hermes', 'id': 'd', 'position': 2},
    {'description': 'Amy', 'id': 'e', 'position': 3}
]


def test_sanity(session):
    manager = ListManager(session)
    r = manager.retrieve_list(42)
    assert r == INITIAL_EXPECTED_STATE

def test_move(session):
    manager = ListManager(session)
    manager.move(42, 'b', 'd')   
    assert manager.retrieve_list(42) == STATE_AFTER_MOVE

def test_add(session):
    manager = ListManager(session)
    manager.add_item(42, 'f', "Zoidberg")   
    assert manager.retrieve_list(42) == STATE_AFTER_ADD

def test_delete(session):
    manager = ListManager(session)
    manager.delete_item(42, 'c')
    assert manager.retrieve_list(42) == STATE_AFTER_DELETE
