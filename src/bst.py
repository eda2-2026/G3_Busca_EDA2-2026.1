# implementação da árvore binária de busca (BST)

class BSTNode:
    def __init__(self, word):
        self.word = word
        self.left = None
        self.right = None

class binarySearchTree:
    def __init__(self):
        self.root = None

# se a raiz estiver vazia, insere a palavra como raiz
    def insert(self, word):
        if self.root is None:
            self.root = BSTNode(word)

# mas se tiver raiz  e for menor que a raiz insere na esquerda 
# e se for maior insere na direita
    def _insert(self, current, word):
        if word < current.word:
            if current.left is None:
                current.left = BSTNode(word)
                
            else: 
                self._insert(current.left, word)
        elif word > current.word:
            if current.right is None:
                current.right = BSTNode(word)
            else:
                self.insert(current.right, word)
                
# Busca na árvore

    def search(self, word):
        return self._search(self.root, word)
    
    def _search(self, current, word):
        if current in None:
            return False
        if word == current.word:
            return True
        
        if word < current.word:
            return self._search(current.left, word)
        else:
            return self._search(current.right, word)
        
# inorder traversal

    def inorder(self):
        words = []
        self._inorder(self.root, words)
        return words
    
    def _inorder(self, current, words):
        if current is not None:
            self._inorder(current.left, words)
            words.append(current.word)
            self._inorder(current.right, words)