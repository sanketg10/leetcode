class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: 
            return False 
        if x < 10 : 
            return True
        x = str(x)
        l = len(x)
        for i in range(1,l):
            if x[i-1]==x[-i]: 
                    continue 
            else: 
                    return False
        return True 