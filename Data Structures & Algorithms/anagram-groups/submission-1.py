class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        # loop through dictionary, return

        freq = [0]*26
        dictionary = defaultdict(list)
        for string in strs:
            freq = [0]*26
            for char in string:
                asci = ord(char) - 97
                freq[asci] +=1
            
            tup = tuple(freq)

            dictionary[tup].append(string)

        return list(dictionary.values())
