class Solution:
    def longestPalindrome(self, s: str) -> str:
        curr_s,curr_max = "",0

        for i in range(len(s)):

            # odd length
            l,r = i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>curr_max:
                    curr_s = s[l:r+1]
                    curr_max = r-l+1
                r += 1
                l -= 1

            # even length
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1)>curr_max:
                    curr_s = s[l:r+1]
                    curr_max = r-l+1
                r += 1
                l -= 1

        return curr_s



        