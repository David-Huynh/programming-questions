class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_map = {}
        for i, val in enumerate(nums):
            if val in target_map:
                return [target_map.get(val),i]
            else:
                target_map[target-val] = i
        return []