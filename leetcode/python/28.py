# Find the Index of the First Occurrence in a String


class Solution:
    def strStr(self, haystack: str, needle: str) -> int | None | str:
        for i, c in enumerate(haystack):
            if haystack[i : i + len(needle)] == needle:
                return i
            else:
                continue
        return -1
