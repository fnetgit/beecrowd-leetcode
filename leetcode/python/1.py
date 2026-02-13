# To Sum


class Solution(object):
    def twoSum(self, nums, target):
        for i, num in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if num + nums[j] == target:
                    return [i, j]
