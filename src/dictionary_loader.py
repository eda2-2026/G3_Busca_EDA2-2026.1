from .bst import binarySearchTree


def load_words(file_path: str) -> list[str]:
    """Carrega palavras de um arquivo de texto, uma por linha.
    Linhas em branco são ignoradas e quebras de linha são removidas.
    """
    words: list[str] = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            word = line.strip()
            if word:
                words.append(word)
    return words


def load_dictionary(file_path: str) -> binarySearchTree:
    """Carrega um dicionário de palavras em uma BST.
    Retorna a árvore binária de busca preenchida com todas as
    palavras encontradas no arquivo.
    """
    tree = binarySearchTree()
    for word in load_words(file_path):
        tree.insert(word)
    return tree
