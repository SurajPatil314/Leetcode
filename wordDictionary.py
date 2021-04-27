"""
https://leetcode.com/problems/design-add-and-search-words-data-structure/


Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
 word may contain dots '.' where dots can be matched with any letter.

"""


class WordDictionary:
    li = defaultdict(list)

    def __init__(self):
        self.li = defaultdict(list)

    def addWord(self, word: str) -> None:
        if word not in self.li[len(word)]:
            self.li[len(word)].append(word)

    def search(self, word: str) -> bool:

        for i in (self.li[len(word)]):
            for i1 in range(len(word)):
                if word[i1] != '.':
                    if i1 == len(word) - 1:
                        if word[i1] == i[i1]:
                            return True
                    else:
                        if word[i1] != i[i1]:
                            break
                else:
                    if i1 == len(word) - 1:
                        return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)