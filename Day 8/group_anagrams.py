class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams_map = {}
        
        for word in strs:
            key = ''.join(sorted(word))
            if key not in anagrams_map:
                anagrams_map[key] = []
            anagrams_map[key].append(word)
        return list(anagrams_map.values())
