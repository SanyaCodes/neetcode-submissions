class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l,r,max_l = 0,0,0
        seen = set()

        while r < len(s):

            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            curr_l = r-l+1
            if max_l < curr_l:
                max_l = curr_l
            seen.add(s[r])
            r += 1

        return max_l
            


            
        