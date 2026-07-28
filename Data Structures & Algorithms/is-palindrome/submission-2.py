

class Solution:
    def isPalindrome(self, s: str) -> bool:
        low_s = "".join(char.lower() for char in s if char.isalnum())
        return low_s == low_s[::-1]