import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_seen = {}
        for num in nums:
            if num in nums_seen:
                nums_seen[num] += 1
            else:
                nums_seen[num] = 1
        most_freq=[]
        for key in nums_seen:
            heapq.heappush(most_freq,(-nums_seen[key], key))
        k_freq = []
        for i in range(0,k):
            k_freq.append(heapq.heappop(most_freq)[1])
        return k_freq