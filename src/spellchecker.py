from src.bst import binarySearchTree
from .autocomplete import autocomplete




def edit_distance(word1: str, word2: str) -> int:

    m = len(word1)
    n = len(word2)

    # matriz (m+1 x n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # inicialização
    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    # preencher matriz
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if word1[i - 1] == word2[j - 1]:
                cost = 0
            else:
                cost = 1

            dp[i][j] = min(
                dp[i - 1][j] + 1,      # remoção
                dp[i][j - 1] + 1,      # inserção
                dp[i - 1][j - 1] + cost  # substituição
            )

    return dp[m][n]

def suggest_corrections(
    tree: binarySearchTree,
    word: str,
    max_distance: int = 2,
    limit: int = 5,
) -> list[str]:

    if tree is None or not word:
        return []

    word = word.lower()

    # usar prefixo pequeno para filtrar
    prefix = word[:2]

    candidates_words = autocomplete(tree, prefix, limit=50)

    candidates = []

    for w in candidates_words:

        distance = edit_distance(word, w)

        if distance <= max_distance:
            candidates.append((w, distance))

    candidates.sort(key=lambda x: x[1])

    return [w for w, _ in candidates[:limit]]