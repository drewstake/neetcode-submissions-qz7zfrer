class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        freqt = {}

        if len(s) != len (t):
            return False

        for i in s: 
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for i in t: 
            if i in freqt:
                freqt[i]+=1
            else:
                freqt[i]=1
        
        if freq == freqt:
            return True
        else:
            return False

        


            
            