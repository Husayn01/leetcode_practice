class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_pal = ""
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substr = s[i:j]
                if substr == substr[::-1] and len(substr) > len(max_pal):
                    max_pal = substr
        return max_pal
            

s = Solution()
print(s.longestPalindrome("cbbh"))