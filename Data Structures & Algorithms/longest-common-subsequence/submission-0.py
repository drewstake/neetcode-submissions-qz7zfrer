class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        smaller_len = min(len(text1),len(text2))
        temp1 = 0

        if len(text1) > len(text2):
            temp1 = text2
            text1 = temp1
            text2 = text1
            


        counts = []

        for i in range(len(text1)):
            counts.append(0)
            ptr1 = i
            ptr2 = 0
            while ptr1 < len(text1):
                if text1[ptr1] == text2[ptr2]:
                    counts[i] +=1
                    ptr1+=1
                    ptr2+=1
                else:
                    ptr2+=1
                    if ptr2 == len(text1):
                        break

        return max(counts)

