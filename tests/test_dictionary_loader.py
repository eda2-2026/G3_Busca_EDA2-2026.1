from src.dictionary_loader import load_words, load_dictionary


def test_load_words(tmp_path):
    file = tmp_path / "words.txt"
    file.write_text("banana\n\n  manga  \n uva\n", encoding="utf-8")

    words = load_words(str(file))

    assert words == ["banana", "manga", "uva"]


def test_load_dictionary(tmp_path):
    file = tmp_path / "words.txt"
    file.write_text("banana\nmanga\nuva\n", encoding="utf-8")

    tree = load_dictionary(str(file))

    # todas as palavras do arquivo devem estar na BST
    for w in ["banana", "manga", "uva"]:
        assert tree.search(w) is True

    # uma palavra que não está no arquivo não deve ser encontrada
    assert tree.search("abacate") is False


def test_load_full_dictionary():
    file = "data/words.txt"
    tree = load_dictionary(file)

    assert tree.search("coqueiro") is True
    assert tree.search("balão") is True
    assert tree.search("roseira") is True
    assert tree.search("word") is False
