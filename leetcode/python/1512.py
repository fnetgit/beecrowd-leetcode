# Number of Good Pairs


class Solution(object):
    def numIdenticalPairs(self, nums):

        count = {}
        pairs = 0

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for quantity in count.values():
            pairs += quantity * (quantity - 1) // 2

        return pairs
