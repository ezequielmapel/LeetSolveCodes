class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        min_word = min(strs)

        for i, l in enumerate(min_word):
            prefix +=l
            for w in strs:
                if w[:i+1] != prefix:
                    return prefix[:i]
        return prefix

