class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
        # for i in range(0, len(nums)):
        #     if target not in nums:
        #         if nums[-1] < target:
        #             return len(nums)
        #         if nums[0] > target:
        #             return 0
        #         if target > nums[i] and target < nums[i + 1]:
        #             nums.insert(i + 1, target)
        #             return i + 1
        #     if nums[i] == target:
        #         return i
            
print(Solution().searchInsert(nums = [1,3,5,6], target = 7))
print(Solution().searchInsert(nums = [1,3,5,6], target = 0))