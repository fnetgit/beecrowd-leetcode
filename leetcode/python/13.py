# Roman to Integer


class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        nums = []
        for i in s:
            nums.append(romans[i])
        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                total -= nums[i]
            elif nums[i + 1] <= nums[i]:
                total += nums[i]
        total += nums[-1]
        print(total)
        return total
