# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        anagrams = []
        for word in words:
            if self.is_anagram(word):
                anagrams.append(word)
        return anagrams

    def is_anagram(self, word):
        return sorted(self.word) == sorted(word)