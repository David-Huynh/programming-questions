class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = {}
        for num in nums:
            if not  dup.get(num, None) == None:
                return True
            dup[num] = num
        return False
            