class Solution:
    def trap(self, height: List[int]) -> int:
        # Max rect - heights inside?

        # traps are formed between max left + max right?

        # Two pointer: find the first left peak then find the corresponding right peak
        # a left peak is defined by a non decreasing height to a decreasing height 
        # a right peak is increasing height to non decreasing height
            # the rectangle they form is the maximum container for those peaks
            # keep track of the heights between them and the trapped water is the difference
        # repeat starting at the right peak as the left peak till end of list
        
            # How to detect if its just evenness in the floor?
                # Just keep going saving peaks?  till we find one thats as tall as the left peak 
                