# Roman to Integer


class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        max_saw = 0
        for c in reversed(s):
            n = romans[c]
            if n < max_saw:
                total -= n
            else:
                total += n
                max_saw = n
        return total
