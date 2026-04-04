from src.bst import binarySearchTree


def autocomplete(
    tree: binarySearchTree, prefix: str, limit: int | None = None
) -> list[str]:
    """Retorna palavras da BST que começam com o prefixo dado.
    As palavras são retornadas em ordem alfabética (baseado em inorder).
    Se ``limit`` for informado, no máximo ``limit`` sugestões são retornadas.
    """
    if tree is None or prefix is None:
        return []

    # obtém todas as palavras em ordem alfabética
    all_words = tree.inorder()

    # filtra apenas as que começam com o prefixo
    suggestions = [word for word in all_words if word.startswith(prefix)]

    # aplica limite, se houver
    if limit is not None:
        suggestions = suggestions[:limit]

    return suggestions
