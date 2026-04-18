class Solution:
    def isPalindrome(self, s: str) -> bool:
        # true if palindrome
        
        import re
        s = re.sub(r'[^A-Za-z0-9]', '', s)
        print(s)

        length = len(s)

        for i in range(length):
            if i == length-i-1 or i >= length-i-1:
                break
            if s[i].lower() == s[length-i-1].lower():
                continue
            else:
                return False
        return True
        
# tac a cat
# len = 9
# i = 0 --- 8
# i = 1 --- 7
# i = 2 --- 6
# i = 3 --- 5
# i = 4 --- 4