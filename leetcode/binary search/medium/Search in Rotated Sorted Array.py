class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        orig_min = nums[0]
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            # If nums[mid] > target 
            # ie. 3,4*,5,6,1,2 then first nums[mid] = 5 > 4
            # If nums[mid] > orig
            if target < orig_min:
                if  nums[mid] >= orig_min:
                    l = mid + 1
                elif nums[mid] < orig_min:
                    if nums[mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1
            else:
                if nums[mid] < orig_min:
                    r = mid - 1
                else:
                    if nums[mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1
        return -1