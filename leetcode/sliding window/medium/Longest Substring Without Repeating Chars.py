class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # What if you greedily add to your substring and 
        # if theres a duplicate cut the prefix off and continue
        l = 0
        ss_dict = {}
        max_ss_len = 0
        for i, c in enumerate(s):
            if c in ss_dict:
                l = max(ss_dict[c]+1, l)
            ss_dict[c] = i
            max_ss_len = max(max_ss_len, i-l+1)

        return max_ss_len