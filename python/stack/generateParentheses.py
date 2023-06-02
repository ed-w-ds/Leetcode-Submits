class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(openN, closedN, string):
            if len(string) == (n * 2):
                return result.append(string)
                
            if openN < n:
                backtrack(openN + 1, closedN, string + '(')

            if openN > closedN:
                backtrack(openN, closedN + 1, string + ')')

        backtrack(0, 0, '')
        return result
