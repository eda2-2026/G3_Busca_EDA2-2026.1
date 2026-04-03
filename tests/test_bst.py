import pytest

from src.bst import binarySearchTree


def test_insert_and_search():
    tree = binarySearchTree()
    words = ["manga", "banana", "uva", "abacate"]

    for w in words:
        tree.insert(w)

    # palavras inseridas devem ser encontradas
    for w in words:
        assert tree.search(w) is True

    # palavra não inserida não deve ser encontrada
    assert tree.search("laranja") is False


def test_inorder():
    tree = binarySearchTree()
    words = ["manga", "banana", "uva", "abacate"]

    for w in words:
        tree.insert(w)

    inorder_list = tree.inorder()

    # inorder de uma BST deve vir ordenado
    assert inorder_list == sorted(set(words))
