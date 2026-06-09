# Majority Element


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        di = {}
        for n in nums:
            di[n] = di.get(n, 0) + 1
        return max(di, key=di.get)
