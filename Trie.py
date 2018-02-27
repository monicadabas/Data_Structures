# Trie with a node as array of 26 nodes, each for a small alphabet

class TrieNode:
    def __init__(self):
        self.children = [None]*26  # we can also keep this as a dictionary with key as letter and value as a trie node
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def get_index(self, c):
        return ord(c.lower())- ord('a')

    def add_word(self, word):
        current = self.root
        for c in word:
            c_index = self.get_index(c)
            if current.children[c_index] is None:
                current.children[c_index]= TrieNode()
            current = current.children[c_index]

        current.isEnd = True

    def find_word(self, word):
        if self.root.children is None:
            return False

        current = self.root
        for c in word:
            c_index = self.get_index(c)
            if current.children[c_index] is not None:
                current = current.children[c_index]
            else:
                return False
        if current.isEnd:
            return True
        return False

    def _print_trie(self, node):
        if node.children is None:
            return

        f_words = []
        for i in range(26):
            words = []
            if node.children[i] is not None:
                if node.children[i].isEnd:
                    words.append(chr(i+ ord('a')))
                words.extend([chr(i+ ord('a'))+ word for word in
                              self._print_trie(node.children[i]) if word is not None])
            f_words.extend(words)
        return f_words

    def print_trie(self):
        if self.root.children is None:
            print("Empty Trie")
            return

        print(self._print_trie(self.root))

    def _delete(self, word, pos, node):
        if pos < len(word) and node.children[ord(word[pos].lower())-ord('a')] is not None:
            self._delete(word, pos+1, node.children[ord(word[pos].lower())-ord('a')])

        if node.children is None:
            node = None
        else:
            if pos == len(word):
                node.isEnd = False

    def delete(self,word):
        if self.root.children is None:
            print("Empty Trie")
            return

        self._delete(word, 0, self.root)

    def get_words_with_prefix(self, prefix):
        if self.root.children is None:
            print("Empty Trie")
            return

        current = self.root
        for letter in prefix:
            if current.children[ord(letter.lower())-ord('a')] is not None:
                current = current.children[ord(letter.lower())-ord('a')]

            else:
                print("Prefix not found")
                return

        return [prefix+word for word in self._print_trie(current)]