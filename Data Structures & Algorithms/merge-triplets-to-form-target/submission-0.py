class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = []

        for i in range(len(triplets[0])):
            res.append(max(triplets[0][i], triplets[1][i]))
        

        if res == target:
            return True
        return False