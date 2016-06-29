class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """

        ## Solution 1  ##
        return s[::-1]
        
        ## Solution 2   ##
        # return "".join(reversed(s)) 

        #######################
        ####Test bench#########
        ####################### 
        
        # string_rev = ''
        # l = len(s) 

        # for i in range (l): 
        #     string_rev = string_rev + s[l-i-1] 

        # return string_rev   