# interface do usuário
from src.dictionary_loader import load_dictionary
from src.autocomplete import autocomplete
from src.spellchecker import suggest_corrections


def main():
    tree = load_dictionary("data/words.txt")

    while True:
        word = input("Digite a palavra/prefixo a ser procurada (ou 'sair' para encerrar): ").strip()
        if word.lower() == 'sair':
            break
        if not word:
            print("Digite uma palavra válida.")
            continue

        word_lower = word.lower()

        if tree.search(word_lower):
            # Palavra existe, mostrar autocomplete
            suggestions = autocomplete(tree, word_lower, limit=5)
            if suggestions:
                print("Palavra encontrada. Sugestões de autocomplete:")
                for s in suggestions:
                    print(f"- {s}")
            else:
                print("Palavra encontrada, mas nenhuma sugestão de autocomplete.")
        else:
            # Palavra não existe, mostrar correções ortográficas
            corrections = suggest_corrections(tree, word_lower, limit=5)
            if corrections:
                print("Palavra não encontrada. Sugestões de correção ortográfica:")
                for c in corrections:
                    print(f"- {c}")
            else:
                print("Palavra não encontrada e nenhuma sugestão de correção.")


if __name__ == "__main__":
    main()
