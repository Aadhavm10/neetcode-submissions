class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = [c.lower() for c in s if c.isalnum()]
        l = 0
        r = len(arr) - 1

        while(l < r):
            if arr[l].lower() != arr[r].lower():
                return False
            l +=1
            r -=1
        
        return True
        