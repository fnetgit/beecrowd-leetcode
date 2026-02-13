# To Sum


class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for i, num in enumerate(nums):
            complemento = target - num
            if complemento in dic:
                return [dic[complemento], i]
            dic[num] = i
