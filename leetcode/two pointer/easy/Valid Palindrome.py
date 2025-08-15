class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s=""
        for c in s:
            if c.isalnum():
                cleaned_s = cleaned_s + c.lower()
        start = 0
        while start < len(cleaned_s)//2:
            if not cleaned_s[start] == cleaned_s[-(start+1)]:
                return False
            start +=1

        return True 