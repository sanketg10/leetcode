class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums3=[]
        for i in range (len(nums1)): 
                for j in range (len(nums2)): 
                           
                    if nums1[i] == nums2[j] and nums2[j] not in nums3: 
                        nums3.append(nums2[j]) 
        return nums3 
        