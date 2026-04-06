from src.bst import binarySearchTree
from src.spellchecker import suggest_corrections, edit_distance


def build_test_tree():

    tree = binarySearchTree()

    words = [
        "casa",
        "casal",
        "casaco",
        "cachorro",
        "carro",
        "carta",
        "casinha",
    ]

    for w in words:
        tree.insert(w)

    return tree


def test_edit_distance_equal_words():
    assert edit_distance("casa", "casa") == 0


def test_edit_distance_insertion():
    assert edit_distance("casa", "casas") == 1


def test_edit_distance_removal():
    assert edit_distance("casas", "casa") == 1


def test_edit_distance_substitution():
    assert edit_distance("casa", "cata") == 1


def test_edit_distance_multiple_changes():
    assert edit_distance("kitten", "sitting") == 3


def test_suggest_corrections_basic():

    tree = build_test_tree()

    suggestions = suggest_corrections(tree, "casaa")

    assert "casa" in suggestions


def test_suggest_corrections_limit():

    tree = build_test_tree()

    suggestions = suggest_corrections(tree, "casaa", limit=2)

    assert len(suggestions) <= 2


def test_suggest_corrections_no_result():

    tree = build_test_tree()

    suggestions = suggest_corrections(tree, "zzzzz")

    assert suggestions == []


def test_suggest_empty_word():

    tree = build_test_tree()

    suggestions = suggest_corrections(tree, "")

    assert suggestions == []