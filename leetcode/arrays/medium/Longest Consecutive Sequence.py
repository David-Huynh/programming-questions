class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen = {}
        starts = {}
        for num in nums:
            # Find starts
            starts.pop(num+1, None)
            if not num-1 in seen:
                starts[num] = True
            seen[num] = True
        
        count = 0
        longest = 0
        # Count from starts 
        for start in starts:
            while True:
                longest = max(longest,count+1)
                if start+count+1 in seen:
                    count += 1
                else: 
                    count = 0
                    break
        return longest