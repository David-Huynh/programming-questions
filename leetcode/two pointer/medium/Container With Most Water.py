class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # start in the middle move left till its 


        # question 1: would the optimal left wall be the optimal for every wall ? 
        # no 
        

        # area = min(height[i] , height[j]) * j-i
        # 
        upperIndex = len(heights) - 1
        lowerIndex = 0
        area = 0
        while lowerIndex < upperIndex:
            upperHeight = heights[upperIndex]
            lowerHeight = heights[lowerIndex]
            area = max(area, (upperIndex-lowerIndex)*min(upperHeight,lowerHeight))
            if lowerHeight < upperHeight:
                lowerIndex += 1
            else:
                upperIndex -= 1
        return area