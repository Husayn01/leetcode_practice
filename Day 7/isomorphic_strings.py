class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping = {}

        for i in range(len(s)):
            if s[i] in mapping:
                if mapping[s[i]] != t[i]:
                    return False
            else:
                if t[i] in mapping.values():
                    return False
                mapping[s[i]] = t[i]

        return True


solution = Solution()

# Call the method
# print(solution.isIsomorphic("egg", "add"))
print(solution.isIsomorphic("badc", "baba")) 