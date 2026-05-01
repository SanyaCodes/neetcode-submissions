class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l,r,max_len = 0,0,0
        seen = set()

        while r<len(s):

            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            
            # to cal single char string len
            curr_len = r-l+1
            if max_len<curr_len:
                max_len = curr_len

            seen.add(s[r])
            r+=1

        return max_len
                      
        