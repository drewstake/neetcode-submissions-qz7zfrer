class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        high = 0
        for x1, y1 in points:
            dist = math.sqrt((x1 - 0)**2 + (y1 - 0)**2)
            if dist == high:
                res.append([x1,y1])
            else:
                high = max(high,dist)
                res.append([x1,y1])
            if len(res) == k:
                return res
