class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
         """
         
        #Time limit exceeded for this: 
        # for i in range(len(nums)): 
        #     for j in range(len(nums)): 
        #         if nums[i]==nums[j] and i!=j: 
        #             return True
        # return False 
        
        if len(nums) > len(set(nums)): 
            return True
        else: 
            return False