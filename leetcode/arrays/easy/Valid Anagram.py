from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt_s = Counter()
        for let in s:
            cnt_s[let] += 1
        cnt_t = Counter()
        for let in t:
            cnt_t[let] += 1 
        
        return cnt_s == cnt_t