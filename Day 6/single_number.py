class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for n in nums:
            if nums.count(n) < 2:
                return n
        