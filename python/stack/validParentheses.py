# time: O() | space: O()
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        hashmap = {'}' : '{', ')' : '(', ']' : '['}
        if len(s)%2 != 0:
            return False
        else: 
            for c in s:
                if c in hashmap:
                    if stack and stack[-1] == hashmap[c]:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(c)
            return True if not stack else False
