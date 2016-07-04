class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        #With O(n^2) complexity, need to find a better way which is less complex
        # n = len(nums)  
        # for i in range(n):  
        #     count = 0 
        #     for j in range(n): 
        #         if nums[i]==nums[j]: 
        #             count +=1 
        #         if count > n/2:  
        #             return nums[i] 
                    
        #This is much better way, but needs to know sorted, set and count functions. 
        #The idea is to first find a unique set and then count each one of them in the original array 
        n = len(nums)
        unique = sorted(set(nums)) 
        for i in range(len(unique)): 
            if nums.count(unique[i]) >  n/2: 
               return unique[i] 