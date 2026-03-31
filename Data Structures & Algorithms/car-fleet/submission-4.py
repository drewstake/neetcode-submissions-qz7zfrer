class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        fleet = 0
        maxt = 0

        for i, position in enumerate(position):
            t = (target - position) / speed[i]
            cars.append((position, t))
        
        cars.sort(reverse=True) 

        for pos, time in cars:
            if time > maxt:
                fleet += 1
                maxt = time

        return fleet