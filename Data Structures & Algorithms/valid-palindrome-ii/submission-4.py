class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == "".join(reversed(s)):
            return True
        def isPalindrome(left, right):
            
            return s[left:right+1] == "".join(reversed(s[left:right+1]))

        left = 0
        right = len(s) - 1

        while left < right:

            if s[left] == s[right]:
                left += 1
                right -= 1

            else:
                return (
                    isPalindrome(left + 1, right) or
                    isPalindrome(left, right - 1)
                )

        return True