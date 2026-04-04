from src.bst import binarySearchTree
from src.autocomplete import autocomplete


def build_tree(words: list[str]) -> binarySearchTree:
    tree = binarySearchTree()
    for w in words:
        tree.insert(w)
    return tree


def test_autocomplete_multiple_results():
    words = ["manga", "mangaio", "banana", "mando", "uva", "abacate"]
    tree = build_tree(words)

    result = autocomplete(tree, "man")

    # resultado deve vir ordenado e só com palavras que começam com "man"
    assert result == ["mando", "manga", "mangaio"]


def test_autocomplete_single_result():
    words = ["manga", "banana", "uva"]
    tree = build_tree(words)

    result = autocomplete(tree, "uva")

    assert result == ["uva"]


def test_autocomplete_no_results():
    words = ["manga", "banana", "uva"]
    tree = build_tree(words)

    result = autocomplete(tree, "xyz")

    assert result == []


def test_autocomplete_with_limit():
    words = ["manga", "mangaio", "mando", "mano", "manga2"]
    tree = build_tree(words)

    result = autocomplete(tree, "man", limit=2)

    expected = sorted([w for w in words if w.startswith("man")])[:2]
    assert result == expected
