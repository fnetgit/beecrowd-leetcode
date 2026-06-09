# Majority Element


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        candidate = 0
        for n in nums:
            if count == 0:
                candidate = n
                count += 1
            else:
                if n == candidate:
                    count += 1
                else:
                    count -= 1
        return candidate

