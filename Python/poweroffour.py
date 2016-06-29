
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """ 
        
        # if num<=3 hello:
        #     return False 
            
        while num/4 >= 1: 
            if num%4 == 0:  
                num = num/4 
            else: 
                return False
        
        if num==1: 
            return True 
            
        return False if num<=3 else True   
