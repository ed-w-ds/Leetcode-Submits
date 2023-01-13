class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # time - 0(n)(O(s+t)), space - O(s+t)
        return Counter(s) == Counter(t)
