
# Check if an integer is a power of 4, return True if yes else False
# Most problems were happening with cases of 1,2,3,4,8 and 12
# Find a more optimal solution without using so many explicit corner cases


class Solution(object):

    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """

        # if num<=3 hello:
        #     return False

        while num / 4 >= 1:
            if num % 4 == 0:
                num = num / 4
            else:
                return False

        if num == 1:
            return True

        return False if num <= 3 else True
