class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Forward Pass
        prefix = {0: 1}
        for i, num in enumerate(nums):
            prefix[i+1] = prefix[i]*num

        # Backward Pass
        suffix = {len(nums):1}
        for i in range(len(nums)-1,-1,-1):
            suffix[i] = suffix[i+1]*nums[i]
        # Compute Product 
        output = []
        for i, num in enumerate(nums):
            output.append(prefix[i] * suffix[i+1])

        return output