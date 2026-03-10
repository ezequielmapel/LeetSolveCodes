class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        newWord = ""
        min_len = min(len(word1), len(word2))
        max_len = max(len(word1), len(word2))

        for i in range(min_len):
            newWord = newWord + word1[i] + word2[i]

        newWord = newWord + word1[min_len:]
        newWord = newWord + word2[min_len:]
        return newWord