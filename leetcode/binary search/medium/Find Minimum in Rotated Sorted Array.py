class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Well if the array is not rotated then min is nums[0]
        # IF rotation then nums[-1] < nums [0] since unique 
            # We split array in half then we can either land at the original beginning part or
            # the original ending tail
            # since we know if a rotation happened then if we find at nums[len//2] is < nums[0] we must be at the orig start half
            # else we are at the orig ending 

        # tldr modified binary search with some constraints/priority
        l = 0
        r = len(nums) - 1
        orig_min = nums[0]
        if nums[0] > nums[-1]:
            while l<r:
                if nums[(l+r)//2] < orig_min:
                    r = (l+r)//2
                else:
                    l = (l+r)//2 + 1
                
            return nums[l]
        else:
            return nums[0]