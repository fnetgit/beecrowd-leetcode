# Length of Last Word


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split()
        return len(a[-1])
