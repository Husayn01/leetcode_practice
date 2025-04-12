class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)  # Convert x to string once
        return s == s[::-1]  # Compare the string with its reverse


# n = [1,2,3,4]
# for i in range(len(n) -1, -1, -1):
#     print(n[i])