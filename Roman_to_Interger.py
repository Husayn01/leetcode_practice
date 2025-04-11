class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        val = 0
        for i in range(len(s)):
            # If the current value is less than the next value, subtract it
            if i + 1 < len(s) and roman_numerals[s[i]] < roman_numerals[s[i + 1]]:
                val -= roman_numerals[s[i]]
            else:
                val += roman_numerals[s[i]]
        
        return val

# Example usage
sol = Solution()
print(sol.romanToInt("IX"))  # Output: 9
print(sol.romanToInt("LVIII"))  # Output: 58
print(sol.romanToInt("MCMXCIV"))  # Output: 1994
