import bisect
class MedianFinder:
    # A sorted list so binary search to insert then findmedian is justhe middle number or the average of the two middles?
    def __init__(self):
        self.sorted_list = []

    def addNum(self, num: int) -> None:
        self.sorted_list.insert(bisect.bisect_left(self.sorted_list, num), num)

    def findMedian(self) -> float:
        length = len(self.sorted_list)

        if length % 2 == 0:
            return self.sorted_list[length//2]/2 + self.sorted_list[length//2 - 1]/2
        return self.sorted_list[length//2]