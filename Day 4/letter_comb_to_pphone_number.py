class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        keypad = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        output = []
        if digits == "":
            return output

        for digit in digits:
            if digit in keypad:
                output.append(keypad[digit])

        # Now combine all lists in `output`
        res = [""]  # start with an empty string
        for group in output:
            temp = []
            for prefix in res:
                for letter in group:
                    temp.append(prefix + letter)
            res = temp

        return res



s = Solution()
print(s.letterCombinations("23"))
print(s.letterCombinations("2"))