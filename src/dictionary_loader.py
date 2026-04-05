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

    def _insert_balanced(
        tree: binarySearchTree, words: list[str], start: int, end: int
    ) -> None:
        """Insere palavras no meio de cada intervalo para manter a BST balanceada."""
        if start > end:
            return

        mid = (start + end) // 2  # divisão inteira
        tree.insert(words[mid])
        _insert_balanced(tree, words, start, mid - 1)
        _insert_balanced(tree, words, mid + 1, end)

    tree = binarySearchTree()

    # Evita árvore degenerada quando o arquivo já vem ordenado.
    unique_sorted_words = sorted(set(load_words(file_path)))
    _insert_balanced(
        tree, unique_sorted_words, 0, len(unique_sorted_words) - 1
    )  # começo da recursão

    return tree
