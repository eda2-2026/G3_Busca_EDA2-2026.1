# interface do usuário
from src.dictionary_loader import load_dictionary
from src.autocomplete import autocomplete


def main():
    tree = load_dictionary("data/palavras.txt")

    word = input("Digite a palavra/prefixo a ser procurada: ")
    suggestions = autocomplete(tree, word, limit=5)

    if suggestions:
        print("Sugestões:")
        for s in suggestions:
            print("-", s)
    else:
        print("Nenhuma palavra encontrada.")


if __name__ == "__main__":
    main()
