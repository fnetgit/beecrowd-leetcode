# Length of Last Word


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split()
        return len(a[-1])


s1 = Solution()
print(s1.lengthOfLastWord("Hello World"))
print(s1.lengthOfLastWord("   fly me   to   the moon  "))
print(s1.lengthOfLastWord("luffy is still joyboy"))
