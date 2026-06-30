class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hashMap = {}
        for i, pos in enumerate(position):
            time = (target - pos) / speed[i]
            if time not in hashMap:
                hashMap[time] = []
            hashMap[time].append(i)

    

        return len(hashMap)
