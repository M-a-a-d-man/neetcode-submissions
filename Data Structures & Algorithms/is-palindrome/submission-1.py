import re
class Solution:
    def isPalindrome(self, s: str) -> bool:


        lower_s = s.lower()

        clean_s = re.sub(r'[^a-zA-Z0-9]', '', lower_s)
        
        s_list = list(clean_s)
        length = len(s_list)
        left = 0
        right = length - 1

        while left < right:
            if s_list[left] != s_list[right]:
                return False
            left += 1
            right -= 1
        return True
            
        