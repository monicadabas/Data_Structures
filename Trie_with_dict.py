# Trie with a node as dictionary of character: TrieNode
# With this we cannot have words sorted lexicographically unless we sort them

class TrieNodeDict:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class TrieDict:
    def __init__(self):
        self.root = TrieNodeDict()

    def add_word(self, word):
        current = self.root
        for w in word:
            if w not in current.children:
                current.children[w] = TrieNodeDict()
            current = current.children[w]
        current.isEnd = True

    def find_word(self, word):
        if not self.root.children:
            print("Empty Trie")
            return False

        current = self.root

        for w in word:
            if w in current.children:
                current = current.children[w]

            else:
                return False

        if current.isEnd:
            return True
        else:
            return False

    def _print_trie(self, node):
        words = []
        if node.children:
            for child in node.children:
                if node.children[child].isEnd:
                    words.append(child)
                words.extend([child+word for word in self._print_trie(node.children[child])])
        return words

    def print_trie(self):
        if not self.root.children:
            print("Empty Trie")

        else:
            print(self._print_trie(self.root))

    def get_words_with_prefix(self, prefix):
        if not self.root.children:
            print("Empty Trie")
            return False

        current = self.root

        for letter in prefix:
            if letter in current.children:
                current = current.children[letter]
            else:
                print("Prefix not found")
                return

        return [prefix + word for word in self._print_trie(current)]

    def _delete_word(self, word, pos, node):
        if pos < len(word) and word[pos] in node.children:
            self._delete_word(word, pos+1, node.children[word[pos]])

        if pos == len(word):
            node.isEnd = False

        if not node.children:
            node = None

    def delete_word(self, word):
        if not self.root.children:
            print("Empty Trie")

        else:
            self._delete_word(word, 0, self.root)


