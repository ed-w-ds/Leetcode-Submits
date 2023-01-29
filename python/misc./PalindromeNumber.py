class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False

        divisor = 1
        while x >= divisor * 10:
            divisor *= 10

        while x:
            rigth = x % 10
            left = x // divisor

            if left != rigth: return False

            x = (x % divisor) // 10

            divisor = divisor / 100

        return True
