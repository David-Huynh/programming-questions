class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lowerIndex = 0 
        upperIndex = len(numbers) - 1
        while lowerIndex < upperIndex:
            if numbers[upperIndex]>target - numbers[lowerIndex]:
                upperIndex -= 1
            elif numbers[upperIndex]<target - numbers[lowerIndex]:
                lowerIndex += 1
            else:
                return [lowerIndex+1,upperIndex+1]
        return []