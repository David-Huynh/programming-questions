class Solution:
    def count(self, s: str):
        cnt_s = Counter()
        for let in s:
            cnt_s[let] += 1
        return cnt_s
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_to_words = {}
        for word in strs:
            letters = frozenset(self.count(word).items())
            if letters in anagram_to_words:
                anagram_to_words[letters].append(word)
            else:
                anagram_to_words[letters] = [word]
        anagram_grouped = []
        for key in anagram_to_words:
            anagram_grouped.append(anagram_to_words[key])
        return anagram_grouped