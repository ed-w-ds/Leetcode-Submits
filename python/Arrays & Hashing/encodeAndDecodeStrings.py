class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    # O(n^2) 
    def encode(self, strs):
        # write your code here
        encode = ""
        for s in strs:
            encode += str(len(strs)) + "#" + s
        return encode

    # O(n)
    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        res, i = [], 0

        while i < len(str):
            j = i
            while str[j] != "#":
                 j += 1
            wordLength = int(str[i:j])
            res.append(str[j + 1 : j + 1 + wordLength])
            i = j + 1 + wordLength
        return res
