class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)

        max_heap = []
        res = []

        for num, freq in cnt.items():
            max_heap.append((-freq, num))
        
        heapq.heapify(max_heap)


        for _ in range(k): # pop
            _, num = heapq.heappop(max_heap)
            res.append(num)

        return res