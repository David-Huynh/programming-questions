class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lowerIndex = 0 
        upperIndex = len(numbers) - 1
        targetTriplets = []
        while lowerIndex < upperIndex:
            if numbers[upperIndex]>target - numbers[lowerIndex]:
                upperIndex -= 1
            elif numbers[upperIndex]<target - numbers[lowerIndex]:
                lowerIndex += 1
            else:
                upperNum = numbers[upperIndex]
                lowerNum = numbers[lowerIndex]
                targetTriplets.append([lowerNum, upperNum, -target])
                while (upperNum == numbers[upperIndex] or lowerNum == numbers[lowerIndex]) and lowerIndex < upperIndex:
                    if upperNum == numbers[upperIndex]:
                        upperIndex -= 1
                    if lowerNum == numbers[lowerIndex]:
                        lowerIndex += 1
        return targetTriplets
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # its the 2 sum problem n times after sorting xddddddd
        nums.sort()
        triplets = []
        lastTarget = None
        for i, target in enumerate(nums):
            if target <= 0 and not target == lastTarget:
                twoSum = self.twoSum(nums[i+1:], -target)
                if not twoSum == []:
                    triplets = triplets + twoSum
            lastTarget = target
        return triplets



