class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
    # a defaultdict is a dict subclass that calls a factory function (in this case, list) to supply missing values. This means that if you try to access a key that does not exist in the dictionary, it will automatically create that key with a default value (in this case, an empty list) rather than raising a KeyError.
        results = defaultdict(list) # val : index
        
        for s in strs:
            count = [0] * 26
            for c in s:
                # counting how many of each character we have
               count[ord(c) - ord("a")] += 1
            # append the string, group all anagrams of the particular count together
            # lists cannot be keys, so change it to tuple, as tuples are non-mutable (can't be changed)
            results[tuple(count)].append(s)
        # returns just the values not the keys
        return results.values()
    
#     class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
#         result = defaultdict(list)

#         for words in strs:
#             count = [0] * 26
#             for character in words:
#                 count[ord(character) - ord("a")] += 1
#             result[tuple(count)].append(words)
#         return result.values()
