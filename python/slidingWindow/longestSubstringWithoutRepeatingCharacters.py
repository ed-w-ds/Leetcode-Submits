class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # O(n) O(n)
        longestString = 0
        l = 0
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            longestString = max(longestString, len(charSet))
        return longestString
