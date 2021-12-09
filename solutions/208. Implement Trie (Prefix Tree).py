"""
Runtime: 372 ms, faster than 7.49% of Python3 online submissions for Implement Trie (Prefix Tree).
Memory Usage: 26.1 MB, less than 95.33% of Python3 online submissions for Implement Trie (Prefix Tree).
"""
from typing import List
from typing import Optional

class TrieNode:
    def __init__(self, char, alt=None, nxt=None):
        self.char = char
        self.alt = alt
        self.nxt = nxt

class Trie:

    def __init__(self):
        self.head = None

    def insert(self, word: str) -> None:
        list_word = list(word)
        list_word.append('-')
        word_head = self.list2Trie(list_word)
        if self.head is None:
            self.head = word_head
        else:
            p1 = self.head
            previous_p1 = None
            p2 = word_head
            while p1 is not None and p2 is not None:
                horizontal_end = False
                vertical_end = False
                if p1.char == p2.char:
                    previous_p1 = p1
                    p1 = p1.nxt
                    p2 = p2.nxt
                    if p1 is None:
                        vertical_end = True
                else:
                    previous_p1 = p1
                    p1 = p1.alt
                    if p1 is None:
                        horizontal_end = True
            if p2 is not None and vertical_end:
                previous_p1.nxt = p2
            elif p2 is not None and horizontal_end:
                previous_p1.alt = p2        

    def search(self, word: str) -> bool:
        list_word = list(word)
        list_word.append('-')
        word_head = self.list2Trie(list_word)
        if self.head is None:
            self.head = word_head
        else:
            p1 = self.head
            previous_p1 = None
            p2 = word_head
            while p1 is not None and p2 is not None:
                horizontal_end = False
                vertical_end = False
                if p1.char == p2.char:
                    previous_p1 = p1
                    p1 = p1.nxt
                    p2 = p2.nxt
                    if p2 is None:
                        return True
                else:
                    previous_p1 = p1
                    p1 = p1.alt
            return False

    def startsWith(self, prefix: str) -> bool:
        word_head = self.list2Trie(list(prefix))
        if self.head is None:
            self.head = word_head
        else:
            p1 = self.head
            previous_p1 = None
            p2 = word_head
            while p1 is not None and p2 is not None:
                horizontal_end = False
                vertical_end = False
                if p1.char == p2.char:
                    previous_p1 = p1
                    p1 = p1.nxt
                    p2 = p2.nxt
                    if p2 is None:
                        return True
                else:
                    previous_p1 = p1
                    p1 = p1.alt
            return False
        
    def list2Trie(self, list_word: List) -> TrieNode:
        for idx, c in enumerate(list_word):
            temp_node = TrieNode(c)
            if idx == 0:
                word_head = temp_node
                previous = temp_node
            else:
                previous.nxt = temp_node
                previous = temp_node
        return word_head

def main():
    ans = []
    trie = Trie()
    trie.insert("apple");
    ans.append(trie.search("apple"))
    ans.append(trie.search("app"))
    ans.append(trie.startsWith("app"))
    trie.insert("app");
    ans.append(trie.search("app"))
    print('Output:', ans)
    print('Expected:', [True, False, True, True])

if __name__ == "__main__":
    main()
