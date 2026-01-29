class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in nums_dict:
                return [index, nums_dict[complement]]
            nums_dict[num] = index
            