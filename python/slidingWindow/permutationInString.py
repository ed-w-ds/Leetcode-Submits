class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # O(n) + O(26) = O(n)
        if len(s1) > len(s2): return False

        s1count, s2count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1count[ord(s1[i]) - ord("a")] += 1 # get the ascii value or the character in s1
            s2count[ord(s2[i]) - ord("a")] += 1
        
        matches = 0
        for i in range(26):
            if s1count[i] == s2count[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # adding a character
            index = ord(s2[r]) - ord('a')
            s2count[index] += 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s2count[index] == s1count[index] + 1:
                matches -= 1
                
            #removing a character
            index = ord(s2[l]) - ord("a")
            s2count[index] -= 1
            if s1count[index] == s2count[index]:
                matches += 1
            elif s2count[index] == s1count[index] -1:
                matches -= 1
            l += 1
        return matches == 26
            
            
            
