class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """ 
        if n<=0:
            return False 
            
        while n/2 >= 1: 
            if n%2 == 0:  
                 n = n/2 
            else: 
                 return False
            
        
        return True