class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        char_to_word = {}
        used_words = set()
        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False
            else:
                if word in used_words:
                    return False
                char_to_word[char] = word
                used_words.add(word)
        return True
    
s = Solution()
print(s.wordPattern(pattern = "abba", s = "dog cat cat dog"))