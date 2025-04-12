class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ""
        num = 0
        for n in digits:
            s += str(n)
        num = int(s) + 1
        return [int(n) for n in str(num)]